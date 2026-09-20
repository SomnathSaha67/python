from itertools import groupby, cycle

statuses = ["OK", "OK", "OK", "FAIL", "FAIL", "OK", "OK", "TIMEOUT"]

print("Consecutive grouping with groupby:")
for status, group in groupby(statuses):
  count= len(list(group))
  print(f"{status}: {count}")

statuses_unsorted= ["OK", "FAIL", "OK", "TIMEOUT", "FAIL", "OK"]

print("\nGrouping on unsorted/scattered list:")
for status, group in groupby(statuses_unsorted):
  count= len(list(group))
  print(f"{status}: {count}")

agents = ["Agent_A", "Agent_B", "Agent_C"]
tickets = 7

print("\nTicket assignment:")
for ticket_num, agent in zip(range(1, tickets+1), cycle(agents)):
  print(f"Ticket {ticket_num} -> {agent}")