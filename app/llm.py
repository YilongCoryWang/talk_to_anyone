from langchain.chat_models import init_chat_model
import os
from app.config import LLM_API_KEY, TAVILY_API_KEY
from langchain_tavily import TavilySearch

os.environ["DEEPSEEK_API_KEY"] = LLM_API_KEY
os.environ["TAVILY_API_KEY"] = TAVILY_API_KEY
llm = init_chat_model("deepseek-chat", model_provider="deepseek")

# Tools
tool = TavilySearch(max_results=2)
tools = [tool]
llm_with_tools = llm.bind_tools(tools)