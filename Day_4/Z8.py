from random import randint
class KhachHang():
    def __init__(self,maKH='',tenKH='',gioiTinh=''):
        self.maKH=maKH
        self.tenKH=tenKH
        self.gioiTinh=gioiTinh

        self.level=0
        self.isActive=False
    
    
    def __repr__(self):
        return str(self.level)

    def nhapInfo(self):
        self.maKH=input('Nhập vào mã KH: ')
        self.tenKH=input('Nhập vào tên KH: ')
        self.gioiTinh=input('Nhập vào gioi tinh: ')
    
    def layThongTin(self):
        print('MSKH là %s, ten KH là %s, giới tính là %s, level %s và đã kích hoạt: %s'%(self.maKH,self.tenKH,self.gioiTinh,self.level,self.isActive))

def SortKHByLv(khList):
    khGroup=khList.copy()
    if len(khGroup) <2:
        return khGroup
    pivot=khGroup.pop()
    lowLV=[]
    highLV=[]
    for kh in khGroup:
        if kh.level < pivot.level:
            lowLV.append(kh)
        else:
            highLV.append(kh)
    return SortKHByLv(lowLV)+[pivot]+SortKHByLv(highLV)

def themKh(khGroup):
    kh=KhachHang()
    kh.nhapInfo()
    kh.level=randint(1,10)
    khGroup.append(kh)

def xoaKH(khGroup,MSKH):
    

if __name__ == "__main__":
    khGroup=[]
    # sll=int(input('Số lượng khách hàng cần nhập: '))

    # for i in range(sll):
    #     kh=KhachHang()
    #     kh.nhapInfo()
    #     kh.level=randint(1,10)
    #     khGroup.append(kh)

    while True:
        userorder=input(r'Bạn muốn gì (add,delete,show):')
        if userorder=='quit':
            break
        if userorder=='add':
            themKh(khGroup)
        elif userorder=='show':
            for i in khGroup:
                i.layThongTin()
        elif userorder=='delete':



