import os
from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_groq import ChatGroq
from tools import search_user_query

load_dotenv()

tools = [search_user_query]
agent_executor = None


def get_agent_executor():
    global agent_executor
    if agent_executor is not None:
        return agent_executor

    model_name = os.getenv("MODEL")
    if not model_name:
        raise RuntimeError("MODEL is missing. Set it in your .env file.")
    if not os.getenv("GROQ_API_KEY"):
        raise RuntimeError("GROQ_API_KEY is missing. Set it in your .env file.")

    llm = ChatGroq(
        model=model_name,
        temperature=0,
    )
    agent_executor = create_agent(
        model=llm,
        tools=tools,
        system_prompt=(
            "You are an expert AI research agent. Always call the `search_user_query` tool at least once "
            "before giving a final answer. Prefer tool results over internal knowledge. "
            "Use internal knowledge only if the tool returns no useful information. "
            "When tool results are used, set source to SearchAPI or a relevant URL from those results. "
            "Keep answers factual and do not hallucinate sources."
        ),
    )
    return agent_executor