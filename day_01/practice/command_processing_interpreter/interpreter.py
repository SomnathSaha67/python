result=0
while True:
  operation= input("Enter operation('EXIT' to stop): ")
  if operation.upper()=='EXIT':
    break
  else:
    operation= operation.split(" ")
    try:
      if operation[0].upper() in ['ADD', 'MULTIPLY', 'SUBTRACT', 'DIVIDE']:
        if operation[0].upper()=='ADD':
          result+=float(operation[1])
        elif operation[0].upper()=='MULTIPLY':
          result*=float(operation[1])
        elif operation[0].upper()=='SUBTRACT':
          result-=float(operation[1])
        elif operation[0].upper()=='DIVIDE':
          result/=float(operation[1])
      else:
        print("Invalid Operation")
    except ValueError:
      print("Invalid Value")
    except ZeroDivisionError:
      print("Cannot divide by Zero")
    print(f"Result: {result}")
print(f"Final Result: {result}")
