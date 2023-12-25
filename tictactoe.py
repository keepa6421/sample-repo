def board(x,y):
    zero='X' if x[0] else ('O' if y[0] else 0)
    one='X' if x[1] else ('O' if y[1] else 1)
    two='X' if x[2] else ('O' if y[2] else 2)
    three='X' if x[3] else ('O' if y[3] else 3)
    four='X' if x[4] else ('O' if y[4] else 4)
    five='X' if x[5] else ('O' if y[5] else 5)
    six='X' if x[6] else ('O' if y[6] else 6)
    seven='X' if x[7] else ('O' if y[7] else 7)
    eight='X' if x[8] else ('O' if y[8] else 8)
    print(f"{zero} | {one} | {two}")
    print(f"{three} | {four} | {five}")
    print(f"{six} | {seven} | {eight}")

def check():
    if (x[0]==1 and x[1]==1 and x[2]==1) or (x[3]==1 and x[4]==1 and x[5]==1) or (x[6]==1 and x[7]==1 and x[8]==1) or (x[0]==1 and x[4]==1 and x[8]==1) or (x[2]==1 and x[4]==1 and x[6]==1) or (x[0]==1 and x[3]==1 and x[6]==1) or (x[1]==1 and x[4]==1 and x[7]==1) or (x[2]==1 and x[5]==1 and x[8]==1):
        return 1
    if (y[0]==1 and y[1]==1 and y[2]==1) or (y[3]==1 and y[4]==1 and y[5]==1) or (y[6]==1 and y[7]==1 and y[8]==1) or (y[0]==1 and y[4]==1 and y[8]==1) or (y[2]==1 and y[4]==1 and y[6]==1) or (y[0]==1 and y[3]==1 and y[6]==1) or (y[1]==1 and y[4]==1 and y[7]==1) or (y[2]==1 and y[5]==1 and y[8]==1):
        return 0

if __name__=="__main__":
    print("Welcome to Tic-Tac-Toe")
    x=[0,0,0,0,0,0,0,0,0]
    y=[0,0,0,0,0,0,0,0,0]
    turn=1 #1 for X and 0 for O
    while(True):
        board(x,y)
        if(turn==1):
           print("X's chance")
           value=int(input("Please enter a value:"))
           x[value]=1
        else:
            print("O's chance")
            value=int(input("Please enter a value:"))
            y[value]=1
        turn=1-turn
        a=check()
        if a==0 or a==1:
            break
    if a==1:
      print("X wins")
    else:
        print("Y wins")
        
        
