import os
import openpyxl


def get_test_data(file_name, sheet_name):

    base_path = os.path.dirname(os.path.dirname(__file__))
    file_path = os.path.join(base_path, file_name)

    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook[sheet_name]

    data = []

    for row in sheet.iter_rows(min_row=2, values_only=True):

        if not any(row):
            continue

        data.append({
            "email": row[0],
            "password": row[1],
            "expected": row[2]
        })

    return data