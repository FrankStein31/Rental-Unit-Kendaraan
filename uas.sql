/*
SQLyog Professional v13.1.1 (64 bit)
MySQL - 8.0.30 : Database - uas
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`uas` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;

USE `uas`;

/*Table structure for table `elf` */

DROP TABLE IF EXISTS `elf`;

CREATE TABLE `elf` (
  `id_elf` int NOT NULL,
  `jenis_elf` varchar(255) DEFAULT NULL,
  `type_elf` varchar(255) DEFAULT NULL,
  `tahun_elf` int DEFAULT NULL,
  `warna_elf` varchar(255) DEFAULT NULL,
  `stok_elf` int DEFAULT NULL,
  `harga_sewa_elf` int DEFAULT NULL,
  `driver` enum('ya','tidak') NOT NULL DEFAULT 'tidak',
  `foto` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id_elf`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `elf` */

insert  into `elf`(`id_elf`,`jenis_elf`,`type_elf`,`tahun_elf`,`warna_elf`,`stok_elf`,`harga_sewa_elf`,`driver`,`foto`) values 
(1,'Mercy','E60',2018,'Hitam',18,250000,'tidak','elf_images\\1f4f2da6-5e61-4ba7-8d9c-29b44a7ee339_1734193971_th (4).jpeg'),
(2,'Mercy','F60',2021,'Merah Muda',9,250000,'tidak','elf_images\\9cab189f-38d4-4998-8dfd-b3390c203a83_1734193963_th (4).jpeg');

/*Table structure for table `mobil` */

DROP TABLE IF EXISTS `mobil`;

CREATE TABLE `mobil` (
  `id_mbl` int NOT NULL,
  `jenis_mbl` varchar(255) DEFAULT NULL,
  `type_mbl` varchar(255) DEFAULT NULL,
  `tahun_mbl` int DEFAULT NULL,
  `warna_mbl` varchar(255) DEFAULT NULL,
  `stok_mbl` int DEFAULT NULL,
  `harga_sewa_mbl` int DEFAULT NULL,
  `driver` enum('ya','tidak') NOT NULL DEFAULT 'tidak',
  `foto` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id_mbl`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `mobil` */

insert  into `mobil`(`id_mbl`,`jenis_mbl`,`type_mbl`,`tahun_mbl`,`warna_mbl`,`stok_mbl`,`harga_sewa_mbl`,`driver`,`foto`) values 
(1,'Honda','Jazz',2017,'Putih',24,150000,'tidak','mobil_images\\9fbd2198-303e-4c8a-a46b-a81a4302aa5d_1734193941_th (3).jpeg'),
(2,'Toyota','Yaris',2022,'Kuning',10,150000,'tidak','mobil_images\\4a3483bd-526b-4881-8f46-83baf367dfeb_1734172427_th (3).jpeg');

/*Table structure for table `motor` */

DROP TABLE IF EXISTS `motor`;

CREATE TABLE `motor` (
  `id_mtr` int NOT NULL,
  `jenis_mtr` varchar(255) DEFAULT NULL,
  `type_mtr` varchar(255) DEFAULT NULL,
  `tahun_mtr` int DEFAULT NULL,
  `warna_mtr` varchar(255) DEFAULT NULL,
  `stok_mtr` int DEFAULT NULL,
  `harga_sewa_mtr` int DEFAULT NULL,
  `driver` enum('ya','tidak') NOT NULL DEFAULT 'tidak',
  `foto` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id_mtr`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `motor` */

insert  into `motor`(`id_mtr`,`jenis_mtr`,`type_mtr`,`tahun_mtr`,`warna_mtr`,`stok_mtr`,`harga_sewa_mtr`,`driver`,`foto`) values 
(1,'Vario','160cc',2021,'hitam',33,70000,'tidak','motor_images\\d0550133-2856-4635-8859-1beed65c4130_1734193907_th (2).jpeg'),
(2,'Yamaha','Nmax',2024,'Hitam',95,75000,'tidak','motor_images\\57b6dc7c-5d42-43de-8545-bc8b3a2f924f_1734193895_th (2).jpeg'),
(4,'tesss','tess',2021,'putih',90,35000,'tidak','motor_images\\1734161331_th (2).jpeg'),
(5,'coba','coba',1234,'coba',31,54000,'tidak','motor_images\\379c6263-b20e-4923-b10f-99bae40563c6_1734234063_th (5).jpeg');

/*Table structure for table `pembayaran` */

DROP TABLE IF EXISTS `pembayaran`;

CREATE TABLE `pembayaran` (
  `id_transaksi` int NOT NULL AUTO_INCREMENT,
  `id_user` int DEFAULT NULL,
  `tanggal_dikembalikan` date NOT NULL,
  `total_pembayaran` decimal(10,2) NOT NULL,
  `denda` decimal(10,2) DEFAULT '0.00',
  `dibayarkan` decimal(10,2) DEFAULT NULL,
  `status` enum('Lunas','Belum Lunas','Kurang','Pending','Cancelled','Completed') DEFAULT NULL,
  `sisa_pembayaran_amount` decimal(10,2) DEFAULT NULL,
  PRIMARY KEY (`id_transaksi`),
  CONSTRAINT `pembayaran_ibfk_1` FOREIGN KEY (`id_transaksi`) REFERENCES `pinjam` (`id_transaksi`)
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `pembayaran` */

insert  into `pembayaran`(`id_transaksi`,`id_user`,`tanggal_dikembalikan`,`total_pembayaran`,`denda`,`dibayarkan`,`status`,`sisa_pembayaran_amount`) values 
(15,7,'2000-03-01',450000.00,300000.00,1000000.00,'Lunas',-550000.00),
(22,8,'2024-12-12',160000.00,10000.00,200000.00,'Pending',-40000.00),
(25,8,'2024-12-12',510000.00,10000.00,520000.00,'Pending',-10000.00),
(26,8,'2024-12-12',510000.00,10000.00,510000.00,'Completed',0.00),
(27,8,'2024-12-16',300000.00,0.00,300000.00,'Completed',0.00);

/*Table structure for table `pembayaran_elf` */

DROP TABLE IF EXISTS `pembayaran_elf`;

CREATE TABLE `pembayaran_elf` (
  `id_transaksi_elf` int NOT NULL AUTO_INCREMENT,
  `id_user` int DEFAULT NULL,
  `tanggal_dikembalikan` date NOT NULL,
  `total_pembayaran` decimal(10,2) NOT NULL,
  `denda` decimal(10,2) DEFAULT '0.00',
  `dibayarkan` decimal(10,2) DEFAULT NULL,
  `status` enum('Lunas','Belum Lunas','Kurang','Pending','Cancelled','Completed') DEFAULT 'Belum Lunas',
  `sisa_pembayaran_amount` decimal(10,2) DEFAULT NULL,
  PRIMARY KEY (`id_transaksi_elf`),
  CONSTRAINT `pembayaran_elf_ibfk_1` FOREIGN KEY (`id_transaksi_elf`) REFERENCES `pinjam_elf` (`id_transaksi_elf`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `pembayaran_elf` */

insert  into `pembayaran_elf`(`id_transaksi_elf`,`id_user`,`tanggal_dikembalikan`,`total_pembayaran`,`denda`,`dibayarkan`,`status`,`sisa_pembayaran_amount`) values 
(4,7,'2000-02-01',405000.00,155000.00,700000.00,'Lunas',-295000.00),
(6,8,'2024-12-12',710000.00,10000.00,710000.00,'Pending',0.00),
(7,7,'2024-12-16',350000.00,0.00,350000.00,'Completed',0.00);

/*Table structure for table `pembayaran_motor` */

DROP TABLE IF EXISTS `pembayaran_motor`;

CREATE TABLE `pembayaran_motor` (
  `id_transaksi_motor` int NOT NULL AUTO_INCREMENT,
  `id_user` int DEFAULT NULL,
  `tanggal_dikembalikan` date NOT NULL,
  `total_pembayaran` decimal(10,2) NOT NULL,
  `denda` decimal(10,2) DEFAULT '0.00',
  `dibayarkan` decimal(10,2) DEFAULT NULL,
  `status` enum('Lunas','Belum Lunas','Kurang','Pending','Cancelled','Completed') DEFAULT 'Belum Lunas',
  `sisa_pembayaran_amount` decimal(10,2) DEFAULT NULL,
  PRIMARY KEY (`id_transaksi_motor`),
  CONSTRAINT `pembayaran_motor_ibfk_1` FOREIGN KEY (`id_transaksi_motor`) REFERENCES `pinjam_motor` (`id_transaksi_motor`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `pembayaran_motor` */

insert  into `pembayaran_motor`(`id_transaksi_motor`,`id_user`,`tanggal_dikembalikan`,`total_pembayaran`,`denda`,`dibayarkan`,`status`,`sisa_pembayaran_amount`) values 
(6,7,'2000-01-02',75000.00,5000.00,270000.00,'Lunas',-195000.00),
(7,7,'2000-01-01',100000.00,0.00,100000.00,'Lunas',0.00),
(12,7,'2000-01-01',75000.00,0.00,NULL,'Lunas',NULL),
(16,8,'2024-12-15',70000.00,0.00,70000.00,'Completed',0.00);

/*Table structure for table `pinjam` */

DROP TABLE IF EXISTS `pinjam`;

CREATE TABLE `pinjam` (
  `id_transaksi` int NOT NULL AUTO_INCREMENT,
  `id_mobil` int DEFAULT NULL,
  `id_user` int DEFAULT NULL,
  `harga_sewa_mobil` decimal(10,2) DEFAULT NULL,
  `tanggal_pinjam` date DEFAULT NULL,
  `tanggal_kembali` date DEFAULT NULL,
  `jumlah_disewa` int DEFAULT NULL,
  `driver` enum('ya','tidak') DEFAULT NULL,
  PRIMARY KEY (`id_transaksi`),
  KEY `id_mobil` (`id_mobil`),
  CONSTRAINT `pinjam_ibfk_1` FOREIGN KEY (`id_mobil`) REFERENCES `mobil` (`id_mbl`) ON DELETE SET NULL ON UPDATE SET NULL
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `pinjam` */

insert  into `pinjam`(`id_transaksi`,`id_mobil`,`id_user`,`harga_sewa_mobil`,`tanggal_pinjam`,`tanggal_kembali`,`jumlah_disewa`,`driver`) values 
(11,1,NULL,150000.00,'2000-01-01','2000-02-01',NULL,'tidak'),
(15,1,7,150000.00,'2000-01-01','2000-01-03',NULL,'tidak'),
(22,1,8,150000.00,'2024-12-11','2024-12-12',1,'tidak'),
(25,1,8,500000.00,'2024-12-11','2024-12-12',2,'ya'),
(26,1,8,500000.00,'2024-12-11','2024-12-12',2,'ya'),
(27,2,8,300000.00,'2024-12-15','2024-12-16',2,'tidak');

/*Table structure for table `pinjam_elf` */

DROP TABLE IF EXISTS `pinjam_elf`;

CREATE TABLE `pinjam_elf` (
  `id_transaksi_elf` int NOT NULL AUTO_INCREMENT,
  `id_elf` int DEFAULT NULL,
  `id_user` int DEFAULT NULL,
  `harga_sewa_elf` decimal(10,2) DEFAULT NULL,
  `tanggal_pinjam` date DEFAULT NULL,
  `tanggal_kembali` date DEFAULT NULL,
  `jumlah_disewa` int DEFAULT NULL,
  `driver` enum('ya','tidak') DEFAULT NULL,
  PRIMARY KEY (`id_transaksi_elf`),
  KEY `id_elf` (`id_elf`),
  CONSTRAINT `pinjam_elf_ibfk_1` FOREIGN KEY (`id_elf`) REFERENCES `elf` (`id_elf`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `pinjam_elf` */

insert  into `pinjam_elf`(`id_transaksi_elf`,`id_elf`,`id_user`,`harga_sewa_elf`,`tanggal_pinjam`,`tanggal_kembali`,`jumlah_disewa`,`driver`) values 
(1,1,NULL,250000.00,'2000-01-01','2000-02-01',NULL,'tidak'),
(2,1,NULL,250000.00,'2000-01-01','2000-02-01',NULL,'tidak'),
(4,1,7,250000.00,'2000-01-01','2000-01-01',NULL,'tidak'),
(6,1,8,700000.00,'2024-12-11','2024-12-12',2,'ya'),
(7,2,7,350000.00,'2024-12-15','2024-12-16',1,'ya');

/*Table structure for table `pinjam_motor` */

DROP TABLE IF EXISTS `pinjam_motor`;

CREATE TABLE `pinjam_motor` (
  `id_transaksi_motor` int NOT NULL AUTO_INCREMENT,
  `id_motor` int DEFAULT NULL,
  `id_user` int DEFAULT NULL,
  `harga_sewa_motor` decimal(10,2) DEFAULT NULL,
  `tanggal_pinjam` date DEFAULT NULL,
  `tanggal_kembali` date DEFAULT NULL,
  `jumlah_disewa` int DEFAULT NULL,
  `driver` enum('ya','tidak') DEFAULT NULL,
  PRIMARY KEY (`id_transaksi_motor`),
  KEY `id_motor` (`id_motor`),
  CONSTRAINT `pinjam_motor_ibfk_1` FOREIGN KEY (`id_motor`) REFERENCES `motor` (`id_mtr`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `pinjam_motor` */

insert  into `pinjam_motor`(`id_transaksi_motor`,`id_motor`,`id_user`,`harga_sewa_motor`,`tanggal_pinjam`,`tanggal_kembali`,`jumlah_disewa`,`driver`) values 
(2,1,NULL,70000.00,'2000-01-01','2000-05-01',NULL,'tidak'),
(3,1,NULL,70000.00,'2024-01-01','2024-01-03',NULL,'tidak'),
(4,2,NULL,100000.00,'2024-01-07','2024-01-09',NULL,'tidak'),
(6,1,7,70000.00,'2000-01-01','2000-01-01',NULL,'tidak'),
(7,2,7,100000.00,'2000-01-01','2000-01-01',NULL,'tidak'),
(12,2,7,225000.00,'2024-12-14','2024-12-15',3,'tidak'),
(16,1,8,70000.00,'2024-12-14','2024-12-15',1,'tidak');

/*Table structure for table `user` */

DROP TABLE IF EXISTS `user`;

CREATE TABLE `user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nama` varchar(100) DEFAULT NULL,
  `alamat` varchar(100) DEFAULT NULL,
  `no_hp` int DEFAULT NULL,
  `username` varchar(50) DEFAULT NULL,
  `password` varchar(50) DEFAULT NULL,
  `level` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `user` */

insert  into `user`(`id`,`nama`,`alamat`,`no_hp`,`username`,`password`,`level`) values 
(1,'Loki','Kediri',81231,'admin','1234','admin'),
(2,'Hoshi','Kediri',862,'test','1234','penyewa'),
(7,'frank','medan',123,'frank','123','penyewa'),
(8,'stein','medan',123,'stein','123','penyewa');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
