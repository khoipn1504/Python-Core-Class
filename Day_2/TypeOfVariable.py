'''
s = 'this is my text'
s1 = "this is my text"
# * nối chuỗi
print(s+s1)
'''

'''
print('Vui lòng nhập vào số a: ')
a=int(input())
print('Vui lòng nhập vào số b: ')
b=int(input())
# * cộng 2 số nhập vào
print(a+b)
'''

'''
# * cách khai báo số phức
z = 3 + 2j
print(z)
print('phần thực: ',z.real)
print('phần ảo: ',z.imag)

z1=complex(4,5)
print('phần thực: ',z1.real)
print('phần ảo: ',z1.imag)
'''

'''
# * kiểu dữ liệu List
lst=['a','b','c','d','e']
print(len(lst))
lst[3]=100
print(lst)
'''

'''
# * kiểu dictionary
dictEV={
    "Hello":'Xin Chào',
    "name":'tên một người',
    "Banana":'quả chuối',
}

print(dictEV['name'])
print(dictEV.keys()) #! Lấy ra list chứa các key
print(dictEV.values())
print(dictEV.items())
dictEV.clear()
print(dictEV)
'''

'''
#* kiểu set
setMHS={'HS01','HS02','HS03','HS01'}
print(setMHS)
setMHS.add('sada')
print(setMHS)
setMHS2={'HS01','HS09'}
setMHS.update(setMHS2)
print(setMHS)
'''

a=bool(input())
print(a)