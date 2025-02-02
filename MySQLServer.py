import mysql.connector

try:
    mydb = mysql.connector.connect(
        host="host",
        user="user",
        password="password",
        auth_plugin="mysql_native_password",
    )
    mycursor = mydb.cursor()
    sql = "CREATE DATABASE IF NOT EXISTS alx_book_store"
    mycursor.execute(sql)
    print("Database 'alx_book_store' created successfully!")

except mysql.connector.Error as e:
    print(e)