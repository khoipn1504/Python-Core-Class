
def BCNN(a, b):
    small, big = 0, 0

    if a == b:
        return a
    elif b > a:
        small = a
        big = b
    else:
        small = b
        big = a

    for i in range(big, (big*small)+1):
        if i % small == 0 and i % big == 0:
            return i


def CheckSoNguyenTo(soNguyenTo):
    # theo nghiên cứu thì chỉ cần check tới đây là được
    limitCheck = int(soNguyenTo**0.5) + 1

    for i in range(2, limitCheck):
        if soNguyenTo % i == 0:
            return False
    return True


def TachTichThuaSo(x):
    dictThuaSo = {}
    soChia = 2
    flag = True
    while flag:
        if x % soChia == 0:
            if soChia not in dictThuaSo.keys():
                dictThuaSo[soChia] = 0
            dictThuaSo[soChia] += 1
            x = int(x/soChia)
            # print(x)
        else:
            if CheckSoNguyenTo(x):
                if x != soChia and x != 1:
                    dictThuaSo[x] = 1
                flag = False
            soChia += 1

    return dictThuaSo


def mergeDict(dict1, dict2):
    # Gộp dict lại nhưng vẫn giữ nguyên value của các key trùng nhau thành 1 list
    dict3 = {**dict1, **dict2}  # unpack dict
    '''
    có thể ghi ra là:
    dict3=dict1.copy()
    dict3.update(dict2)
    '''
    for key, value in dict3.items():
        if key in dict1 and key in dict2:
            dict3[key] = [value, dict1[key]]

    return dict3


def BCNNPlus(a, b):
    if a == b:
        return a
    else:
        ans = 1
        dictA = TachTichThuaSo(a)
        dictB = TachTichThuaSo(b)
        # print(dictA, dictB)
        mergeAB = mergeDict(dictA, dictB)
        # print(mergeAB)
        for key, value in mergeAB.items():
            try:
                ans *= key**max(value)
            except Exception:
                ans *= key**value

        return ans


def UCLNPlus(a, b):
    if a == b:
        return a
    else:
        ans = 1
        dictA = TachTichThuaSo(a)
        dictB = TachTichThuaSo(b)
        mergeAB = mergeDict(dictA, dictB)
        for key, value in mergeAB.items():
            try:
                ans *= key**min(value)
            except Exception:
                pass

        return ans


'''
Chương trình bắt đâu từ đây
'''
while True:
    userInput = input('Nhập vào 2 số cần xác định UCLN và BCNN: ')

    if userInput == '':
        print('Kết thúc chương trình')
        break

    lstNum = userInput.strip().split(' ')
    lstNum = [int(i) for i in lstNum]

    print('BCNN của %s và %s là: ' %
          (lstNum[0], lstNum[1]), BCNNPlus(lstNum[0], lstNum[1]))

    print('UCLN của %s và %s là: ' %
          (lstNum[0], lstNum[1]), UCLNPlus(lstNum[0], lstNum[1]))
