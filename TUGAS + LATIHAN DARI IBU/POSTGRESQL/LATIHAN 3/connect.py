import psycopg2

db = psycopg2.connect(
    host="localhost",
    database="pbop-crud-postgre",
    user="esaage",
    password="root")

cur = db.cursor()