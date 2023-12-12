import mysql.connector
import json


# Function to initialize the database
def initialize_database(app):
    try:
        # Create a connection without specifying the database
        conn = mysql.connector.connect(
            host=app.config["MYSQL_HOST"],
            user=app.config["MYSQL_USER"],
            password=app.config["MYSQL_PASSWORD"],
        )
        
        # Create a cursor to execute SQL commands
        cursor = conn.cursor()

        # Create the database if it doesn't exist
        cursor.execute(
            f"CREATE DATABASE IF NOT EXISTS {app.config['MYSQL_DB']};"
        )

        # Switch to the database
        cursor.execute(f"USE {app.config['MYSQL_DB']};")

        # Drop the table if it exists
        cursor.execute("DROP TABLE IF EXISTS jobs;")

        # Create a new table
        cursor.execute(
            """
            CREATE TABLE jobs (
                id INT AUTO_INCREMENT PRIMARY KEY,
                title VARCHAR(255),
                location VARCHAR(255),
                salary VARCHAR(255)
            );
        """
        )

        # Read data from jobs.json
        with open(app.config["DATA_FILE_NAME"]) as json_file:
            jobs_data = json.load(json_file)

        # Insert data into the table
        for job in jobs_data:
            cursor.execute(
                """
                INSERT INTO jobs (title, location, salary)
                VALUES (%s, %s, %s)
            """,
                (job["title"], job["location"], job.get("salary", "")),
            )

        # Commit the changes and close the connection
        conn.commit()
        conn.close()

        print("Database initialized successfully.")

    except mysql.connector.Error as e:
        print(f"Error initializing database: {e}")


def get_mysql_connection(app):
    return mysql.connector.connect(
        host=app.config["MYSQL_HOST"],
        user=app.config["MYSQL_USER"],
        password=app.config["MYSQL_PASSWORD"],
        database=app.config["MYSQL_DB"],
    )
