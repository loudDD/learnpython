# 题目：一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同。
#
# 程序分析：无。

def nuM():

    num = input("pls enter:")
    if num[0] == num[-1]:
        if num[1] == num[-2]:
            print("这是回文数")
    else:
        print("不是")


nuM()