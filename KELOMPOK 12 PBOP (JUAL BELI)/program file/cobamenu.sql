-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Waktu pembuatan: 11 Bulan Mei 2022 pada 03.22
-- Versi server: 10.4.22-MariaDB
-- Versi PHP: 8.1.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `cobamenu`
--

-- --------------------------------------------------------

--
-- Struktur dari tabel `data_makanan`
--

CREATE TABLE `data_makanan` (
  `ID` int(11) NOT NULL,
  `menu_makanan` varchar(100) NOT NULL,
  `harga` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `data_makanan`
--

INSERT INTO `data_makanan` (`ID`, `menu_makanan`, `harga`) VALUES
(1, 'Nasi goreng', 12000),
(2, 'Mie Kuah', 8000),
(3, 'Soto Ayam', 14000),
(4, 'Ayam Geprek', 12000),
(5, 'Rawon ', 13000),
(6, 'Pecel Lele', 11000),
(7, 'Ayam Bakar Madu', 14000),
(8, 'Ayam Penyet', 13000),
(9, 'Ayam Crispy', 12000),
(11, 'Es Teh', 2000),
(12, 'Teh Panas', 2000),
(13, 'Es Jeruk', 2000),
(14, 'Jeruk Panas', 2000),
(15, 'Es Sirup', 2000),
(16, 'Kopi', 2000),
(17, 'Bebek Goreng', 13000);

--
-- Indexes for dumped tables
--

--
-- Indeks untuk tabel `data_makanan`
--
ALTER TABLE `data_makanan`
  ADD PRIMARY KEY (`ID`);

--
-- AUTO_INCREMENT untuk tabel yang dibuang
--

--
-- AUTO_INCREMENT untuk tabel `data_makanan`
--
ALTER TABLE `data_makanan`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
