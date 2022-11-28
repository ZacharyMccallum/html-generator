# Load xlsx workbook
import openpyxl

def readData():
    wb = openpyxl.load_workbook(r'./src/user_details.xlsx')
    print(type(wb))

readData()