import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "kuliah-pbop-crud-mysql"
)
cursor = db.cursor()