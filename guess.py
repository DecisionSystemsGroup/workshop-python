import random

guesses = 0

print ("Hello, what is your name?")
players_name = raw_input()

number = random.randint(1,20)
print ("Well, " + players_name + " I am thinking of a number between 1 and 20. Can you guess it? You have 5 tries.")
print number

while guesses <6 :

    guess = input()

    if guess > number:
        print "Your guess is higher than the number i am thinking"

    elif guess < number:
        print "Your guess is lower than the number i am thinking"

    elif guess == number:
        break

    guesses=guesses+1
    
if guess == number:
    print "you found the number i was thinking"

else:
    print "you lost... try again later"
