import mariadb
import sys

def connect_to_db():
    try:
        conn = mariadb.connect(
            user="gymbuddy",
            password="1234",
            host="localhost",
            port=3306,
            database="gymbuddyDB"
        )
        return conn
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        sys.exit(1)
