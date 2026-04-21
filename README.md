# AI Research Agent

Backend-only AI research API built with FastAPI, LangChain, Groq, and SearchAPI.
It accepts a user research query, performs web search, and returns structured output.

## Features

- FastAPI API with `/research` endpoint
- Groq LLM (`MODEL` from `.env`)
- SearchAPI tool integration for live web results
- Structured response parsing with Pydantic
- Fallback to internal knowledge only when search results are not useful

## Tech Stack

| Component | Technology |
|---|---|
| Web Framework | FastAPI |
| LLM | Groq via `langchain-groq` |
| Agent Runtime | LangChain `create_agent` |
| Search Tool | SearchAPI (`SearchApiAPIWrapper`) |
| Validation | Pydantic |
| Runtime | Python 3.10+ |

## Project Structure

- `main.py` - FastAPI app and `/research` endpoint
- `agent.py` - LangChain agent setup and lazy initialization
- `tools.py` - Search tool (`search_user_query`)
- `schemas.py` - Request/response models
- `prompt.py` - Output parser setup
- `requirements.txt` - Python dependencies

## Environment Variables

Create a `.env` file in project root:

```env
MODEL=llama-3.3-70b-versatile
GROQ_API_KEY=your_groq_api_key
SEARCHAPI_API_KEY=your_searchapi_key
```

## Installation

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

## Run the Server

```bash
uvicorn main:app --reload
```

Server runs at:
- `http://127.0.0.1:8000`

## API Endpoints

### Health Check

- `GET /`
- Response:

```json
{"message": "Agent is running"}
```

### Research Endpoint

- `POST /research`
- Request body:

```json
{
  "query": "latest AI news in 2026"
}
```

- Example response:

```json
{
  "answer": "The latest AI news in 2026 includes expanded Search Live, enhanced AI tools, and increased enterprise AI adoption.",
  "source": "SearchAPI",
  "confidence": "High"
}
```

## Notes

- Keep `.env` private. Never commit real API keys.
- If `MODEL` or `GROQ_API_KEY` is missing, `/research` returns a clear server error.
- `.gitignore` already excludes `venv/`, `__pycache__/`, and `.env`.
