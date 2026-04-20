#  AI Research Agent

A fully automated research agent built with **FastAPI**, **Groq (LLaMA 3.3)**, **DuckDuckGo Search**, and **Pydantic structured output**.  
It takes a user topic → performs web search → analyzes information using LLM → returns a structured research report.
This cotains the backend code 
---

## Features

- ✔ **Research Automation**: Takes any topic and performs live internet lookup.
- ✔ **DuckDuckGo Search Tool**: Free, no-API-key search integration.
- ✔ **Groq LLaMA-3.3 LLM Processing**: Fast, high-accuracy model reasoning.
- ✔ **Pydantic Structured Output**: Ensures predictable JSON responses.
- ✔ **FastAPI Endpoint**: Ready for deployment.

---

##  Tech Stack

| Component         | Technology                       |
|------------------|----------------------------------|
| Web Framework     | FastAPI                          |
| LLM               | Groq – LLaMA-3.3-70B             |
| Search Engine     | DuckDuckGo (ddgs)                |
| Agent Logic       | Custom                           |
| Output Parsing    | LangChain PydanticOutputParser   |
| Runtime           | Python 3.10–3.12                 |

---pip install -r requirements.txt
cd ai-research-agent
uvicorn maain:app --reload
cd frontend 
npm start / npm run build 


## 📂 Project Structure

