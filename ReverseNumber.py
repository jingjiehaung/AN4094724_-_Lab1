
"""Exercise 2 (30%): Name your file ReverseNumber.ipynb. Write the following function to 
display an integer in reverse order:
def reverse(number):
For example, reverse(3456) displays 6543. Write a test script that prompts the user to enter 
an integer and displays its reversal (hint and note: The main reversal logic can be solved in 
multiple ways. For example, you can convert the number into a string and reverse the string. 
You can also store all the numeric values into a list (covered in the later module) and reverse 
the contents. For now, please try to solve the problem at its most naïve and algorithmic way. 
Think of the combo usage of while loop, %, // and display its reversal directly inside the while 
loop).
"""
"""
以相反的順序顯示一個整數：
定義反向（數字）：
比如reverse(3456)顯示6543，寫一個測試腳本提示用戶輸入
一個整數並顯示其反轉（提示和注意：主要反轉邏輯可以在
多種方式。 例如，您可以將數字轉換為字符串並反轉字符串。
您還可以將所有數值存儲到一個列表中（在後面的模塊中介紹）並反轉
內容。 現在，請嘗試以最天真和算法的方式解決問題。
想想while循環、%、//的組合用法，直接在while裡面顯示它的反轉
環形）。
"""
#定義函數
def reverse(num):
    #除數
    divisor = 10
    #while迴圈 判斷 輸入數值是否被除數整除為0
    while num // divisor != 0:
        #要先把最後一個數字移到第一個(判斷除是數否為10
        if divisor == 10:
            Num = num%divisor
            print("{}".format(Num),end ="")
        #print("{}".format(Num),end ="")
        else :#除數超過10以上
            Num = num%divisor//((divisor//10)) #取餘數後再取整數(如：543%100 = 43,43//(100//10)
            print("{}".format(Num),end ="")
        divisor *= 10 #除數*10
        #print(count)
    print("{}".format(num//(divisor//10)))
num = int(input('Enter an integer:'))
reverse(num)












