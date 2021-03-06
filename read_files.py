import glob

import openpyxl as xl
target_dir="./salesbooks"
save_file ="matome.xlsx"

def read_files():
    book =xl.Workbook()
    main_sheet =book.active
    enumfiles(main_sheet)
    book.save(save_files)

def enumfiles(main_sheet):
    files =glob.glob(target_dir + "/*.xlsx")
    for fname in files:
        read_book(main_sheet, fname)


def read_book(main_sheet, fname):
    print("read:", fname)
    book =xl.load_workbook(fname, data_only=True)
    sheet =book.active
    rows =sheet["A4":"F999"]
    for row in rows:
        values =[cell.value for cell in row]
        if values[0] is None: break
        print(values)
        main_sheet.append(values)

if __name__ =="__main__":
    read_files()
