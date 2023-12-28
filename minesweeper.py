
import random

class board:
    def __init__(self,size,bomb):
        self.size=size
        self.bomb=bomb
        self.board=self.newboard()

        #let's create board
        # initialize to keep track of loations we've covered
        # we'll save (row,col) tuples into list
        self.dug=set()
    
    def newboard(self):
        #generate new board
        board=[[None for i in range(self.size)] for i in range(self.size)]
        number=0
        while number<self.bomb:
            loc=random.randint(0,self.dim_size**2-1)
            row=loc//self.dim_size
            col=loc%self.dim_size

            if board[row][col]=='*':
                #this means we've planted bomb
                continue

            board[row][col]="*"
        bombs_planted+=1
        return board
    