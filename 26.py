# 题目：利用递归方法求5!。
#
# 程序分析：递归公式：fn=fn_1*4!

def sum(n=5):
    if n == 0:
        return 1
    return  n * sum(n-1)

a = sum()
print(a)