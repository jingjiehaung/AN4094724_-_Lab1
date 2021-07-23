"""
練習 3 (30 %)：將您的文件命名為 RemoveOutliers.ipynb。分析收集的數據時
作為科學實驗的一部分，可能需要在之前刪除最極端的值
執行其他計算。編寫一個接受值列表的函數 remove_outliers
和一個非負整數 n 作為其參數。該函數應該返回一個帶有 n 的列表
刪除的最大元素和最小的 n 個元素以及異常值列表。的順序
返回列表中的元素不必與原始元素的順序匹配
列表。
編寫一個 Python 程序來演示您的函數。它應該提示用戶輸入
數字 n，一些數據，用“q”或“Q”表示輸入的結束，並通過調用前面描述的函數從中刪除 n 個最大和 n 個最小值。顯示原始列表，
刪除異常值的列表和異常值。下面是一個示例運行
"""
#輸入要移除的個數
n = int(input("Enter the number of smallest and largest values to remove: "))
#建立新的列表
a_list = []
outlier_remove_list = []
outliter_list = []
#輸入數值
num = input("Enter a value (q or Q to quit): ")
#while迴圈判斷輸入是否為Q
while num != "q" and num != "Q":
    a_list += [int(num)]
    num = input("Enter a value (q or Q to quit): ")
#輸出原有資料
print("The original data:",end = " ")
print(a_list)

outlier_remove_list = a_list
#計數
count = 0
#while 迴圈 移除最大最小值 ，並加入移除數值到outlier_list
while count < n:
    outliter_list.append(max(a_list))
    outliter_list.append(min(a_list))
    outlier_remove_list.remove(max(a_list))
    outlier_remove_list.remove(min(a_list))
    #計數加1
    count+=1
#重新排列並輸出
outlier_remove_list.sort()
outliter_list.sort()
print("The data with the outliers removed:" ,end = " ")
print(outlier_remove_list)
print("The outliers:" , end = " ")
print(outliter_list)

    
