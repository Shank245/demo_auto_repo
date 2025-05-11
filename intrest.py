def simple_intrest(p, n, r):
    i = (p * r * n) / 100
    a = p + i
    return i, a


p = eval(input("Enter the principal amount: "))
n = eval(input("Enter the rate of interest: "))
r = eval(input("Enter the time in years: "))
i, a = simple_intrest(p, n, r)
print("The simple interest is: ", i)


import teradatasql

# Define connection parameters
host = "your_teradata_host"  # Replace with your Teradata server hostname or IP
username = "your_username"  # Replace with your username
password = "your_password"  # Replace with your password

# Establish connection
try:
    with teradatasql.connect(host=host, user=username, password=password) as connection:
        print("Connection successful!")

        # Create a cursor to execute queries
        with connection.cursor() as cursor:
            # Example query
            query = """
            SELECT department_id, AVG(salary) AS avg_salary
            FROM employee
            GROUP BY department_id
            ORDER BY avg_salary DESC
            LIMIT 1;
            """
            cursor.execute(query)

            # Fetch and print results
            for row in cursor.fetchall():
                print(row)

except Exception as e:
    print(f"Error: {e}")
