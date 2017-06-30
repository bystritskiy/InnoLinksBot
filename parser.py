import sqlite3
import xlrd
import os
import config


def create_database():
    if os.path.isfile(config.db_path):
        os.remove(config.db_path)
    conn = sqlite3.connect(config.db_path)
    cursor = conn.cursor()
    cursor.execute(config.create_db_command)
    print("Table created successfully...")
    conn.commit()
    cursor.close()
    conn.close()


def import_data():
    conn = sqlite3.connect(config.db_path)
    cursor = conn.cursor()
    excel_data_file = xlrd.open_workbook(config.companies_path)
    sheet = excel_data_file.sheet_by_index(0)
    row_number = sheet.nrows

    if row_number > 0:
        for row in range(1, row_number):
            name, category, subcategory, desc, address, phone, schedule, links = \
                [str(line).replace("text:", "").replace("number:", "").replace("empty:", "").replace('\\n'," ")
                 for line in sheet.row(row)]
            cursor.execute(f"INSERT INTO COMPANY (id,name,category,subcategory,description,address,phone,schedule,links) \
                VALUES ({row}, {name}, {category}, {subcategory}, {desc}, {address}, {phone}, {schedule}, {links})")
    conn.commit()
    cursor.close()
    conn.close()
    print("Information imported")


create_database()
import_data()