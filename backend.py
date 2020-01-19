import time
from moves import move
global opt
opt=0
def valid(bo,num,pos):
	for i in range(9):
		if bo[i][pos[1]] == num and pos[0]!=i:
			return False
	for i in range(9):
		if bo[pos[0]][i] == num and pos[1]!=i:
			return False
	for i in range((pos[0]//3)*3,(pos[0]//3)*3+3):
		for j in range((pos[1]//3)*3,(pos[1]//3)*3+3):
			if bo[i][j]==num and pos!=(i,j):
				return False
	return True
	
def empty(bo):
	for i in range(9):
		for j in range(9):
			if bo[i][j]==0:
				return (i,j)
	return None
				
def solve(bo):
        global opt
        a=empty(bo)
        if a:
           for i in range(1,10):
              if valid(bo,i,a):
                 bo[a[0]][a[1]]=i
                 opt+=1
                 #move(i,(a[0],a[1]),(0,0))
                 if solve(bo):
                   return True
                 bo[a[0]][a[1]]=0			
        else:
           return True
        return False

if __name__=='__main__':
      board=[[6,0,0,0,0,0,0,0,5],
             [0,4,0,0,0,3,0,0,0],
             [2,3,0,0,0,0,0,0,0],
             [3,0,0,1,0,0,5,4,0],
             [0,0,0,3,2,0,8,7,0],
             [0,0,0,0,0,8,0,1,0],
             [0,0,1,0,0,6,2,0,0],
             [0,0,3,0,0,0,0,0,7],
             [9,0,0,4,5,0,6,0,1]]
      st=time.time()
      if solve(board):
             end=time.time()			
             for i in range(9):
                     for j in range(9):
                             print(board[i][j],end='  ')
                     print()

      print('time taken:',end-st)
      print('moves:',opt)
