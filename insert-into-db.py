import pandas as pd
import mysql.connector

# Connect to MySQL database
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='a1'
)

# Create a table in the database if not exists
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS enrolments (
        SIN INT,
        CID INT,
        Semester VARCHAR(255),
        Year INT,
        Grade VARCHAR(255)
    )
''')

# Open and read the CSV file using pandas
csv_file_path = 'Enrollments.csv'
df = pd.read_csv(csv_file_path)

# Insert data into the database
for index, row in df.iterrows():
    cursor.execute('''
        INSERT INTO enrolments (SIN, CID, Semester, Year, Grade)
        VALUES (%s, %s, %s, %s, %s)
    ''', (row['SIN'], row['CID'], row['Semester'], row['Year'], row['Grade']))

# Commit the changes and close the connection
conn.commit()
conn.close()
