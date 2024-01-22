# word guesser !!
import random
print('Welcome to the Word Guesser!')



high = input('How High?: ')
number = random.randint(1, int(high))


while True:
  guess = int(input("Guess the number:  "))
  if guess == number:
    print('Correct!')
    break
  elif guess > number:
    print('Lower')
  elif guess < number:
    print('Higher')

