import pyautogui
import pygetwindow as gw
import pickle

#pyautogui.moveTo(x,y, duration = 0)
#pyautogui.click(x,y) 

'''
USEFUL CODE
w=gw.getWindowsWithTitle('Remote Control - Redmi Go')[0]
print(w.topleft.x,w.topleft.y)
pyautogui.moveTo(w.topleft.x,w.topleft.y, duration = 0)
pyautogui.moveTo(1169,617, duration = 0)
#The place where i record the coords is (790 107)


#Parsing (code for writing the button extension files)
arr=[]
with open('process.txt','r') as f:
    lines=f.readlines()
op=0
for i in range(9):
    tmp=[]
    for j in range(9):
       tmp.append(convert(lines[op].replace('\n','')))
       op+=1
    arr.append(tmp)
for i in arr:
    print(i)
pickle.dump(arr,open('box.button','wb'))
'''

'''
try:
    w=gw.getWindowsWithTitle('Remote Control - Redmi Go')[0]
    win=(w.topleft.x,w.topleft.y)
except IndexError:
    print('No window found')
    exit()
'''
#load data
coords=pickle.load(open('box.button','rb'))
other=pickle.load(open('otherdict.button','rb'))



def convert(string):
    """Function takes tuple strings as input and returns tuples"""
    return tuple(int(i) for i in string.replace('(','').replace(')','').split(','))

def move(num,pos,win):
    """ Takes 3 args\n:
        num-number to place\n{int}
        pos-postion to place the number{tuple}
        win-top left corner of the window{tuple}
    """
    pos=coords[pos[0]][pos[1]]
    pyautogui.click(other[num][0],other[num][1],duration=0.1)
    pyautogui.click(pos[0],pos[1],duration=0.1) 

    


#move(4,(3,4),(0,0))




        




    
