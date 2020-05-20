def CheckSoNguyenTo(soNguyenTo):
    isNguyenTo = True
    for i in range(2, soNguyenTo):
        if soNguyenTo % i == 0:
            isNguyenTo = False
            break

    return isNguyenTo


lstNum = input('Nhập vào danh sách các số cần kiểm tra: ').strip().split(' ')
lstIsNguyeTo=[]

for i in lstNum:
    if CheckSoNguyenTo(int(i)):
        lstIsNguyeTo.append(i)

print('Đây là danh sách các số nguyên tố: ',end='')
for i in lstIsNguyeTo:
    print(i,end=' ')

