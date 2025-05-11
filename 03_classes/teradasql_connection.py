import terdatasql
import pandas as pd


class TeradataConnection:
    def __init__(self, host, username, password, database):
        self.host = host
        self.username = username
        self.password = password
        self.database = database
        return None

    def connect(self):
        try:
            self.conn = teradata.connect(
                host=self.host,
                user=self.username,
                password=self.password,
                database=self.database,
            )
            print("Connection successful")
        except Exception as e:
            print("Error connecting to Teradata: ", e)

    def execute_query(self, query):
        try:
            self.cursor = self.conn.cursor()
            self.cursor.execute(query)
            self.result = self.cursor.fetchall()
        except Exception as e:
            print("Error executing query: ", e)
            return None


def main():
    host = ""
    username = ""
    password = ""
    database = ""

    teradata = TeradataConnection(host, username, password, database)
    teradata.connect()

    query = "SELECT DATABASE;"
    results = teradata.execute_query(query)

    if results:
        print("Query Results:")
        for row in results:
            print(row)

    # Close the connection
    teradata.close_connection()


if __name__ == "__main__":
    main()
