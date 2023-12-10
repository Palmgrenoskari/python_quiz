import random

# Asks user specified number of random questions from the question set provided
def quiz(questions, num_of_questions):
  # Keep track of correct answers
  correct = 0
  print('\n--- Quiz time! ---\n')
  # Loop num_of_q times
  for i in range(num_of_questions):
    # random question from questions
    question = random.choice(questions)
    # Print the question property of question object
    print(question['question'])
    # Print answer options from options property of question object
    for answer_option in question['options']:
      print(answer_option)
    
    # Use our user_choice function here too to get answer from user
    answer = user_choice('Your answer (A,B,C or D): ', ['A', 'B', 'C', 'D'])

    # If correct -> congratulate and correct++
    if (answer == question['answer']):
      correct += 1
      print('\nCorrect!\n')
    # Else tell the correct answer
    else:
      print('\nWrong. The correct answer was', question['answer'], '\n')

  # Return num of correct answers
  return correct

# Add a question to specified difficulty textfile
def add_question(difficulty):
  # Our question
  question = input("Enter the question: ")
  # Enter the choices one by one, use a cool list comprehension here and add the letter in front of each answer option
  options = [option + ': ' + input(f'Enter answer option {option}: ') for option in ['A', 'B', 'C', 'D']]
  # Give the correct answer, prevent bad answers with user_choice function
  answer = user_choice('Which one is the correct answer? (A,B,C or D): ', ['A', 'B', 'C', 'D'])
  # Make our new question object
  new_question = {'question': question, 'options': options, 'answer': answer}

  # Onto writing the question into the file, use 'a' parameter to append
  # Questions are stored in format: Question|A: Mikki|B: Hiiri|C: Aku|D: Ankka|C
  with open(f'./questions/{difficulty}.txt', 'a') as file:
    # Looks confusing but the end result is basically: '|'.join(list)
    # Our answer options are already a list, and we turn our question and answer also onto list, then add all together to form a whole list, which we then join with '|'.
    file.write('\n' + '|'.join([new_question['question']] + new_question['options'] + [new_question['answer']]))
  print('\nQuestion added successfully\n')



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
  return questions

# Get user user choice and return it, make sure userchoice is in list of available options
def user_choice(prompt, options):
  while True:
    user_input = input(prompt)
    if (user_input in options):
      return user_input
    else:
      print('Your choice is not found in the available options, please try again')

# Print varying results based on the portion of correct answers
def end_result(correct_answers, num_of_questions):
  print('\n--- Results ---\n')
  # All correct
  if (correct_answers == num_of_questions):
    print(f'WHAT A GENIUS!\nYou got everything correct {correct_answers}/{num_of_questions}')
  # None correct
  elif (correct_answers == 0):
    print(f'What happened? I can\'t believe it.\nYou got none of the answers correct {correct_answers}/{num_of_questions}')
  # Else just print score
  else:
    print(f'Your score: {correct_answers}/{num_of_questions}')

  # Another quiz?
  print('\nAnother Quiz?')


# Basic quiz loop
while True:
  print('\n----- Quiz App -----\n')
  print('1 - Take a Quiz')
  print('2 - Add a Question')
  print('3 - Exit')
  # Choose from the above options
  option = user_choice('Choose an option(1, 2 or 3): ', ['1', '2', '3'])

  if (option == '1'):
    # Choose difficulty
    difficulty = user_choice('Choose difficulty(easy, medium, hard or insane): ', ['easy', 'medium', 'hard', 'insane'])
    # Load chosen difficulty questions
    questions = load_questions(difficulty)
    # Choose num of questions, current possible answers 3,4,5,6,7,8,9,10
    # Need to stringify numbers for user_choice function to work properly
    num_of_questions = int(user_choice('How many questions do you want to answer(3-10): ', [str(n) for n in range(3,11)]))
    # Quiz loop, store correct answers.
    correct_answers = quiz(questions, num_of_questions)
    # Print how many user got correct out of X number of questions
    end_result(correct_answers, num_of_questions)
  elif (option == '2'):
    # Choose difficulty
    difficulty = user_choice('Choose difficulty for your question(easy, medium, hard or insane): ', ['easy', 'medium', 'hard', 'insane'])
    # Question adding loop, add question to chosen difficulty .txt file
    add_question(difficulty)
  elif (option == '3'):
    print('Exit successful')
    break
  

