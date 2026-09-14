age_input= "27" 
salary_input = "55000.50" 
is_subscribed_input = "True"

print(f"Before type conversion:\ntype of '{age_input}': {type(age_input)}\ntype of '{salary_input}': {type(salary_input)}\ntype of '{salary_input}': {type(salary_input)}\n")
print(f"After type conversion:\ntype of '{age_input}': {type(int(age_input))}\ntype of '{salary_input}': {type(float(salary_input))}\ntype of '{is_subscribed_input}': {type(bool(is_subscribed_input))}")