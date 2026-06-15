def main():
  initial_name, initial_role= "", ""
  while True:
    command= input("Enter command('n' to stop): ")
    if command=='n':
      break
    valid_command, name, role, asked_command= validate_command(command, initial_name, initial_role)
    if valid_command:
      if asked_command=="SET:name:" or asked_command=="SET:role:":
        initial_name, initial_role= name, role
        continue
      else:
        if asked_command=="GET:name:":
          print(f"Name: {name}")
        else:
          print(f"Role: {role}")
    else:
      print("Invalid command")
def validate_command(command, name, role):
  first_colon_position= command.find(":")
  second_colon_position= command.find(":", first_colon_position+1)
  if command[0:second_colon_position+1] in ["SET:name:", "GET:name:", "SET:role:", "GET:role:"]:
    if command[0:first_colon_position]=="SET":
      if command[first_colon_position+1:second_colon_position]=="name":
        name= command[second_colon_position+1:]
      else:
        role= command[second_colon_position+1:]
      return True, name, role, command[0:second_colon_position+1]
    else:
      if name.isspace() or role.isspace():
        if name.isspace():
          name= "not given"
        if role.isspace():
          role= "not given"
        return True, name, role, command[0:second_colon_position+1]
      elif command[first_colon_position+1:second_colon_position]=="name":
        return True, name, 0, command[0:second_colon_position+1]
      elif command[first_colon_position+1:second_colon_position]=="role":
        return True, 0, role, command[0:second_colon_position+1]
  else:
    return False, 0, 0, 0
if __name__=="__main__":
  main()