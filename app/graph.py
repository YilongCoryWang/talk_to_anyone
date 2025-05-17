from langgraph.prebuilt import ToolNode, tools_condition
from langgraph.checkpoint.memory import MemorySaver
from app.llm import tools, llm_with_tools
from langgraph.graph import StateGraph, START, END
from typing import Annotated
from typing_extensions import TypedDict
from langgraph.graph.message import add_messages
import json
from langchain_core.prompts import ChatPromptTemplate

memory = MemorySaver()

class State(TypedDict):
    messages: Annotated[list, add_messages]
    person_name: str | None
    person_age: int | None

graph_builder = StateGraph(State)

def chatbot(state: State):
    if state.get("person_name") and state.get("person_age"):
        prompt = ChatPromptTemplate.from_messages([
            ("system", f"You are {state["person_name"]} at age {state["person_age"]}, let's talk in English."),
            ("user", "{input}")
        ])
        formatted_prompt = prompt.invoke({"input": state["messages"]})
        message = llm_with_tools.invoke(formatted_prompt)
        print(message)
        return {"messages": [message]}
    message = llm_with_tools.invoke(state["messages"])
    return {"messages": [message]}

tool_node = ToolNode(tools=tools)
graph_builder.add_node("tools", tool_node)
graph_builder.add_conditional_edges(
    "chatbot",
    tools_condition
)

def start_route(state):
    if state.get("person_name") is None or state.get("person_age") is None:
        return "interlocutor_retriever"
    return "chatbot"

graph_builder.add_node("chatbot", chatbot)
graph_builder.add_conditional_edges(START, start_route, {"interlocutor_retriever": "interlocutor_retriever", "chatbot": "chatbot"})
graph_builder.add_edge("tools", "chatbot")

def interlocutor_retriever(state: State):
    try:
        if messages := state.get("messages", []):
            message = messages[-1]
        else:
            raise ValueError("No message found in input")
        prompt = f'Please find person name and age from: {message}. Please only output string of dictionary'
        message = llm_with_tools.invoke(prompt)
        person = json.loads(message.content)
    except Exception as e:
        print(e)
    return {"messages": [message], "person_name": person["name"], "person_age": person["age"]}

def chatbot_interlocutor_route(state):
    if state.get("person_name") is None or state.get("person_age") is None:
        print("Can't find name or age. Please provide both name and age of the person you want to talk to.")
        return END
    return "chatbot"

graph_builder.add_node("interlocutor_retriever", interlocutor_retriever)
graph_builder.add_conditional_edges("interlocutor_retriever", chatbot_interlocutor_route, {"chatbot": "chatbot", END: END})

graph = graph_builder.compile(checkpointer=memory)