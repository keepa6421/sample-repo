import random

def guess(x):
    low=1
    high=x
    num=None
    feedback=None
    while feedback!='c':
        if low!=high:
            num=random.randint(low,high)
        feedback=input(f"Is {num} too high(h), low(l) or correct")
        if feedback=='h':
            print("Try again!! Your guess is too high.")
            high=num-1
        elif feedback=='l':
            print("Try again!! Your guess is too low.")
            low=num+1

print(f"Yeah you did it. The correct number is {low}.")
        
guess(5)