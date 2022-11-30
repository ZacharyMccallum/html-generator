# Load xlsx workbook
import pandas as pd

def readData():
    # Create workbook var for import spreadsheet
    df_students = pd.read_excel(r'./src/user_details.xlsx', "Sheet1")
    data = {k: f.groupby('last_name')['date_of_birth'].apply(list).to_dict()
    for k, f in df_students.groupby('first_name')}
    return data