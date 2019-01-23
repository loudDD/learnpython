# 题目：利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来。
#
# 程序分析：无。

def printReverse(n):
    i = n[::-1]
    for j in i:
        print(j)

printReverse([1,2,3])

def printRever(n):
    if len(n)== 0:
        return
    else:
        return n[::-1]


b = input("pls enter :")
a = printReverse(b)