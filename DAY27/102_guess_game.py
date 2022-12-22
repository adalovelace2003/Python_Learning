import random
randNumber = random.randint(1, 100)
print(randNumber)
userGuess = None
guess = 0  

while (userGuess != randNumber):
    userGuess = int(input("Enter your guess between 1 and 100: "))
    if (userGuess == randNumber):
        print("You guessed it right!")
    else:   
        if ( userGuess > randNumber):    
            print("Your guess is  high") 
        elif ( userGuess < randNumber):  
            print("Your guess is   low") 

    guess += 1

print(f"\n\n\nYou guessed the number in {guess} times")

#  writing hi score to the file 

with open("DAY27/hiscore.py") as f:
    hiscore = int(f.read())
    
if (guess < hiscore) :
    print("You have just broken the high score ")
    with open("DAY27/hiscore.py","w") as f:
        f.write(str(guess))
    