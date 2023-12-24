import random

user=input("Enter 'r'for rock 'p' for paper and 's' for scissor:")
computer=random.choice(['r','p','s'])

if((user=='r' and computer=='s')or (user=='p' and computer=='r') or (user=='s' and computer=='p')):
    print("You win")

elif(user==computer):
    print("It's a tie")

else:
    print("You lose")