x=int(input())
if x%4==0:
    if x%100==0:
        if x%400==0:
            print("LEAP")
        else:
            print("NOPE")
    else:
        print("LEAP")
else:
    print("NOPE")


