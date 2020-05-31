def hello(a): return print('hello %s' % (a))


hello('Khoi')


def myFilter(songuyen):
    ans = []
    for i in songuyen:
        if i % 2 == 0:
            ans.append(i)
    return ans


songuyen = [1, 2, 3, 4, 5, 6, 7, 8]
filtered = list(filter(lambda a: a % 2 == 0, songuyen))
print(myFilter(songuyen))
print(filtered)
