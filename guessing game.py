import random

def guess(x):
    num=random.randint(1,x)
    a=0
    while num!=a:
        a=int(input("Enter a number:"))

        if a>num:
            print("Try again!! Your guess is too high.")

        elif a<num:
            print("Try again!! Your guess is too low.")

        else:
            print(f"Yeah you did it. The correct number is {num}.")

guess(5)