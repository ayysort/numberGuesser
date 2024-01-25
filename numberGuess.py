# word guesser !!
import random
import time

print(' ')
print(' ')
print('Welcome to the Number Guesser!')
print(' ')

count = 0
play = True


while play == True:
  while True:
    print(' ')
    high = input("I'm thinking of a number between 1 and _?: ")
    if high.isdigit():
      break
    else:
      print("   Wrong Input... Please enter a number")
    
  number = random.randint(1, int(high))

  print(' ')
  print(' ')
  print("I'm thinking...")
  time.sleep(2)
  
  print(' ')
  print(' ')
  print(' ')
  print('Ok, I got one!')
  print("I'm thinking of a number between 1 and", int(high))

  while True:    #game
    
    guess = input("Guess the number: ")

    while not guess.isdigit():
      print("   Invalid input... Please enter a number.")
      guess = input("Guess the number: ")

    
    count = count + 1
    
    if int(guess) == number:
      print(' ')
      print(' ')
      print('Correct!')
      break
    elif int(guess) > number:
      print(' ')
      print(' ')
      print('Lower than', guess)
    elif int(guess) < number:
      print(' ')
      print(' ')
      print('Higher than', guess)
    else:
      print('Wrong Input...')

  if count == 1:
    print("Wow! That took", count, 'attempt!')
  else:
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
    
print(' ')
print('Thanks for playing!')
print(' ')
