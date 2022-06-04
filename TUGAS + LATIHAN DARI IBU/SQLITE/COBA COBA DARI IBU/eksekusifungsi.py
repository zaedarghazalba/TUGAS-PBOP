#Membuat dan mengeksekusi fungsi 

#fungsi utama 
def touper (s):
        return s.upper()

#fungsi kedua
def tolower(s):
        return s.lower()

import sqlite3

conn=sqlite3.connect("mydbpbop")

#memasukkan fungsi ke dalam database 
conn.create_function("toupper",1,touper)
conn.create_function("tolower",1,tolower)

#menggunakan fungsi didalam sql
cur = conn.cursor()
