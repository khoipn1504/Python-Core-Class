a = int(input())
b = int(input())
try:
    print(a/b)
except EOFError:
    print("Loi khong tim thay file")
except ZeroDivisionError:
    print("Loi chia cho 0")
