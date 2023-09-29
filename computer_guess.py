import random as r
def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        guess = r.randint(low, high)  # Always choose a number between low and high
        feedback = input(f"is {guess} too high (H), too low (L), or correct (C)?").lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
            
    print(f"the number is {guess}")

computer_guess(9)
