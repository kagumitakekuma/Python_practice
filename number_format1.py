import openpyxl as xl

book =xl.Workbook()
sheet =book.active

val =3.14159
sheet.append([val, val, val])

sheet["A1"].number_format ="0"

sheet["B2"].number_format ="0.00"
sheet["C2"].number_format ="0.0000"

book.save =("number_format1.xlsx")

