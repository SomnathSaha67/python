data_list = [10, "Google", 3.5, True] 
data_tuple = (10, "Google", 3.5, True)

print(f"List before: {data_list} | id: {id(data_list)}")
print(f"Tuple before: {data_tuple} | id: {id(data_tuple)}")

data_list[1]= "Microsoft"
print(f"\nList after reasignment: {data_list} | id: {id(data_list)}")  #id unchanged

#data_tuple[1]= "Microsoft" #TypeError
print(f"\nTuple after failed reassignement: {data_tuple} | id: {id(data_tuple)}")

nested= (1, 2, [3, 4])
print(f"\nNested tuple before: {nested} | id: {id(nested)}")
print(f"Inner list id before: {id(nested[2])}")

nested[2].append(5)
print(f"\nNested tuple after modifying inner list: {nested} | id: {id(nested)}")
print(f"Inner list id after: {id(nested[2])}")