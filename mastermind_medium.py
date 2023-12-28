import random

# list of colors
colors=["red","blue","purple","orange","white","pink","green"]
# here is our guesses
guess=[]
temp=""
# here g is our tracker 
g=["  ","  ","  ","  ","  "]
# checking
correct="white"
needs_to_be_corrected="red"
wrong="blank"
# secret
code=["red","blue","pink","white","orange"]
while g!=["white","white","white","white","white"]:
    print(colors)
    guess=[]
    for i in range(5):
     temp=input("Enter your colors:")
     guess.append(temp)
    

    for index, value in enumerate(guess):
       if value in code:
          g[index]="red"

    
    for index,(value1,value2) in enumerate(zip(code,guess)):
       if value1==value2:
          g[index]="white"
          
    random.shuffle(g)
    print(g)

if g==["white","white","white","white","white"]:
   print("YAY")


