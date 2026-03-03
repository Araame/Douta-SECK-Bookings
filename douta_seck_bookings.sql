-- MySQL dump 10.13  Distrib 8.0.45, for Linux (x86_64)
--
-- Host: localhost    Database: Douta_SECK_bookings
-- ------------------------------------------------------
-- Server version	8.0.45-0ubuntu0.24.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Bookings`
--

DROP TABLE IF EXISTS `Bookings`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Bookings` (
  `id_booking` int NOT NULL AUTO_INCREMENT,
  `user` int NOT NULL,
  `event` int NOT NULL,
  `slot` int NOT NULL,
  `motif` text NOT NULL,
  `date` datetime NOT NULL,
  `confirmed` tinyint(1) DEFAULT '1',
  PRIMARY KEY (`id_booking`),
  KEY `staff` (`user`),
  KEY `event` (`event`),
  KEY `slot` (`slot`),
  CONSTRAINT `Bookings_ibfk_2` FOREIGN KEY (`user`) REFERENCES `Users` (`id_staff`),
  CONSTRAINT `Bookings_ibfk_3` FOREIGN KEY (`event`) REFERENCES `Events` (`id_event`),
  CONSTRAINT `Bookings_ibfk_4` FOREIGN KEY (`slot`) REFERENCES `Slots` (`id_slot`)
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Bookings`
--

LOCK TABLES `Bookings` WRITE;
/*!40000 ALTER TABLE `Bookings` DISABLE KEYS */;
INSERT INTO `Bookings` VALUES (1,2,1,1,'kjhgf','2026-03-01 00:00:00',1),(2,3,1,1,'dfghj','2026-03-01 00:00:00',1),(3,3,1,1,'dfghj','2026-03-01 00:00:00',1),(4,3,1,1,'dfghj','2026-03-01 00:00:00',1),(5,3,1,1,'dfghj','2026-03-01 00:00:00',1),(6,3,1,1,'dfghj','2026-03-01 00:00:00',1),(7,3,1,1,'dfghj','2026-03-01 00:00:00',1),(8,3,1,1,'dfghj','2026-03-01 00:00:00',1),(9,3,1,1,'dfghj','2026-03-01 00:00:00',1),(10,3,1,1,'dfghj','2026-05-01 00:00:00',1),(11,3,1,1,'dfghj','2026-05-01 00:00:00',1),(12,3,1,1,'dfghj','2026-05-01 00:00:00',1),(13,3,1,1,'dfghj','2026-05-01 00:00:00',1),(14,2,1,1,'fhjjj','2026-03-02 00:00:00',1),(15,2,1,1,'fhjjj','2026-03-01 00:00:00',1),(16,2,1,1,'fhjjj','2026-03-01 00:00:00',1),(17,2,1,1,'fhjjj','2026-03-01 00:00:00',1),(18,2,1,1,'fhjjj','2026-03-01 00:00:00',1),(19,2,1,1,'fhjjj','2026-03-01 00:00:00',1),(20,2,1,1,'fhjjj','2026-03-01 00:00:00',1),(21,2,1,1,'fhjjj','2026-03-01 00:00:00',1),(22,2,1,1,'fhjjj','2001-03-26 00:00:00',1),(23,2,1,1,'fhjjj','2001-03-26 00:00:00',1),(24,2,1,1,'fhjjj','2001-03-26 00:00:00',1),(26,3,1,1,'fds','2026-03-04 00:00:00',1),(27,3,1,1,'kjhgf','2026-03-03 00:00:00',0);
/*!40000 ALTER TABLE `Bookings` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Events`
--

DROP TABLE IF EXISTS `Events`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Events` (
  `id_event` int NOT NULL AUTO_INCREMENT,
  `type_event` varchar(40) NOT NULL,
  PRIMARY KEY (`id_event`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Events`
--

LOCK TABLES `Events` WRITE;
/*!40000 ALTER TABLE `Events` DISABLE KEYS */;
INSERT INTO `Events` VALUES (1,'festival');
/*!40000 ALTER TABLE `Events` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Roles`
--

DROP TABLE IF EXISTS `Roles`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Roles` (
  `id_role` int NOT NULL AUTO_INCREMENT,
  `role` varchar(30) NOT NULL,
  PRIMARY KEY (`id_role`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Roles`
--

LOCK TABLES `Roles` WRITE;
/*!40000 ALTER TABLE `Roles` DISABLE KEYS */;
INSERT INTO `Roles` VALUES (1,'simple'),(2,'admin');
/*!40000 ALTER TABLE `Roles` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Slots`
--

DROP TABLE IF EXISTS `Slots`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Slots` (
  `id_slot` int NOT NULL AUTO_INCREMENT,
  `moment` varchar(15) NOT NULL,
  `end` time NOT NULL,
  `start` time NOT NULL,
  PRIMARY KEY (`id_slot`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Slots`
--

LOCK TABLES `Slots` WRITE;
/*!40000 ALTER TABLE `Slots` DISABLE KEYS */;
INSERT INTO `Slots` VALUES (1,'matin','12:10:00','08:00:00'),(2,'apres midi','15:00:00','20:00:00');
/*!40000 ALTER TABLE `Slots` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Users`
--

DROP TABLE IF EXISTS `Users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Users` (
  `id_staff` int NOT NULL AUTO_INCREMENT,
  `firstname` varchar(30) NOT NULL,
  `lastname` varchar(20) NOT NULL,
  `email` varchar(40) NOT NULL,
  `call_number` varchar(13) NOT NULL,
  `role` int NOT NULL DEFAULT '1',
  `password` varchar(255) NOT NULL,
  PRIMARY KEY (`id_staff`),
  UNIQUE KEY `email` (`email`),
  UNIQUE KEY `call_number` (`call_number`),
  KEY `role` (`role`),
  CONSTRAINT `Users_ibfk_1` FOREIGN KEY (`role`) REFERENCES `Roles` (`id_role`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Users`
--

LOCK TABLES `Users` WRITE;
/*!40000 ALTER TABLE `Users` DISABLE KEYS */;
INSERT INTO `Users` VALUES (2,'diop','fat','fat@gmail.com','776587655',1,'fatdiop'),(3,'Arame','DIENG','aram@gmail.com','221778909907',2,'$2b$12$41I.2Ynx3RaKuBMdVSWUWOmyntYYBNGYbcA7GTL3660Y.vt/D4NIK'),(4,'Birane','LY','birane@gmail.com','781234567',1,'$2b$12$Hcu9lPQEK0721FOYNrmU8eadx76j8euFFtb.b3g6J09jZXuN9x9MC');
/*!40000 ALTER TABLE `Users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-03-03  8:55:11
