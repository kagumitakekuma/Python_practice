import openpyxl as excel

book =excel.Workbook()
sheet =book.active

for y in range(1,10):
 for x in range(1,10):
  cell =sheet.cell(row=y, column=x)
  cell.value= x*y

book.save("99.xlsx")
