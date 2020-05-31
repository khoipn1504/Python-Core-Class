from abc import ABC, abstractmethod


class DaGiac(ABC):

    def __init__(self, so_canh=0, ten_da_giac=''):
        self._ten_da_giac = ten_da_giac
        self._so_canh = so_canh

    @abstractmethod
    def tinhDienTich(self):
        pass


class TamGiac(DaGiac):

    def __init__(self):
        super().__init__(so_canh=3, ten_da_giac='tam giác')

    def tinhDienTich(self):
        print('Chu vi tam giác')

    def tinhTheTich(self):
        print('WTF')

tg = TamGiac()
tg.tinhDienTich()
tg.tinhTheTich()
