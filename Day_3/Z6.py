def SelectionSort(lstNum):
    for i in range(len(lstNum)):
        for x in range(i, len(lstNum)):
            if lstNum[x] < lstNum[i]:
                lstNum[x], lstNum[i] = lstNum[i], lstNum[x] #swap value


# def QuickSort(lstNum):


lstNum = input('Nhập vào danh sách các số cần sắp xêp: ').strip().split(' ')
lstNum = [int(i) for i in lstNum]

SelectionSort(lstNum)

print(lstNum)
