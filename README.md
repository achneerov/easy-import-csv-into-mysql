# MySQL Table Creator from CSV using Python and Pandas

This Python script allows you to create a MySQL table from a CSV file using the Pandas library. It automatically analyzes the CSV file, determines the data types of each column, and creates a corresponding MySQL table with the appropriate schema. Additionally, it inserts the data from the CSV file into the newly created table.

## Prerequisites

Before using this script, ensure you have the following installed:

- Python (3.x recommended)
- Pandas library (`pip3 install pandas`)
- MySQL Connector (`pip3 install mysql-connector-python`)

## Getting Started

1. **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/your-repository.git
    ```

2. **Navigate to the project directory:**

    ```bash
    cd your-repository
    ```

3. **Place your CSV file in the `place-csv-files-here` directory.**

4. **Configure the MySQL connection details in the script:**

    ```python
    host='localhost',
    user='your-username',
    password='your-password',
    database='your-database'
    ```

5. **Run the script:**

    ```bash
    python create_mysql_table_from_csv.py
    ```

## Configuration

Modify the following variables in the script according to your needs:

- `file_name`: The name of your CSV file.
- `table_name`: The desired name for your MySQL table.
- MySQL connection details (host, user, password, database).

## Note

- The script assumes a local MySQL server. Adjust the `host` variable if your database is hosted elsewhere.
- The data types in MySQL are mapped from Pandas data types. You may need to adjust the mapping based on your specific requirements.

Feel free to contribute or report issues. Happy coding!

