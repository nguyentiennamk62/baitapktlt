def gt(a):
    if a==0:
        return 1
    else:
        i=1
        t=1
        while(i<=a):
            t=t*i
            i=i+1
        return t
a = int(input("nhap a:"))
x = gt(a)
print("giai thua cua %d là %d" %(a,x))