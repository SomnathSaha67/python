import logging, traceback

logging.basicConfig(level= logging.ERROR, format= "%(levelname)s - %(message)s")

class DivisionByZeroError(Exception):
  pass

class InvalidConversionError(Exception):
  pass

def risky_function(x):
  if x=="zero":
    raise DivisionByZeroError("Attempted divison by zero")
  elif x=="bad":
    raise InvalidConversionError("Invalid type conversion attempted")
  else:
    return int(x)*2
  
for test_input in ["zero", "bad", "5"]:
  try:
    result= risky_function(test_input)
    print(f"Result: {result}")
  except (DivisionByZeroError, InvalidConversionError, ValueError) as e:
    print(f"Plain print(e): {e}")

    tb_str= traceback.format_exc()
    logging.error(tb_str)