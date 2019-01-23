# 2/1 3/2 5/3 8/5

def suM(n):
    result = 0.0
    a = 2
    b = 1
    for i in range(1,n+1):
        result += a / b
        t = a
        a = a + b
        b = t
        # print(b)
        # print(a)
        print(result)
suM(20)

# 题目：求1+2!+3!+...+20!的和。
# 
# 程序分析：此程序只是把累加变成了累乘。