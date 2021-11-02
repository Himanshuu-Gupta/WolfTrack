-- MySQL dump 10.13  Distrib 8.0.26, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: wolftrack
-- ------------------------------------------------------
-- Server version	8.0.26

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Dumping data for table `roles`
--
--SIGNUP stored procedure creating the user and inserting the user in corresponding table
CREATE DEFINER=`admin`@`%` PROCEDURE `CreateUser`(IN email varchar(256),IN name varchar(256),IN password varchar(256))
BEGIN
	INSERT INTO `user_login`(password) values(password);
    SET @last_id_in_user_login = LAST_INSERT_ID();
	INSERT INTO `user`(user_id,email,full_name) values(@last_id_in_user_login,email,name);
END

LOCK TABLES `roles` WRITE;
/*!40000 ALTER TABLE `roles` DISABLE KEYS */;
INSERT INTO `roles` (`role_id`, `role`) VALUES (1,'SDE I');
INSERT INTO `roles` (`role_id`, `role`) VALUES (2,'SDE II');
INSERT INTO `roles` (`role_id`, `role`) VALUES (3,'Data Analyst');
INSERT INTO `roles` (`role_id`, `role`) VALUES (4,'Data Engineer');
INSERT INTO `roles` (`role_id`, `role`) VALUES (5,'HR');
INSERT INTO `roles` (`role_id`, `role`) VALUES (6,'Corporate Lawyer');
INSERT INTO `roles` (`role_id`, `role`) VALUES (7,'IT Staff');
INSERT INTO `roles` (`role_id`, `role`) VALUES (8,'Intern');
/*!40000 ALTER TABLE `roles` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `company`
--
	
LOCK TABLES `company` WRITE;
/*!40000 ALTER TABLE `company` DISABLE KEYS */;
INSERT INTO `company` (`company_id`, `company_name`) VALUES (1,'Google');
INSERT INTO `company` (`company_id`, `company_name`) VALUES (2,'Amazon');
INSERT INTO `company` (`company_id`, `company_name`) VALUES (3,'Facebook');
INSERT INTO `company` (`company_id`, `company_name`) VALUES (4,'Intuit');
INSERT INTO `company` (`company_id`, `company_name`) VALUES (5,'Twitter');
INSERT INTO `company` (`company_id`, `company_name`) VALUES (6,'LinkedIn');
INSERT INTO `company` (`company_id`, `company_name`) VALUES (7,'Toast');
INSERT INTO `company` (`company_id`, `company_name`) VALUES (8,'FlexGen');
INSERT INTO `company` (`company_id`, `company_name`) VALUES (9,'Netflix');
INSERT INTO `company` (`company_id`, `company_name`) VALUES (10,'Microsoft');
INSERT INTO `company` (`company_id`, `company_name`) VALUES (11,'Salesforce');
INSERT INTO `company` (`company_id`, `company_name`) VALUES (12,'SAS');
/*!40000 ALTER TABLE `company` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` (`user_id`, `email`, `full_name`) VALUES (1,'jessica123@ncsu.edu','Jessica Holds');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `application`
--

LOCK TABLES `application` WRITE;
/*!40000 ALTER TABLE `application` DISABLE KEYS */;
INSERT INTO `application` (`application_id`, `user_id`, `company_id`, `role_id`, `recruiter_id`, `application_date`, `job_description`, `salary`, `location`, `imortant_links`, `status`, `due_date`) VALUES (1,1,1,3,NULL,'2021-01-01 05:00:00',NULL,90000,'Mountain View',NULL,'TO_DO','2021-02-01 05:00:00');
INSERT INTO `application` (`application_id`, `user_id`, `company_id`, `role_id`, `recruiter_id`, `application_date`, `job_description`, `salary`, `location`, `imortant_links`, `status`, `due_date`) VALUES (2,1,2,3,NULL,'2021-01-01 05:00:00',NULL,70000,'Seattle',NULL,'TO_DO','2021-01-06 05:00:00');
INSERT INTO `application` (`application_id`, `user_id`, `company_id`, `role_id`, `recruiter_id`, `application_date`, `job_description`, `salary`, `location`, `imortant_links`, `status`, `due_date`) VALUES (3,1,3,3,NULL,'2021-01-01 05:00:00',NULL,50000,'Seattle',NULL,'TO_DO','2021-01-06 05:00:00');
INSERT INTO `application` (`application_id`, `user_id`, `company_id`, `role_id`, `recruiter_id`, `application_date`, `job_description`, `salary`, `location`, `imortant_links`, `status`, `due_date`) VALUES (4,1,4,3,NULL,'2021-01-01 05:00:00',NULL,50000,'Seattle',NULL,'APPLIED','2021-01-17 05:00:00');
INSERT INTO `application` (`application_id`, `user_id`, `company_id`, `role_id`, `recruiter_id`, `application_date`, `job_description`, `salary`, `location`, `imortant_links`, `status`, `due_date`) VALUES (5,1,8,3,NULL,'2021-01-01 05:00:00',NULL,75000,'Texas',NULL,'APPLIED','2021-01-17 05:00:00');
INSERT INTO `application` (`application_id`, `user_id`, `company_id`, `role_id`, `recruiter_id`, `application_date`, `job_description`, `salary`, `location`, `imortant_links`, `status`, `due_date`) VALUES (6,1,6,3,NULL,'2021-01-07 05:00:00',NULL,90000,'Arizona',NULL,'APPLIED','2021-01-17 05:00:00');
INSERT INTO `application` (`application_id`, `user_id`, `company_id`, `role_id`, `recruiter_id`, `application_date`, `job_description`, `salary`, `location`, `imortant_links`, `status`, `due_date`) VALUES (7,1,7,3,NULL,'2021-02-07 05:00:00',NULL,95000,'New York',NULL,'IN_PROCESS','2021-02-17 05:00:00');
INSERT INTO `application` (`application_id`, `user_id`, `company_id`, `role_id`, `recruiter_id`, `application_date`, `job_description`, `salary`, `location`, `imortant_links`, `status`, `due_date`) VALUES (8,1,1,7,NULL,'2021-09-20 04:00:00',NULL,95000,'New York',NULL,'IN_PROCESS','2021-10-17 04:00:00');
INSERT INTO `application` (`application_id`, `user_id`, `company_id`, `role_id`, `recruiter_id`, `application_date`, `job_description`, `salary`, `location`, `imortant_links`, `status`, `due_date`) VALUES (9,1,2,7,NULL,'2021-09-23 04:00:00',NULL,95000,'Raleigh',NULL,'IN_PROCESS','2021-10-27 04:00:00');
INSERT INTO `application` (`application_id`, `user_id`, `company_id`, `role_id`, `recruiter_id`, `application_date`, `job_description`, `salary`, `location`, `imortant_links`, `status`, `due_date`) VALUES (10,1,5,7,NULL,'2021-09-23 04:00:00',NULL,55000,'Dallas',NULL,'ACCEPTED','2021-10-30 04:00:00');
INSERT INTO `application` (`application_id`, `user_id`, `company_id`, `role_id`, `recruiter_id`, `application_date`, `job_description`, `salary`, `location`, `imortant_links`, `status`, `due_date`) VALUES (11,1,7,3,NULL,'2021-09-27 04:00:00',NULL,55000,'Sunnyvale',NULL,'ACCEPTED','2021-10-30 04:00:00');
INSERT INTO `application` (`application_id`, `user_id`, `company_id`, `role_id`, `recruiter_id`, `application_date`, `job_description`, `salary`, `location`, `imortant_links`, `status`, `due_date`) VALUES (12,1,8,3,NULL,'2021-08-27 04:00:00',NULL,65000,'Houston',NULL,'ACCEPTED','2021-10-30 04:00:00');
/*!40000 ALTER TABLE `application` ENABLE KEYS */;
UNLOCK TABLES;


--
-- Dumping data for table `recruiter`
--

LOCK TABLES `recruiter` WRITE;
/*!40000 ALTER TABLE `recruiter` DISABLE KEYS */;
/*!40000 ALTER TABLE `recruiter` ENABLE KEYS */;
UNLOCK TABLES;


--
-- Dumping data for table `user_details`
--

LOCK TABLES `user_details` WRITE;
/*!40000 ALTER TABLE `user_details` DISABLE KEYS */;
/*!40000 ALTER TABLE `user_details` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `user_login`
--

LOCK TABLES `user_login` WRITE;
/*!40000 ALTER TABLE `user_login` DISABLE KEYS */;
INSERT INTO `user_login` (`id`, `user_id`, `password`) VALUES (1,1,'admin');
/*!40000 ALTER TABLE `user_login` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-09-27 23:20:15
