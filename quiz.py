# Get user user choice and return it, make sure userchoice is in list of available options
def user_choice(prompt, options):
  while True:
    user_input = input(prompt)
    if (user_input in options):
      return user_input
    else:
      print('Your choice is not found in the available options, please try again')

# Basic quiz loop
while True:
  print("--- Quiz App ---")
  print("1 - Take a Quiz")
  print("2 - Add a Question")
  print("3 - Exit")
  option = user_choice("Choose an option(1, 2 or 3): ", ['1', '2', '3'])

  if (option == "1"):
    print('quiz loop here')
  elif (option == '2'):
    print('Add question loop here')
  elif (option == '3'):
    print('Exit successful')
    break
  

