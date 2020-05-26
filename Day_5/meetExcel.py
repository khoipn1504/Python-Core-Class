import xlsxwriter

excWorkSpace=xlsxwriter.Workbook('Hello_bitch.xlsx')
excSheet=excWorkSpace.add_worksheet()

excSheet.write('A1','Hello')

excWorkSpace.close()