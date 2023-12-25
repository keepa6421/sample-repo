import random
from words import word
word=random.choice(word)
used_words=[]
live=6
a = ["-" for _ in word]
# Convert the list to a string for printing
a_str = "".join(a)
print(a_str)
b_str=""
j=0
while live!=0 and a_str!=word:
    user_input=input("Enter a letter:")
    used_words.append(user_input)
    print(used_words)
    if user_input in word:
        print("You guessed it")
        for i in range(len(word)):
            if user_input == word[i]:
                # Replace the corresponding dash in a_str
                a_str = a_str[:i] + user_input + a_str[i + 1:]

        print(a_str)
    else:
        print("Oops try again")
        live=live-1
        print(f"Your current life is {live}")

if live>0:
    print("Yay you won the game!!")

else:
    print("Sorry you lost.")


