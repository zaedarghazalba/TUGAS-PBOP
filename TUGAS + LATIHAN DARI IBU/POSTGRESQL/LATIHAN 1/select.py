from connect import db, cursor

# gaji
cursor.execute("SELECT * FROM `gaji`")
for row in cursor.fetchall():
    print("%s, %s, %s, %s, %s, %s, %s, %s" %
          (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])) 

# golongan
cursor.execute("SELECT * FROM `golongan`")
for row in cursor.fetchall():
    print("%s, %s, %s, %s, %s, %s, %s" %
          (row[0], row[1], row[2], row[3], row[4], row[5], row[6]))

# jabatan
cursor.execute("SELECT * FROM `jabatan`")
for row in cursor.fetchall():
    print("%s, %s, %s, %s" %
          (row[0], row[1], row[2], row[3]))

# pegawai
cursor.execute("SELECT * FROM `pegawai`")
for row in cursor.fetchall():
    print("%s, %s, %s, %s, %s, %s" %
          (row[0], row[1], row[2], row[3], row[4], row[5]))


db.commit()