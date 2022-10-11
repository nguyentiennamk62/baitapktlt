a = int(input("Nhập a: "))
b = int(input("Nhập b: "))
c = int(input("Nhập c: "))

def find_max(a, b, c):
    max = a
    if max < b:
        max = b
    if max < c:
        max = c
    return max;
print("GTLN trong ba số là: ",find_max(a,b,c))
