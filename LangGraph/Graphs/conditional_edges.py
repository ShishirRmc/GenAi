from typing import Dict, TypedDict, List
from langgraph.graph import StateGraph, START, END

# graph that uses conditional edges
class StateAgent2(TypedDict):
  num1: int
  num2: int
  num3: int
  num4: int
  final1: int
  final2: int
  operation1: str
  operation2: str

def addition1(State: StateAgent2) -> StateAgent2:
  """ first addition """
  State['final1'] = State['num1'] + State['num2']
  return State

def substraction1(State: StateAgent2) -> StateAgent2:
  """ first substraction """
  State['final2'] = State['final1'] - State['num3']
  return State

def next_node(State: StateAgent2) -> StateAgent2:
  """selects first batch of next nodes"""
  if State['operation1']=='+':
    return "first_addition"

  elif State['operation1'] == '-':
    return 'first_substraction'

def addition2(State: StateAgent2) -> StateAgent2:
  """ second addition """
  State['final1'] = State['final1'] + State['num4']
  return State

def substraction2(State: StateAgent2) -> StateAgent2:
  """ second substraction """
  State['final2'] = State['final2'] - State['num4']
  return State

def next_node1(State: StateAgent2) -> StateAgent2:
  """selects second batch of next nodes"""
  if State['operation2']=='+':
    return "second_addition"

  elif State['operation2'] == '-':
    return 'second_substraction'

graph3 = StateGraph(StateAgent2)

graph3.add_node('first_adder', addition1)
graph3.add_node('first_subber', substraction1)
graph3.add_node('router', lambda State: State)
graph3.add_node('second_adder', addition2)
graph3.add_node('second_subber', substraction2)
graph3.add_node('router1', lambda State: State)

graph3.add_edge(START, 'router')

graph3.add_conditional_edges(
    'router',
    next_node,
    {
        'first_addition': 'first_adder',
        'first_substraction': 'first_subber'
    }
)

graph3.add_conditional_edges(
    'router1',
    next_node1,
    {
        'second_addition': 'second_adder',
        'second_substraction': 'second_subber'
    }
)

graph3.add_edge('first_adder', 'router1')
graph3.add_edge('first_subber', 'router1')


graph3.add_edge('second_adder', END)
graph3.add_edge('second_subber', END)

app3 = graph3.compile()
# display(Image(app3.get_graph().draw_mermaid_png()))
initial_state = StateAgent2(num1 = 10, operation1="-", num2 = 5, num3 = 7, num4=2, operation2="+", final1= 0, final2 = 0)
print(app3.invoke(initial_state))
