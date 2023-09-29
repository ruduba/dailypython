import random as r
def guess(x):
    random_number = r.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"guess a number between 1 and {x}: "))
        if guess < random_number:
            print("guess too low")
        elif guess > random_number:
            print("guess too high")
        
    print(f"you are right the number is {random_number}") 
guess(10)
