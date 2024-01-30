a = int(input("enter the amount"))
if a < 104 and a > 0:
    b = a % 10
    c = b % 5
    d = a // 10
    e = b // 5
    print ("the 10 coins are: ",d)
    print ("the 5 coins are: ",e)
    print ("the 1 coins are: ",c)
else:
    print ("number out of range")