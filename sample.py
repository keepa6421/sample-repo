import random
from words import word

word = random.choice(word)
used_words = []
live = 6

a = ["-" for _ in word]

# Convert the list to a string for printing
a_str = "".join(a)
print(a_str)
