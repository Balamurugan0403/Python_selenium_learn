import openpyxl
import os

def get_Excel_Data(sheet_name):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(base_dir, "..", "DataProviders", "loginTN.xlsx")
    
    Workbook = openpyxl.load_workbook(path)
    Sheet = Workbook[sheet_name]
    
    rows = []
    for row in Sheet.iter_rows(min_row=2, values_only=True):
        rows.append(row)
    return rows
