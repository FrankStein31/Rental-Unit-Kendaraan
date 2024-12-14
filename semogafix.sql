/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

CREATE TABLE `elf` (
  `id_elf` int NOT NULL,
  `jenis_elf` varchar(255) DEFAULT NULL,
  `type_elf` varchar(255) DEFAULT NULL,
  `tahun_elf` int DEFAULT NULL,
  `warna_elf` varchar(255) DEFAULT NULL,
  `stok_elf` int DEFAULT NULL,
  `harga_sewa_elf` int DEFAULT NULL,
  `driver` enum('ya','tidak') NOT NULL DEFAULT 'tidak',
  PRIMARY KEY (`id_elf`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `mobil` (
  `id_mbl` int NOT NULL,
  `jenis_mbl` varchar(255) DEFAULT NULL,
  `type_mbl` varchar(255) DEFAULT NULL,
  `tahun_mbl` int DEFAULT NULL,
  `warna_mbl` varchar(255) DEFAULT NULL,
  `stok_mbl` int DEFAULT NULL,
  `harga_sewa_mbl` int DEFAULT NULL,
  `driver` enum('ya','tidak') NOT NULL DEFAULT 'tidak',
  PRIMARY KEY (`id_mbl`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `motor` (
  `id_mtr` int NOT NULL,
  `jenis_mtr` varchar(255) DEFAULT NULL,
  `type_mtr` varchar(255) DEFAULT NULL,
  `tahun_mtr` int DEFAULT NULL,
  `warna_mtr` varchar(255) DEFAULT NULL,
  `stok_mtr` int DEFAULT NULL,
  `harga_sewa_mtr` int DEFAULT NULL,
  `driver` enum('ya','tidak') NOT NULL DEFAULT 'tidak',
  PRIMARY KEY (`id_mtr`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `pembayaran` (
  `id_transaksi` int NOT NULL AUTO_INCREMENT,
  `tanggal_dikembalikan` date NOT NULL,
  `total_pembayaran` decimal(10,2) NOT NULL,
  `denda` decimal(10,2) DEFAULT '0.00',
  `dibayarkan` decimal(10,2) DEFAULT NULL,
  `status` enum('Lunas','Belum Lunas','Kurang','Pending','Cancelled','Completed') DEFAULT NULL,
  `sisa_pembayaran_amount` decimal(10,2) DEFAULT NULL,
  PRIMARY KEY (`id_transaksi`),
  CONSTRAINT `pembayaran_ibfk_1` FOREIGN KEY (`id_transaksi`) REFERENCES `pinjam` (`id_transaksi`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `pembayaran_elf` (
  `id_transaksi_elf` int NOT NULL AUTO_INCREMENT,
  `tanggal_dikembalikan` date NOT NULL,
  `total_pembayaran` decimal(10,2) NOT NULL,
  `denda` decimal(10,2) DEFAULT '0.00',
  `dibayarkan` decimal(10,2) DEFAULT NULL,
  `status` enum('Lunas','Belum Lunas','Kurang','Pending','Cancelled','Completed') DEFAULT 'Belum Lunas',
  `sisa_pembayaran_amount` decimal(10,2) DEFAULT NULL,
  PRIMARY KEY (`id_transaksi_elf`),
  CONSTRAINT `pembayaran_elf_ibfk_1` FOREIGN KEY (`id_transaksi_elf`) REFERENCES `pinjam_elf` (`id_transaksi_elf`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `pembayaran_motor` (
  `id_transaksi_motor` int NOT NULL AUTO_INCREMENT,
  `tanggal_dikembalikan` date NOT NULL,
  `total_pembayaran` decimal(10,2) NOT NULL,
  `denda` decimal(10,2) DEFAULT '0.00',
  `dibayarkan` decimal(10,2) DEFAULT NULL,
  `status` enum('Lunas','Belum Lunas','Kurang','Pending','Cancelled','Completed') DEFAULT 'Belum Lunas',
  `sisa_pembayaran_amount` decimal(10,2) DEFAULT NULL,
  PRIMARY KEY (`id_transaksi_motor`),
  CONSTRAINT `pembayaran_motor_ibfk_1` FOREIGN KEY (`id_transaksi_motor`) REFERENCES `pinjam_motor` (`id_transaksi_motor`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `pinjam` (
  `id_transaksi` int NOT NULL AUTO_INCREMENT,
  `id_mobil` int DEFAULT NULL,
  `harga_sewa_mobil` decimal(10,2) DEFAULT NULL,
  `tanggal_pinjam` date DEFAULT NULL,
  `tanggal_kembali` date DEFAULT NULL,
  `driver` enum('ya','tidak') DEFAULT NULL,
  PRIMARY KEY (`id_transaksi`),
  KEY `id_mobil` (`id_mobil`),
  CONSTRAINT `pinjam_ibfk_1` FOREIGN KEY (`id_mobil`) REFERENCES `mobil` (`id_mbl`) ON DELETE SET NULL ON UPDATE SET NULL
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `pinjam_elf` (
  `id_transaksi_elf` int NOT NULL AUTO_INCREMENT,
  `id_elf` int DEFAULT NULL,
  `harga_sewa_elf` decimal(10,2) DEFAULT NULL,
  `tanggal_pinjam` date DEFAULT NULL,
  `tanggal_kembali` date DEFAULT NULL,
  `driver` enum('ya','tidak') DEFAULT NULL,
  PRIMARY KEY (`id_transaksi_elf`),
  KEY `id_elf` (`id_elf`),
  CONSTRAINT `pinjam_elf_ibfk_1` FOREIGN KEY (`id_elf`) REFERENCES `elf` (`id_elf`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `pinjam_motor` (
  `id_transaksi_motor` int NOT NULL AUTO_INCREMENT,
  `id_motor` int DEFAULT NULL,
  `harga_sewa_motor` decimal(10,2) DEFAULT NULL,
  `tanggal_pinjam` date DEFAULT NULL,
  `tanggal_kembali` date DEFAULT NULL,
  `driver` enum('ya','tidak') DEFAULT NULL,
  PRIMARY KEY (`id_transaksi_motor`),
  KEY `id_motor` (`id_motor`),
  CONSTRAINT `pinjam_motor_ibfk_1` FOREIGN KEY (`id_motor`) REFERENCES `motor` (`id_mtr`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nama` varchar(100) DEFAULT NULL,
  `alamat` varchar(100) DEFAULT NULL,
  `no_hp` int DEFAULT NULL,
  `username` varchar(50) DEFAULT NULL,
  `password` varchar(50) DEFAULT NULL,
  `level` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO `elf` (`id_elf`, `jenis_elf`, `type_elf`, `tahun_elf`, `warna_elf`, `stok_elf`, `harga_sewa_elf`, `driver`) VALUES
(1, 'Mercy', 'E60', 2018, 'Hitam', 2, 250000, 'tidak');
INSERT INTO `elf` (`id_elf`, `jenis_elf`, `type_elf`, `tahun_elf`, `warna_elf`, `stok_elf`, `harga_sewa_elf`, `driver`) VALUES
(2, 'Mercy', 'F60', 2021, 'Merah Muda', 1, 250000, 'tidak');


INSERT INTO `mobil` (`id_mbl`, `jenis_mbl`, `type_mbl`, `tahun_mbl`, `warna_mbl`, `stok_mbl`, `harga_sewa_mbl`, `driver`) VALUES
(1, 'Honda', 'Jazz', 2017, 'Putih', 4, 150000, 'tidak');
INSERT INTO `mobil` (`id_mbl`, `jenis_mbl`, `type_mbl`, `tahun_mbl`, `warna_mbl`, `stok_mbl`, `harga_sewa_mbl`, `driver`) VALUES
(2, 'Toyota', 'Yaris', 2022, 'Kuning', 1, 150000, 'tidak');


INSERT INTO `motor` (`id_mtr`, `jenis_mtr`, `type_mtr`, `tahun_mtr`, `warna_mtr`, `stok_mtr`, `harga_sewa_mtr`, `driver`) VALUES
(1, 'Vario', '160cc', 2021, 'hitam', 2, 70000, 'tidak');
INSERT INTO `motor` (`id_mtr`, `jenis_mtr`, `type_mtr`, `tahun_mtr`, `warna_mtr`, `stok_mtr`, `harga_sewa_mtr`, `driver`) VALUES
(2, 'Yamaha', 'Nmax', 2022, 'Hitam', 2, 100000, 'tidak');


INSERT INTO `pembayaran` (`id_transaksi`, `tanggal_dikembalikan`, `total_pembayaran`, `denda`, `dibayarkan`, `status`, `sisa_pembayaran_amount`) VALUES
(11, '2000-01-01', '150000.00', '0.00', '77777.00', 'Kurang', '72223.00');


INSERT INTO `pembayaran_elf` (`id_transaksi_elf`, `tanggal_dikembalikan`, `total_pembayaran`, `denda`, `dibayarkan`, `status`, `sisa_pembayaran_amount`) VALUES
(1, '2000-02-01', '405000.00', '155000.00', '1000.00', 'Kurang', '404000.00');


INSERT INTO `pembayaran_motor` (`id_transaksi_motor`, `tanggal_dikembalikan`, `total_pembayaran`, `denda`, `dibayarkan`, `status`, `sisa_pembayaran_amount`) VALUES
(2, '2000-02-01', '225000.00', '155000.00', '10000.00', 'Kurang', '215000.00');


INSERT INTO `pinjam` (`id_transaksi`, `id_mobil`, `harga_sewa_mobil`, `tanggal_pinjam`, `tanggal_kembali`, `driver`) VALUES
(11, 1, '150000.00', '2000-01-01', '2000-02-01', 'tidak');


INSERT INTO `pinjam_elf` (`id_transaksi_elf`, `id_elf`, `harga_sewa_elf`, `tanggal_pinjam`, `tanggal_kembali`, `driver`) VALUES
(1, 1, '250000.00', '2000-01-01', '2000-02-01', 'tidak');
INSERT INTO `pinjam_elf` (`id_transaksi_elf`, `id_elf`, `harga_sewa_elf`, `tanggal_pinjam`, `tanggal_kembali`, `driver`) VALUES
(2, 1, '250000.00', '2000-01-01', '2000-02-01', 'tidak');


INSERT INTO `pinjam_motor` (`id_transaksi_motor`, `id_motor`, `harga_sewa_motor`, `tanggal_pinjam`, `tanggal_kembali`, `driver`) VALUES
(2, 1, '70000.00', '2000-01-01', '2000-05-01', 'tidak');
INSERT INTO `pinjam_motor` (`id_transaksi_motor`, `id_motor`, `harga_sewa_motor`, `tanggal_pinjam`, `tanggal_kembali`, `driver`) VALUES
(3, 1, '70000.00', '2024-01-01', '2024-01-03', 'tidak');
INSERT INTO `pinjam_motor` (`id_transaksi_motor`, `id_motor`, `harga_sewa_motor`, `tanggal_pinjam`, `tanggal_kembali`, `driver`) VALUES
(4, 2, '100000.00', '2024-01-07', '2024-01-09', 'tidak');

INSERT INTO `user` (`id`, `nama`, `alamat`, `no_hp`, `username`, `password`, `level`) VALUES
(1, 'Loki', 'Kediri', 81231, 'admin', '1234', 'admin');
INSERT INTO `user` (`id`, `nama`, `alamat`, `no_hp`, `username`, `password`, `level`) VALUES
(2, 'Hoshi', 'Kediri', 862, 'test', '1234', 'penyewa');



/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;