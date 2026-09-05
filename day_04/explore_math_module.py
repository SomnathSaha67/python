import math
print('\n'.join(cont for cont in dir(math) if cont.startswith("_")==False))
print(f"Years required to double and investment at 8% annual: {math.log(2)/math.log(1.08):.2f}")