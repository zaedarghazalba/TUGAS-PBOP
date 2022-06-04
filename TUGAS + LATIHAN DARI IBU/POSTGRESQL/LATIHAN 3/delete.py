from connect import db, cursor

# dosen
cursor.execute("DELETE FROM `dosen`")

# kuliah
cursor.execute("DELETE FROM `kuliah`")

# mata_kuliah
cursor.execute("DELETE FROM `mata_kuliah`")

db.commit()