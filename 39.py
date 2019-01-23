#题目：有一个已经排好序的数组。现输入一个数，要求按原来的规律将它插入数组中。

def orderList(n):
    a = [1,30,40,41,50]
    print("插入前" ,a)
    for i in range(len(a)):
        if a[i] < n and a[i+1] >n :
            a.insert(i+1,n)
            break
    print("插入 %d" %(n))
    print("插入后" , a)

if __name__ == "__main__":
    orderList(31)