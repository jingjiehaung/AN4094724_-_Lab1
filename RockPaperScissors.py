"""
練習 1 (20%)：將文件命名為 RockPaperScissors.ipynb。 寫個程序來玩
石頭，紙，剪刀遊戲。 遊戲將 (1) 要求您輸入 Rock、Paper 或
Scissors, (2) 隨機生成 Rock, Paper, or Scissors 和 (3) 確定它是否
是贏、平或輸。 當您贏得第一場胜利時，遊戲將退出。 （提示：您可以導入
通過調用 import random 和使用 random.randint(1, 3) 從 python 中獲得隨機模塊
生成隨機數 1、2 或 3)
"""
"""
Welcome to ROCK, PAPER, SCISSORS game!
Enter your move: (r)ock (p)aper (s)cissors r
ROCK versus...
ROCK
"""
import random
#定義變數
global count
global win
global lose
global tie
count = 0
win = 0
lose =0
tie = 0
#定義class(電腦的手勢
class Computer:
    def Move():
        ComMoveRandom = random.randint(1,3)
        if ComMoveRandom == 1:
            ComMove = "Rock"
            
        elif ComMoveRandom == 2:
            ComMove = "Paper"
 
        else :
            ComMove = "Scissors"
        print(ComMove)
        #判斷用
        return ComMoveRandom
#定義玩家的手勢
def User_Move(Move):
    if Move == "r":
        userMove = "Rock"
        user = 1
    elif Move == "p":
        userMove = "Paper"
        user = 2
    elif Move == "s":
        userMove = "Scissors"
        user = 3
    print(userMove,'versus...')
    #判斷用
    return user
#定義判斷輸贏
def WinOrLoser(User_num,Com_num):
    global win
    global lose
    global tie
    num = 3
    if User_num == Com_num:
        num = 0
    else:
        if User_num == 1 and Com_num == 3:
             num =1
        elif User_num == 2 and Com_num == 1:
             num = 1
        elif User_num == 3 and Com_num == 2:
             num = 1
        else :
             num = 2
    if num == 1:
        print("You win!")
        win +=1
        count = 1
    elif num == 2 :
        print("You lose!")
        lose +=1
        count = 0
    elif num == 0:
        print("It is a tie!")
        tie +=1
        count = 0
    return count
    
print("Welcome to ROCK, PAPER, SCISSORS game!")
while  count == 0:
    
    Move = input(" Enter your move: (r)ock (p)aper (s)cissors :  ") #Move 剪刀石頭布
    #User_Move(Move)
    #Computer.Move()
    #WinOrLoser(User_Move(Move),Computer.Move())
    count = WinOrLoser(User_Move(Move),Computer.Move())
    #tie
print("You have {} ties and {} losses before your first win.".format(tie,lose))

    
    
    
    
   
    










    
    
