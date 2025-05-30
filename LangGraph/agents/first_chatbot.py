# simple chatbot chat accepts a message and returns a response  using the LLM
from typing import TypedDict, List
from langchain_core.messages import HumanMessage
from langgraph.graph import StateGraph, START, END
from langchain.chat_models import init_chat_model
import os
from dotenv import load_dotenv

load_dotenv()
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")

llm = init_chat_model(
    "google_genai:gemini-2.0-flash",
    temperature=0
)

class FirstChatbot(TypedDict):
    messages: List[HumanMessage]

def first_chatbot(state: FirstChatbot) -> FirstChatbot:
    """ simple chatbot that gives response to the queries asked by the user """
    response = llm.invoke(state['messages'])
    print(f"Ai Response: {response.content}")
    return state

graph = StateGraph(FirstChatbot)
graph.add_node('first_chatbot', first_chatbot)
graph.add_edge(START, 'first_chatbot')
graph.add_edge('first_chatbot', END)

app = graph.compile()

user_input = input("Enter: ")
while user_input.lower() != "exit":  # Added case-insensitive check for "exit"
    app.invoke({"messages": [HumanMessage(content=user_input)]})  # Pass user input as a HumanMessage to the app
    user_input = input("Enter: ")