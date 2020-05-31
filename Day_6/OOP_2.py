class DongVat():

    def __init__(self, ten='không biết', so_chan='không biết', mau_long='không biết'):
        self._mau_long = mau_long
        self._so_chan = so_chan
        self._ten = ten

    def DiKiemAn(self):
        print('Đi kiếm ăn!')


class ConHeo(DongVat):

    def __init__(self, can_nang=0):
        super().__init__(self, so_chan=4)
        self._can_nang = can_nang

    def DiNgu(self):
        print('Đi ngủ!!!')


heo = ConHeo(100)

print(heo._can_nang)
