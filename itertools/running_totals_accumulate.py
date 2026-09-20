from itertools import accumulate
import operator

daily_sales = [120, 85, 200, 60, 150, 90]

running_sum= list(accumulate(daily_sales))

running_product= list(accumulate(daily_sales, operator.mul))

running_max= list(accumulate(daily_sales, max))

print("Day  |  Sales  |  Running Sum  |  Running Product  |  Running Max  ")
for i, sale in enumerate(daily_sales, start=1):
  print(f"{i:3}  |  {sale:5}  |  {running_sum[i-1]:11}  |  {running_product[i-1]:14}   |  {running_max[i-1]:11}")