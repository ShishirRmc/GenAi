from typing import Dict, TypedDict, List
from langgraph.graph import StateGraph, START, END

class StateAgent(TypedDict):
  values: List[int]
  name: str
  process: str
  results: str

def processor(state: StateAgent) -> StateAgent:
  """ agent with multiple processes """
  if state['process'] == 'add':
        state['results'] = f"{state['name']} your result is: {str(sum(state['values']))}"

  elif state['process'] == 'multiply':
    res = 1
    for val in state['values']:
      res = res * val
    state['results'] = f"{state['name']} your result is: {res}"

  return state

graph1 = StateGraph(StateAgent)
graph1.add_node(processor, "processor")
graph1.set_entry_point("processor")
graph1.set_finish_point("processor")
app1 = graph1.compile()

# display(Image(app1.get_graph().draw_mermaid_png()))
answers_add = app1.invoke({'values': [1,2,3,4], 'name': 'shishir', 'process': 'add'})
answers_multiply = app1.invoke({'values': [1,2,3], 'name': 'shishir', 'process': 'multiply'})

print(answers_add['results'])
print(answers_multiply['results'])
