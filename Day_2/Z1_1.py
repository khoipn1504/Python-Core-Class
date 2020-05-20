while True:
    soNguyenTo = int(input('Hãy nhập vào số nguyên tố: '))
    isNguyenTo = True

    if soNguyenTo == '':
        break

    for i in range(2, soNguyenTo):
        if soNguyenTo % i == 0:
            print(soNguyenTo,' không phải số nguyên tố')
            isNguyenTo = False
            break

    if isNguyenTo:
        print(soNguyenTo,' là số nguyên tố')
