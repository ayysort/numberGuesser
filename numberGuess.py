# word guesser !!
import random
print(' ')
print(' ')
print('Welcome to the Number Guesser!')
print(' ')
print(' ')

count = 0

high = input("I'm thinking of a number between 1 and _?: ")
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
