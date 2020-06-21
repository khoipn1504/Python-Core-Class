def check():
    a = int(input())
    b = int(input())
    try:
        print(a/b)
    except EOFError:
        print("Loi khong tim thay file")
    except ZeroDivisionError:
        raise

    finally:
        print("ASD")


try:
    check()
except ZeroDivisionError:
    print("loi nham")
