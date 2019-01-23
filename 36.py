#求100内素数之和

def su():
    lower = 1
    upper = 100

    for i in range(lower,upper+1):
        if i > 1:
            for num in range(2,i):
                if i%num == 0:
                    break
            else:
                print(i)

su()