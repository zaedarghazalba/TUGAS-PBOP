from connect import db, cursor

# dosen
cursor.execute("SELECT * FROM `dosen`")
for row in cursor.fetchall():
    print("%s, %s, %s, %s, %s, %s, %s, %s" %
          (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])) 

# kuliah
cursor.execute("SELECT * FROM `kuliah`")
for row in cursor.fetchall():
    print("%s, %s, %s, %s, %s, %s, %s" %
          (row[0], row[1], row[2], row[3], row[4], row[5], row[6]))

# mata_kuliah
cursor.execute("SELECT * FROM `mata_kuliah`")
for row in cursor.fetchall():
    print("%s, %s, %s, %s" %
          (row[0], row[1], row[2], row[3]))

db.commit()