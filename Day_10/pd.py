import pandas as pd


# data = pd.read_excel(r'Day_10/Test.xlsx')
# df = pd.DataFrame(data, columns=['ID','Name'])
# print(df)


df1 = pd.DataFrame({'Data': [11, 12, 13, 14],'Name':[1,2,3,4]})
df2 = pd.DataFrame({'Data': [21, 22, 23, 24]})
df3 = pd.DataFrame({'Data': [31, 32, 33, 34]})
df4 = pd.DataFrame({'Data': [41, 42, 43, 44]})

writer = pd.ExcelWriter(r'Day_10/Test.xlsx', engine='xlsxwriter')

df1.to_excel(writer, sheet_name='Sheet1')  # Default position, cell A1.
df2.to_excel(writer, sheet_name='Sheet1', startcol=3)
df3.to_excel(writer, sheet_name='Sheet1', startrow=6)


df4.to_excel(writer, sheet_name='Sheet1',
             startrow=7, startcol=4, header=False, index=False)

writer.save()

data = pd.read_excel(r'Day_10/Test.xlsx')
# df = pd.DataFrame(data, columns=['ID','Name'])
print(data)
