
while True:
    try:
        num = int(input("enter number "))
        if num == 0:
            print(1)
        a=1
        while num>1:
            a*=num
            num-=1
        print(a)
    except:
        break