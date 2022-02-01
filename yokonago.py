import openpyxl as excel

book =excel.load_workbook("all-customer.xlsx")

sheet =book["名簿"]
customers =[["名前","住所","購入プラン"]]

for row in sheet.iter_rows(min_row=3):
    values =[v.value for v in row]
    if values [0] is None: break
    area =="横浜市" or area =="名古屋市":
        customers.append(values)
        print(values)

        
