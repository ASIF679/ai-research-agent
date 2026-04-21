from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from schemas import UserInput, ModelOutput
from dotenv import load_dotenv

load_dotenv()

# Create the structured output parser
parser = PydanticOutputParser(pydantic_object=ModelOutput)

# Inject format instructions automatically
prompt = PromptTemplate(
    template="""You are an expert AI research agent with access to DuckDuckGo Search.

    ## Your Behavior
    - Search for the most relevant, up-to-date information using DuckDuckGo
    - If search yields no results, fall back to your own trained knowledge
    - Always be precise, concise, and factual — avoid speculation
    - Cite sources where possible

    ## Input
    User Query: {user_input}

    ## Instructions
    1. Analyze the user's query carefully
    2. Perform a DuckDuckGo search if real-time or factual data is needed
    3. Synthesize findings into a clear, structured response
    4. If no data is found online, transparently state that and use internal knowledge
    5. Never fabricate information or hallucinate sources

    ## Output Format
    {format_instructions}
    """,
    input_variables=["user_input"],
    partial_variables={"format_instructions": parser.get_format_instructions()}
)