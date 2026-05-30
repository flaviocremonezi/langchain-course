from typing import List
from pydantic import BaseModel, Field

from dotenv import load_dotenv

load_dotenv()
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from tavily import TavilyClient
from langchain_community.tools.tavily_search import TavilySearchResults

class Source(BaseModel):
    """Schema for a source used by the agent"""

    url:str = Field(description="The URL of the source")

class AgentResponse(BaseModel):
    """Schema for agent response with and answer and sources"""

    answer:str = Field(description="The agent's answer to the query")
    sources: List[Source] = Field(default_factory=list, description="List of sources used to generate the answer")

llm=ChatOpenAI(model="gpt-5")
tools=[TavilySearchResults()]
agent=create_agent(model=llm, tools=tools, response_format=AgentResponse)

def main():
    print("Hello")
    result = agent.invoke({"messages":HumanMessage(content="search for 3 job posting for an ai engineer usig langchain in the bay area on linkedin and list their details")})
    print(result)

if __name__ == "__main__":
    main()