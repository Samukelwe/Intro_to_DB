"""
import mysql.connector

# Replace with your connection details
mydb = mysql.connector.connect(
    host="localhost",
    user="samu",
    password="samukelwe",
    database="yourdatabase"
)

print(mydb.get_server_info())
""" 

import mysql.connector

# Replace with your connection details
mydb = mysql.connector.connect(
    host="localhost",
    user="samu",
    password="samukelwe",
    database="1stdatabase"
)

mycursor = mydb.cursor()
# Execute SQL statements using the execute() method on the cursor

CREATE TABLE Employees (
    employee_id INT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    department VARCHAR(50),
    hire_date DATE
);
# Close connection to the databasse  
mycursor.close()
mydb.close()