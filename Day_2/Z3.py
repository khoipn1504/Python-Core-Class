import math

print('Phương trình ax^2 + bx +c = 0 trong đó: ')
a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))

delta = math.pow(b, 2) - 4 * a * c

if delta < 0:
    print('Phương trình vô nghiệm.')
elif delta == 0:
    x = -b/(2*a)
    print('Phương trình có nghiệm kép x = ', x)
elif delta > 0:
    x1 = (-b+math.sqrt(delta))/(2*a)
    x2 = (-b-math.sqrt(delta))/(2*a)
    print('Phương trình có 2 nghiệm x1 = %s và x2 = %s' % (x1, x2))
