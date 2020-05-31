class NhanVien():
    __ten_nv = ''  # __variable là khởi tạo private. Bên ngoài class không thể gọi trực tiếp mà phải thông qua hàm
    __tuoi = 0

    def setTenNV(self, name):
        self.__ten_nv = name+'asdsa'

    def getTenNV(self):
        return self.__ten_nv
