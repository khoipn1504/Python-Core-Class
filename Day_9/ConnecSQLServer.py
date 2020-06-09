import pyodbc

serverInfo = "DESKTOP-7PLBSPR\MSSQLSERVER01"
databaseName = "QUAN_LY_SAN_PHAM"
userId='khoipn'
userPass='123456789'

driver = '{SQL Server}'
# port = '1433'

connection = pyodbc.connect('DRIVER={SQL Server};SERVER=' +
                            serverInfo+';DATABASE='+databaseName+';UID='+userId+';PWD='+userPass)

cursor = connection.cursor()

# cursor.execute("SELECT * FROM SAN_PHAM WHERE MA_DANH_MUC='DM004'")

# for row in cursor.fetchall():
#     print(row.TEN_SAN_PHAM)
    

sql = "INSERT INTO SAN_PHAM VALUES(?,?,?,?)"
val = ('SP101', 'lăn nách','1000','DM003')
cursor.execute(sql, val)
connection.commit()
print("record inserted.")

# sql = "UPDATE SAN_PHAM SET TEN_SAN_PHAM=(%s) WHERE MA_SAN_PHAM='SP100'"
# val = ('diana')
# cursor.execute("UPDATE SAN_PHAM SET TEN_SAN_PHAM='{0}' WHERE MA_SAN_PHAM='SP100'".format("dilac"))
# connection.commit()


