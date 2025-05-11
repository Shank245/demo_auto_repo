import teradatasql
import gzip
import csv

# Define Teradata connection parameters
host = "your_teradata_host"  # Replace with your Teradata server hostname or IP
username = "your_username"  # Replace with your username
password = "your_password"  # Replace with your password

# Define the SQL query to fetch data
query = """
SELECT department_id, AVG(salary) AS avg_salary
FROM employee
GROUP BY department_id
ORDER BY department_id;
"""

# Path to the .dat.gz file
dat_file_path = "path_to_your_file.dat.gz"  # Replace with the actual file path

# Function to read data from .dat.gz file
def read_dat_file(file_path):
    data = []
    with gzip.open(file_path, mode="rt") as file:  # Open the .dat.gz file in text mode
        reader = csv.reader(file, delimiter="|")  # Assuming '|' is the delimiter
        for row in reader:
            data.append(row)
    return data

# Function to fetch data from Teradata
def fetch_teradata_data():
    try:
        with teradatasql.connect(
            host=host,
            user=username,
            password=password
        ) as connection:
            print("Connected to Teradata!")
            with connection.cursor() as cursor:
                cursor.execute(query)
                return cursor.fetchall()
    except Exception as e:
        print(f"Error connecting to Teradata: {e}")
        return []

# Main validation logic
def validate_data():
    # Fetch data from Teradata
    teradata_data = fetch_teradata_data()

    # Read data from .dat.gz file
    file_data = read_dat_file(dat_file_path)

    # Compare the two datasets
    mismatches = []
    for teradata_row, file_row in zip(teradata_data, file_data):
        if list(map(str, teradata_row)) != file_row:  # Convert Teradata row to string for comparison
            mismatches.append((teradata_row, file_row))

    # Print validation results
    if mismatches:
        print("Data mismatches found:")
        for teradata_row, file_row in mismatches:
            print(f"Teradata: {teradata_row}, File: {file_row}")
    else:
        print("Data validation successful! No mismatches found.")

# Run the validation
validate_data()