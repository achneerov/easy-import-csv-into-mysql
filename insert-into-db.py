import pandas as pd
import mysql.connector

file_name = "Courses.csv"
table_name = "courses"

csv_file_path = f'place-csv-files-here/{file_name}'

# Connect to MySQL database
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='a1'
)

# Open and read the CSV file using pandas
df = pd.read_csv(csv_file_path)

# Get column names and data types from the CSV file
columns = list(df.columns)
data_types = [df[col].dtype for col in columns]

# Mapping pandas data types to MySQL data types
mysql_data_types = {
    'int64': 'INT',
    'float64': 'DOUBLE',
    'object': 'VARCHAR(255)'  # Adjust the length based on your requirements
}

# Convert pandas data types to MySQL data types
mysql_column_types = [mysql_data_types[str(dtype)] for dtype in data_types]

# Create a table in the database if not exists
cursor = conn.cursor()

# Using f-strings for SQL queries
create_table_query = f'''
    CREATE TABLE IF NOT EXISTS {table_name} (
        {', '.join([f'{col} {dtype}' for col, dtype in zip(columns, mysql_column_types)])}
    )
'''
cursor.execute(create_table_query)

# Insert data into the database
for index, row in df.iterrows():
    insert_query = f'''
        INSERT INTO {table_name} ({', '.join(columns)})
        VALUES ({', '.join(['%s'] * len(columns))})
    '''
    cursor.execute(insert_query, tuple(row))

# Commit the changes and close the connection
conn.commit()
conn.close()
