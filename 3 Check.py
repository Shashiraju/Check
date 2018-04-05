import openpyxl as xl
wb = xl.load_workbook("C:\\Shashiraju Learning Projects\\Python\\Programs\\check.xlsx")
ws=  wb.active
print(ws)
