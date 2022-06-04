from connect import db, cur

# -- INSERT CabangBank
cur.execute("INSERT INTO CabangBank VALUES ('NGW', 'Ngawi', 'Ngawi Jawa Timur')")

# -- INSERT Nasabah
cur.execute("INSERT INTO Nasabah VALUES ('NGW01', 'Esa Age', 'Kec. Kedunggalar')")

# -- INSERT Rekening
cur.execute("INSERT INTO Rekening VALUES ('77572192', '920910', 'NGW01', 'NGW', 5000000000)")

# -- INSERT Transaksi
cur.execute("INSERT INTO Transaksi VALUES ('trx01' , 'INCO', 'NGW01', date('now'), 7000000)")


# commit database
db.commit()