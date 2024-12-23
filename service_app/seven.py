import pyodbc
from setting_app.models import SevenConfig


def get_reception_info(job_number):
    config = SevenConfig.objects.last()
    server = config.server
    database = 'AsSevenSamsung'
    username = config.username
    password = config.password
    
    # Create a connection string
    connection_string = (
        f'DRIVER={{ODBC Driver 17 for SQL Server}};'
        f'SERVER={server};'
        f'DATABASE={database};'
        f'UID={username};'
        f'PWD={password}'
    )

    # Establish connection
    connection = pyodbc.connect(connection_string)

    print("Connection established successfully")

    # Create a cursor from the connection
    cursor = connection.cursor()

    # Define your SQL query (change table name as needed)
    query = f"SELECT * FROM vicReception WHERE LocalReceptionCode = '{job_number}'"

    # Execute the query
    x = cursor.execute(query)
    print("Query executed successfully")
    print(x)

    rows = cursor.fetchall()

    for row in rows:
        print(row)
        print("-" * 50)
