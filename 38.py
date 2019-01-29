# 题目：求一个3*3矩阵主对角线元素之和。


def sum():
    sum = 0
    a = []
    for i in range(3):
        a.append([])
        for j in range(3):
            a[i].append(int(input("pls enter:")))

    for i in range(3):
        sum += a[i][i]

    print(sum)

if __name__=="__main__":
    sum()