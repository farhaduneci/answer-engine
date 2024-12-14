from typing import List

import logfire
from environs import Env
from fastapi import FastAPI
from pydantic import BaseModel, Field
from pydantic_ai import Agent
from pydantic_ai.result import Cost
from tavily import AsyncTavilyClient

from app import prompts

logfire.configure()

env = Env()
env.read_env()

tavily_client = AsyncTavilyClient(api_key=env("TAVILY_API_KEY"))


class SearchResult(BaseModel):
    title: str
    url: str
    content: str


class SearchQuery(BaseModel):
    query: str = Field(max_length=256)


class SearchAnswer(BaseModel):
    answer: str = Field(description="The answer to the user query")


class SearchResponse(BaseModel):
    result: SearchAnswer
    usage: Cost


search_agent = Agent(
    model=env("MODEL_NAME"),
    result_type=SearchAnswer,
    system_prompt=prompts.SEARCH_SYSTEM_PROMPT,
)


@search_agent.tool_plain
async def search_result(query: str) -> List[SearchResult]:
    """Searches the web for the given query and returns the search results."""

    search_results = []

    for result in (await tavily_client.search(query))["results"]:
        search_results.append(SearchResult(**result))

    return search_results


app = FastAPI()


@app.post("/search", response_model=SearchResponse)
async def search(query: SearchQuery):
    answer = await search_agent.run(query.query)
    return SearchResponse(result=answer.data, usage=answer.cost())
