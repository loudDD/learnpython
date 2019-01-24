# 对10个数进行排序。

#冒泡


def orderlist():

    a = [4,1,4,40,31,45,23]

    for i in range(len(a)):
        for j in range(len(a)-1):
            if a[j] < a[j+1]:
                a[j],a[j+1] = a[j+1],a[j]

    print(a)


if __name__ == "__main__":
    orderlist()
