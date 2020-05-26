class Xe():
    def __init__(self,mauSacXe='Không màu',dongXe='Không Hãng',bienSoXe='Chưa biển số'):
        print('Đã tạo ra một xe.')
        self.mauSacXe=mauSacXe
        self.dongXe=dongXe
        self.bienSoXe=bienSoXe

    def LayThongTinXe(self):
        print('Xe có màu: ',self.mauSacXe)
        print('Dòng xe: ',self.dongXe)
        print('Biển số xe: ',self.bienSoXe)


xe1=Xe('Đỏ','BMW','58658')
xe1.LayThongTinXe()

xe2=Xe()
xe2.LayThongTinXe()

