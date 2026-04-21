from langchain_core.tools import tool
import os 
from dotenv import load_dotenv
load_dotenv() 
from langchain_community.utilities import SearchApiAPIWrapper
search=SearchApiAPIWrapper()


@tool
def search_user_query(query: str) -> str:
    """Search the web for real-time information based on user query."""
    results = search.run(query)
    return results if results else "No results found."



if __name__ == "__main__":
   result= search_user_query.invoke("latest AI news 2026")
   print(result)