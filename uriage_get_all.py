import openpyxl as excel

book =excel.load_workbook("uriage.xlsx")
sheet =book.active

rows =sheet["A3:F11"]
for row in rows:
    values =[cell.value for cell in row]
    print(values)

    
            
