import openpyxl as excel
book =excel.Workbook()
sheet =book.active

#連続でセルに値を設定
for i in range(10):
 sheet.cell(row=(i+1), column=1, value=i)

book.save("renzoku.xlsx")
    
