# to import random module
import random

# to create a range of random numbers between 1-10
n = random.randint(1,9)
chanceCount=0
# to take a user input to enter a number
print("Welcome to the NUMBER GUESSING GAME")
print("You have 5 chances to guess the number...")
guess = int(input("Enter any number between 1 to 9: "))
while chanceCount<5: # means if n is not equal to the input guess
    # if guess is smaller than n
    if guess < n:
        if n-guess<=2:
            print("Very close!!! Just slightly less!!!")
            
        else:
            print("Too low!")
        
        chanceCount=chanceCount+1
        # to again ask for input
        guess = int(input("Enter number again: "))
        
    # if guess is greater than n
    elif guess > n:
        if guess-n<=2:
            print("Very close!!! Just slightly high!!!")

        else:
            print("Too high!")
        
        chanceCount=chanceCount+1
        # to again ask for the user input
        guess = int(input("Enter number again: "))
       
    # if guess gets equals to n terminate the while loop
    elif guess==n:
        print("Congratulations!!You guessed it right!!")
        break

if not chanceCount<5:
    print ("You LOSE!!You are out of chances... The number is",n)