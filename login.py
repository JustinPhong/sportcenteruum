import mysql.connector

def connect_to_database():
    # Modify the following parameters with your MySQL server details
    config = {
        'user': 'id21699656_admin',
        'password': 'Abc12345@',
        'host': 'localhost',
        'database': 'login',
        'raise_on_warnings': True
    }

    try:
        # Establish a connection to the MySQL server
        connection = mysql.connector.connect(**config)
        print("Connected to the database")
        return connection

    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

def authenticate_user(username, password, connection):
    try:
        # Create a cursor object to interact with the database
        cursor = connection.cursor()

        # Execute a query to fetch the user details
        query = "SELECT * FROM users WHERE username = %s AND password = %s"
        cursor.execute(query, (username, password))

        # Fetch the result
        result = cursor.fetchone()

        if result:
            print('<meta http-equiv="refresh" content="0;url=https://sportcenteruum.000webhostapp.com/home.html">')
        else:
            print("Invalid username or password")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        # Close the cursor and connection
        cursor.close()

if __name__ == "__main__":
    # Connect to the database
    connection = connect_to_database()

    if connection:
        # Example login
        authenticate_user("example_user", "example_password", connection)

        # Close the database connection
        connection.close()
