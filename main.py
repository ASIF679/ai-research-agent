from fastapi import FastAPI
from fastapi import HTTPException
from dotenv import load_dotenv
from agent import get_agent_executor
from schemas import UserInput
from prompt import parser

load_dotenv()

app = FastAPI()

@app.get("/")
def check():
    return {"message": "Agent is running"}

@app.post("/research")
def research(user_input: UserInput):
    try:
        agent_executor = get_agent_executor()
    except RuntimeError as exc:
        raise HTTPException(status_code=500, detail=str(exc)) from exc

    result = agent_executor.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": (
                        f"{user_input.query}\n\n"
                        "Important behavior rules:\n"
                        "- Call search_user_query first.\n"
                        "- Use search results as primary evidence.\n"
                        "- Only use Internal Knowledge if search has no useful results.\n"
                        "- If you used search results, source must be SearchAPI (or a URL from the results).\n\n"
                        "Return your final answer using this exact format:\n"
                        f"{parser.get_format_instructions()}"
                    ),
                }
            ]
        }
    )
    output = result["messages"][-1].content
    if isinstance(output, list):
        output = " ".join(
            block.get("text", "") if isinstance(block, dict) else str(block)
            for block in output
        )
    parsed = parser.parse(str(output))
    return parsed