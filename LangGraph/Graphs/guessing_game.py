from typing import Dict, TypedDict, List
from langgraph.graph import StateGraph, START, END

# guess game

import random
class StateAgent3(TypedDict):
  player_name: int
  target: int
  guessed: List[int]
  counter: int
  hint: str
  lower_bound: int
  higher_bound: int


#greet/setup, guess, hint, should continue or not
lower_bound = 1
higher_bound  = 20

def greeter(state: StateAgent3) -> StateAgent3:
  """initialize the game"""
  state['player_name'] = f"welcome to the game {state['player_name']}"
  state['target'] = random.randint(1, 20)
  state['guessed'] = []
  state['counter'] = 0
  state['hint'] = f"the number you guessed is "
  return state


def guesser(state: StateAgent3) -> StateAgent3:
  """ part where we guess the number """
  guesses = [i for i in range(lower_bound, higher_bound + 1) if i not in state['guessed']]
  if guesses:
    guess = random.choice(guesses)
  else:
    guess = random.randint(lower_bound, higher_bound)

  state['guessed'].append(guess)
  state['counter'] = state['counter'] + 1
  print(f"Attempt {state['guessed']}: Guessing {guess} (Current range: {lower_bound} to {higher_bound})")
  return state


def hint(state: StateAgent3) -> StateAgent3:
  """ gives hint to the user """
  latest_guess = state['guessed'][-1]
  target = state['target']
  if latest_guess < state['target']:
    print(f"Hint: The target number is greater than {latest_guess}.")
  elif latest_guess > state['target']:
    print(f"Hint: The target number is less than {latest_guess}.")

  else:
    print(f"Congratulations! You guessed the number {state['target']} in {state['counter']} attempts.")

  return state

def should_continue(state: StateAgent3) -> StateAgent3:
  """ checks if we should continue or not """
  latest_guess = state['guessed'][-1]
  if latest_guess == state["target"]:
        print(f"GAME OVER: Number found!")
        return "end"
  elif state["counter"] >= 7:
        print(f"GAME OVER: Maximum attempts reached! The number was {state['target_number']}")
        return "end"
  else:
        print(f"CONTINUING: {state['counter']}/7 attempts used")
        return "continue"

graph4 = StateGraph(StateAgent3)

graph4.add_node(greeter, "greeter")
graph4.add_node(guesser, "guesser")
graph4.add_node("hint_node", hint)

graph4.add_edge('greeter', 'guesser')
graph4.add_edge('guesser', 'hint_node')

graph4.add_conditional_edges(
    'hint_node',
    should_continue,
    {
        'continue': 'guesser',
        'end': END
    }
)

graph4.set_entry_point("greeter")

app4 = graph4.compile()

# from IPython.display import display, Image
# display(Image(app4.get_graph().draw_mermaid_png()))

initial_game_state_2 = StateAgent3(player_name = "shishir", target = 0, guessed = [], counter = 0, hint = "", lower_bound = 1, higher_bound = 20)
result = app4.invoke(initial_game_state_2)


