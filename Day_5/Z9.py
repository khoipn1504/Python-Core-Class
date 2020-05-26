def cong(*arg):
    tong=0
    for i in arg:
        tong+=i
    return tong
a=[1,2,3,4]
print(cong(*a))