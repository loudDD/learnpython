# 题目：给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字。
#
# 程序分析：学会分解出每一位数。
def nuM():
    a= input("less than 5 character:")
    b = len(a)
    print("it is %d character" %(b))
    c = a[::-1]
    for i in c:
        print("the number is %d" %(int(i)))
nuM()