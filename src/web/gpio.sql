-- MySQL dump 10.13  Distrib 5.5.40, for debian-linux-gnu (armv7l)
--
-- Host: localhost    Database: gpio
-- ------------------------------------------------------
-- Server version	5.5.40-0+wheezy1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `pinDescription`
--

DROP TABLE IF EXISTS `pinDescription`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `pinDescription` (
  `pinID` int(11) NOT NULL AUTO_INCREMENT,
  `pinNumber` varchar(2) COLLATE utf8_unicode_ci NOT NULL,
  `pinDescription` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`pinID`),
  UNIQUE KEY `pinNumber` (`pinNumber`)
) ENGINE=MyISAM AUTO_INCREMENT=9 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pinDescription`
--

LOCK TABLES `pinDescription` WRITE;
/*!40000 ALTER TABLE `pinDescription` DISABLE KEYS */;
INSERT INTO `pinDescription` VALUES (1,'4','Little light'),(2,'17','Pin 17'),(3,'18','Pin 18'),(4,'21','Pin 21'),(5,'22','Pin 22'),(6,'23','Pin 23'),(7,'24','Pin 24'),(8,'25','Pin 25');
/*!40000 ALTER TABLE `pinDescription` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pinDirection`
--

DROP TABLE IF EXISTS `pinDirection`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `pinDirection` (
  `pinID` int(11) NOT NULL AUTO_INCREMENT,
  `pinNumber` varchar(2) COLLATE utf8_unicode_ci NOT NULL,
  `pinDirection` varchar(3) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`pinID`),
  UNIQUE KEY `pinNumber` (`pinNumber`)
) ENGINE=MyISAM AUTO_INCREMENT=9 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pinDirection`
--

LOCK TABLES `pinDirection` WRITE;
/*!40000 ALTER TABLE `pinDirection` DISABLE KEYS */;
INSERT INTO `pinDirection` VALUES (1,'4','out'),(2,'17','out'),(3,'18','out'),(4,'21','out'),(5,'22','out'),(6,'23','out'),(7,'24','out'),(8,'25','out');
/*!40000 ALTER TABLE `pinDirection` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pinStatus`
--

DROP TABLE IF EXISTS `pinStatus`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `pinStatus` (
  `pinID` int(11) NOT NULL AUTO_INCREMENT,
  `pinNumber` varchar(2) COLLATE utf8_unicode_ci NOT NULL,
  `pinStatus` varchar(1) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`pinID`),
  UNIQUE KEY `pinNumber` (`pinNumber`)
) ENGINE=MyISAM AUTO_INCREMENT=9 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pinStatus`
--

LOCK TABLES `pinStatus` WRITE;
/*!40000 ALTER TABLE `pinStatus` DISABLE KEYS */;
INSERT INTO `pinStatus` VALUES (1,'4','0'),(2,'17','0'),(3,'18','0'),(4,'21','0'),(5,'22','0'),(6,'23','0'),(7,'24','0'),(8,'25','0');
/*!40000 ALTER TABLE `pinStatus` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tracker`
--

DROP TABLE IF EXISTS `tracker`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tracker` (
  `ip` varchar(50) DEFAULT NULL,
  `action` varchar(1) DEFAULT NULL,
  `city` varchar(32) DEFAULT NULL,
  `location` varchar(24) DEFAULT NULL,
  `timstamp` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tracker`
--

LOCK TABLES `tracker` WRITE;
/*!40000 ALTER TABLE `tracker` DISABLE KEYS */;
INSERT INTO `tracker` VALUES ('70.197.10.110','0','Pleasanton','37.6624,-121.8747','2014-12-15 07:12:07'),('184.152.76.182','1','Brooklyn','40.6944,-73.9906','2014-12-16 03:03:08'),('184.152.76.182','0','Brooklyn','40.6944,-73.9906','2014-12-16 05:02:09'),('184.152.76.182','1','Brooklyn','40.6944,-73.9906','2014-12-16 05:04:47'),('203.13.146.17','1','Bangalore','12.9833,77.5833','2014-12-16 06:41:34'),('203.13.146.17','0','Bangalore','12.9833,77.5833','2014-12-16 06:43:21'),('203.13.146.17','1','Bangalore','12.9833,77.5833','2014-12-16 06:44:38'),('203.13.146.17','0','Bangalore','12.9833,77.5833','2014-12-16 06:44:43'),('203.13.146.17','1','Bangalore','12.9833,77.5833','2014-12-16 06:44:48'),('203.13.146.17','0','Bangalore','12.9833,77.5833','2014-12-16 06:44:51'),('203.13.146.17','1','Bangalore','12.9833,77.5833','2014-12-16 06:44:54'),('203.13.146.17','0','Bangalore','12.9833,77.5833','2014-12-16 06:44:59'),('203.13.146.17','1','Bangalore','12.9833,77.5833','2014-12-16 06:47:29'),('203.13.146.17','0','Bangalore','12.9833,77.5833','2014-12-16 06:47:42');
/*!40000 ALTER TABLE `tracker` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `userID` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(28) COLLATE utf8_unicode_ci NOT NULL,
  `password` varchar(64) COLLATE utf8_unicode_ci NOT NULL,
  `salt` varchar(8) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`userID`),
  UNIQUE KEY `username` (`username`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'admin','25da86bfcf5296b16424c09a709d5ccf0f62096dce9b978ce75396518427220f','b2195a8a');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2015-04-04 15:19:11
