def SelectionSort(lstNum):
    for i in range(len(lstNum)):
        for x in range(i, len(lstNum)):
            if lstNum[x] < lstNum[i]:
                lstNum[x], lstNum[i] = lstNum[i], lstNum[x]  # swap value



def QuickSort(lstInput):
    lstNum=lstInput.copy()
    if len(lstNum) < 2:
        return lstNum

    pivot = lstNum.pop()
    lstLow = []
    lstHigh = []
    for num in lstNum:
        if num < pivot:
            lstLow.append(num)
        else:
            lstHigh.append(num)

    return QuickSort(lstLow)+[pivot]+QuickSort(lstHigh)


lstNum = input('Nhập vào danh sách các số cần sắp xêp: ').strip().split(' ')
lstNum = [int(i) for i in lstNum]
a=QuickSort(lstNum)
print(a)
print(lstNum)
