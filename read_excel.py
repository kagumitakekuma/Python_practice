import openpyxl as excel
book =excel.load_workbook("hello.xlsx")

#先頭のワークシートを取り出す
sheet =book.worksheets[0]
cell =sheet["A1"]
print(cell.value)
