#pip install sqlalchemy
#pip install pandas
#pip install openpyxl
#pip install pymysql
#pip install cryptography
#CREATE DATABASE demo_db;

#USE demo_db;
#SELECT * FROM warehouse_table LIMIT 10;


import pandas as pd
from sqlalchemy import create_engine

# MySQL database credentials
db_user = 'root'
db_password = 'root'  # Replace with your MySQL root password
db_host = 'localhost'
db_name = 'demo_db'

# File paths to the data sources
csv_file_path = 'c:\demo\demo.csv'  # Replace with the actual path to your CSV file
excel_file_path = 'c:\demo\demo.xlsx'  # Replace with the actual path to your Excel file

# Read data from CSV
df_csv = pd.read_csv(csv_file_path)

# Read data from Excel
df_excel = pd.read_excel(excel_file_path, sheet_name='Sheet1')  # Change sheet_name if necessary

# Example transformation: rename columns
df_csv.rename(columns={'old_column_name_csv': 'new_column_name'}, inplace=True)
df_excel.rename(columns={'old_column_name_excel': 'new_column_name'}, inplace=True)

# Combine data (if needed)
df_combined = pd.concat([df_csv, df_excel])

# Create a SQLAlchemy engine
engine = create_engine(f'mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_name}')

# Load data into MySQL
df_combined.to_sql('warehouse_table', con=engine, if_exists='replace', index=False)

print('Data imported successfully')
