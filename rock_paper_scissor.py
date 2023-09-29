#rock paper scissor
import random as r
def play():
    user = input("what's your choice? 'r' for rock, 'p' for paper, 's' for scissors\n") 
    computer = r.choice(['r', 'p', 's'])

    if user == computer:
        return f"computer chose {computer}, it's a tie"

    if is_win(user, computer):
        return f'computer chose {computer}, you won! :)'
    
    return f'computer chose {computer}, you lost :('
    
    
def is_win(player, opponent):
    if (player == 'r' and opponent =='s') or (player == 'p' and opponent == 'r') or (player == 's' and opponent == 'p'):
        return True
       
print(play())

