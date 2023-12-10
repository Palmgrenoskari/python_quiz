# Load questions from easy/medium/hard/insane txt file
# Split question, answer choices and correct answer into different properties inside questions list
def load_questions(difficulty):
  questions = []
  # Read from current dir/questions/difficulty.txt
  with open(f'./questions/{difficulty}.txt', 'r') as file:
    for line in file:
      # strip to get rid of linebreaks, split using | 
      parts = line.strip().split('|')
      # Append to question as question, options, answer properties
      # First we have the question, then 4 options/answer choices, then the actual answer
      questions.append({
        'question': parts[0],
        'options': parts[1:5],
        'answer': parts[5]
      })
  # Finally return the questions list
  print(questions)
  return questions

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
  print('--- Quiz App ---')
  print('1 - Take a Quiz')
  print('2 - Add a Question')
  print('3 - Exit')
  option = user_choice('Choose an option(1, 2 or 3): ', ['1', '2', '3'])

  if (option == '1'):
    difficulty = user_choice('Choose difficulty(easy, medium, hard or insane): ', ['easy', 'medium', 'hard', 'insane'])
    load_questions(difficulty)
  elif (option == '2'):
    print('Add question loop here')
  elif (option == '3'):
    print('Exit successful')
    break
  

