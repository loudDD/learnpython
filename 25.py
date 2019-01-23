# 题目：求1+2!+3!+...+20!的和。
#
# 程序分析：此程序只是把累加变成了累乘。题目：求1+2!+3!+...+20!的和。
#
# 程序分析：此程序只是把累加变成了累乘。

def sum(n=20):
    result = 0
    a = 1
    for i in range(1,n+1):
        a *=i
        result +=a
    print(result)

sum()