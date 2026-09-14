plan_type= "pro"   #"basic", "pro", "enterprise"
country_code= "IN"
is_student= True
account_age_months= 18   #loyalty check threshold

if (plan_type)=="basic": base_price= 10.0
elif (plan_type=="pro"): base_price= 20.0
elif (plan_type=="enterprise"): base_price= 50.0
else: base_price= 15.0

price= base_price

if (is_student): price*=0.5
else:
  if (country_code in ("IN", "BR", "ZA")): price*=0.9
  else: price= price

if (plan_type!="enterprise"): 
  if (account_age_months>12): price= price
  else: price+=5.0
else: price+=10.0

print(f"Final subscription price: ${price}")