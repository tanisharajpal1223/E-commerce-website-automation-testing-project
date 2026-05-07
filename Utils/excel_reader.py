import openpyxl
import os

def get_test_data(file_name, sheet_name):

    base_path = os.path.dirname(os.path.dirname(__file__))
    file_path = os.path.join(base_path, file_name)

    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook[sheet_name]

    data = []

    for row in sheet.iter_rows(min_row=2, values_only=True):

        # ✅ skip completely empty rows
        if not any(row):
            continue

        data.append({
            "first_name": row[0],
            "last_name": row[1],
            "email": row[2],
            "password": row[3],
            "telephone": row[4],
            "expected": row[5]
        })

    return data