from typing import Dict, TypedDict, List
from langgraph.graph import StateGraph, START, END

# multiple nodes

class StateAgent1(TypedDict):
  fullname: str
  age: int
  skills: List[str]
  resultss: str

def process_names(state: StateAgent1) -> StateAgent1:
  """agent that gives full name"""
  state['fullname'] = f"hi, {state['fullname']}, welcome to the system!"
  return state

def process_age(state: StateAgent1) -> StateAgent1:
  """agent that gives age"""
  if state['age']<14:
    state['age'] = f"You're {state['age']} so we recommend use the kids mode"
  else:
    state['age'] = f"You're {state['age']} so we recommend use the normal mode"
  return state

def process_skill_result(state: StateAgent1) -> StateAgent1:
  """agent prints all skills in formatted strings
  and combines the response in results"""
  formatted_skills = ', '.join(state['skills'])
  state['skills'] = f"your skills are {formatted_skills}"

  state['resultss'] = f'{state["fullname"]}, {state["age"]}, {state["skills"]}'
  return state

graph2 = StateGraph(StateAgent1)

graph2.add_node("names", process_names)
graph2.add_node("ages", process_age)
graph2.add_node("skilllist", process_skill_result)

graph2.set_entry_point("names")

graph2.add_edge("names", "ages")
graph2.add_edge("ages", "skilllist")

graph2.set_finish_point("skilllist")

app2 = graph2.compile()
answers = app2.invoke({'fullname':'shihsir', 'age':20, 'skills':["python", "java"]})
answers['resultss']
