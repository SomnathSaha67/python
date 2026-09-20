from collections import deque

back_history= deque()
forward_history= deque()
current= None

def visit(url):
  global current
  if current:
    back_history.append(current)
  current= url
  forward_history.clear()
  print(f"Visited: {url}")
  print_state()

def back():
  global current
  if back_history:
    forward_history.appendleft(current)
    current= back_history.pop()
    print("Went back")
  else:
    print("No back hsitory")
  print_state()

def print_state():
  print(f"Back: {list(back_history)}")
  print(f"Current: {current}")
  print(f"Forward: {list(forward_history)}")
  print("---")

visit("google.com")
visit("github.com")
visit("stackoverflow.com")
visit("wikipedia.org")

back()
back()

visit("reddit.com")