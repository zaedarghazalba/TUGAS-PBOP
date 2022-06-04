import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "kuliah-pbop-crud-mysql"
)
cur = db.cursor()

# table cabang bank
cur.execute('''CREATE TABLE IF NOT EXISTS CabangBank (
	kodeCabang VARCHAR(3) PRIMARY KEY,
	namaCabang VARCHAR(60),
	alamatCabang VARCHAR(120));''')

# table nasabah
cur.execute('''CREATE TABLE IF NOT EXISTS Nasabah ( 
	idNasabah VARCHAR(5) PRIMARY KEY,
	namaNasabah VARCHAR(60),
	alamatNasabah VARCHAR(120));''')

# table rekening
cur.execute('''CREATE TABLE IF NOT EXISTS Rekening (
	noRekening VARCHAR(9) PRIMARY KEY,
	pin VARCHAR(6),
	idNasabah VARCHAR(5),
	kodeCabang VARCHAR(3),
	saldo INTEGER,
	FOREIGN KEY(idNasabah) REFERENCES Nasabah(idNasabah),
	FOREIGN KEY(kodeCabang) REFERENCES CabangBank(kodeCabang));''')

# table transaksi
cur.execute('''CREATE TABLE IF NOT EXISTS Transaksi (
	noTransaksi VARCHAR(5) PRIMARY KEY,
	jenisNasabah VARCHAR(10),
	idNasabah VARCHAR(5),
	tanggal DATE,
	jumlah INTEGER,
	FOREIGN KEY(idNasabah) REFERENCES Nasabah(idNasabah));''')