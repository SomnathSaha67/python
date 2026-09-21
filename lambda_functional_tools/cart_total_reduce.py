from functools import reduce

cart = [("Item1", 250, 2), ("Item2", 90, 5), ("Item3", 500, 1)]

line_totals= list(map(lambda item: item[1]*item[2], cart))

grand_total_map_reduce= reduce(lambda acc, x: acc+x, line_totals, 0)

grand_total_direct= reduce(lambda acc, item: acc+item[1]*item[2], cart, 0)

print(f"Line totals: {line_totals}")
print(f"Grand total (map -> reduce): {grand_total_map_reduce}")
print(f"Grand total (direct reduce): {grand_total_direct}")

print(f"Totals match? {grand_total_map_reduce==grand_total_direct}")