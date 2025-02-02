import mysql.connector

# Replace with your connection details
mydb = mysql.connector.connect(
    host="localhost",
    user="samu",
    password="samukelwe",
    database="alx_be"
)

print(mydb.get_server_info())