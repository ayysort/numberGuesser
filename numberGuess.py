# word guesser !!
import random
print(' ')
print(' ')
print('Welcome to the Number Guesser!')
print(' ')
print(' ')

count = 0
play = True

while play == True:
  while True:
    high = input("I'm thinking of a number between 1 and _?: ")
    if high.isdigit():
      break
    else:
      print("Wrong Input.. Please type in a number")
    
  number = random.randint(1, int(high))

  print(' ')
  print('Ok, I got one!')
  print("I'm thinking of a number between 1 and", int(high))

  while True:
    
    guess = int(input("Guess the number:  "))
    
    count = count + 1
    
    if guess == number:
      print('Correct!')
      break
    elif guess > number:
      print('Lower')
    elif guess < number:
      print('Higher')
    else:
      print('Wrong Input...')

  print("That took", count, 'attempts.')
  
  
  again = input("Would you like to play again? (y/n): ")
  if again == 'y':
    count = 0
    continue
  elif again == 'n':
    break
  else:
    while True:
      print("Wrong Input...")
      again2 = input("Would you like to play again? (y/n): ")
      if again2 == 'y':
        count = 0
        break
      elif again2 == 'n':
        play = False
        break
      else:
        continue
