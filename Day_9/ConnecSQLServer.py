import pyodbc

serverInfo = "DESKTOP-7PLBSPR\MSSQLSERVER01"
databaseName = "QUAN_LY_SAN_PHAM"
userId = 'khoipn'
userPass = '123456789'

driver = '{SQL Server}'
# port = '1433'

connection = pyodbc.connect('DRIVER={SQL Server};SERVER=' +
                            serverInfo+';DATABASE='+databaseName+';UID='+userId+';PWD='+userPass)

cursor = connection.cursor()


def AddProduct(id, name, sll, cata):
    sql = "INSERT INTO SAN_PHAM VALUES(?,?,?,?)"
    val = (id, name, sll, cata)
    cursor.execute(sql, val)
    connection.commit()
    print("record inserted.")


def ShowProduct():
    cursor.execute("SELECT * FROM SAN_PHAM")
    for row in cursor.fetchall():
        print(row.MA_SAN_PHAM.ljust(10), str(row.TEN_SAN_PHAM).strip().ljust(30),
              str(row.SL_TON_KHO).ljust(10), row.MA_DANH_MUC.ljust(10), sep="|")

    # sql = "UPDATE SAN_PHAM SET TEN_SAN_PHAM=(%s) WHERE MA_SAN_PHAM='SP100'"
    # val = ('diana')
    # cursor.execute("UPDATE SAN_PHAM SET TEN_SAN_PHAM='{0}' WHERE MA_SAN_PHAM='SP100'".format("dilac"))
    # connection.commit()


while True:
    user = int(input(
        'Nhập 0 để exit. Nhập 1 để thêm sản phẩm. Nhập 2 để xem danh sách sản phẩm: '))
    if user == 0:
        break
    elif user == 1:
        product_id = input("Nhap vao id san pham: ")
        product_name = input("Nhap vao ten san pham: ")
        product_sll = input("Nhap vao so luong san pham: ")
        product_cata = input("Nhap vao danh muc san pham: ")
        AddProduct(product_id, product_name, product_sll, product_cata)
    elif user == 2:
        ShowProduct()
