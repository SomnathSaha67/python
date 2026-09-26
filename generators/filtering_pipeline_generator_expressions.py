raw_numbers= [4, -7, 12, 0, 23, -5, 18, 9, -1, 30]

non_negatives= (x for x in raw_numbers if x>=0)

squares= (x**2 for x in non_negatives)

big_values= (x for x in squares if x>50)

result= list(big_values)
print(f"Chained generator result: {result}")

result_listcomp= [x**2 for x in raw_numbers if x>=0 and x**2>50]
print(f"List comprehension result: {result_listcomp}")