import random
n=random.randint(1, 100)
print("Welcome to the number guessing game!")
print("I have selected a number between 1 and 100.")
print("Try to guess it in as few attempts as possible.")
a= -1
guesses=0
while(a!=n):
    guesses +=1
    a=int(input("Guess a number: "))
    if(a>n):
        print("Lower number Please")
    else:
        print("Higher number Please")
print(f"You have guessed the number {n} correctly in {guesses} attempts")            
        
        