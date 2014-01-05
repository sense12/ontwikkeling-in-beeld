/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


# Dump of table m_assignment
# ------------------------------------------------------------

DROP TABLE IF EXISTS `m_assignment`;

CREATE TABLE `m_assignment` (
  `assignment_id` bigint(11) unsigned NOT NULL AUTO_INCREMENT,
  `parent_assignment` int(11) DEFAULT NULL,
  `course_id` int(11) DEFAULT NULL,
  `title` varchar(200) NOT NULL DEFAULT '',
  `weight` smallint(10) NOT NULL DEFAULT '0',
  PRIMARY KEY (`assignment_id`),
  KEY `course_id` (`course_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

LOCK TABLES `m_assignment` WRITE;
/*!40000 ALTER TABLE `m_assignment` DISABLE KEYS */;

INSERT INTO `m_assignment` (`assignment_id`, `parent_assignment`, `course_id`, `title`, `weight`)
VALUES
	(1,NULL,1,'Omgaan met verschillen',10),
	(2,1,1,'Persoonlijke visie',0),
	(3,1,1,'Bedrijfs visie',0),
	(4,1,1,'Verschillen en overeenkomsten visie',0),
	(5,NULL,1,'Activiteiten ontwikkelen',10),
	(6,NULL,1,'Begeleiden en aansturen van de groep',30);

/*!40000 ALTER TABLE `m_assignment` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table m_course
# ------------------------------------------------------------

DROP TABLE IF EXISTS `m_course`;

CREATE TABLE `m_course` (
  `course_id` bigint(11) unsigned NOT NULL AUTO_INCREMENT,
  `title` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`course_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

LOCK TABLES `m_course` WRITE;
/*!40000 ALTER TABLE `m_course` DISABLE KEYS */;

INSERT INTO `m_course` (`course_id`, `title`)
VALUES
	(1,'BeroepsPrestatie 1');

/*!40000 ALTER TABLE `m_course` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table s_class
# ------------------------------------------------------------

DROP TABLE IF EXISTS `s_class`;

CREATE TABLE `s_class` (
  `class_id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `class_code` varchar(200) DEFAULT NULL,
  `start_year` year(4) DEFAULT NULL,
  PRIMARY KEY (`class_id`),
  UNIQUE KEY `class_code` (`class_code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

LOCK TABLES `s_class` WRITE;
/*!40000 ALTER TABLE `s_class` DISABLE KEYS */;

INSERT INTO `s_class` (`class_id`, `class_code`, `start_year`)
VALUES
	(1,'TAKPWA038A','2013'),
	(5,'TCIF-CBA03B','2000');

/*!40000 ALTER TABLE `s_class` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table s_enrollment
# ------------------------------------------------------------

DROP TABLE IF EXISTS `s_enrollment`;

CREATE TABLE `s_enrollment` (
  `id` bigint(11) unsigned NOT NULL AUTO_INCREMENT,
  `course_id` bigint(11) unsigned NOT NULL,
  `user_id` bigint(11) NOT NULL DEFAULT '0',
  `start_period` year(4) NOT NULL,
  `end_period` year(4) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`,`course_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='id is present because enrolments can be done twice for the s';

LOCK TABLES `s_enrollment` WRITE;
/*!40000 ALTER TABLE `s_enrollment` DISABLE KEYS */;

INSERT INTO `s_enrollment` (`id`, `course_id`, `user_id`, `start_period`, `end_period`)
VALUES
	(1,1,1,'2013','2014'),
	(2,1,3,'2013','2014');

/*!40000 ALTER TABLE `s_enrollment` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table s_milestone
# ------------------------------------------------------------

DROP TABLE IF EXISTS `s_milestone`;

CREATE TABLE `s_milestone` (
  `user_id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `class_id` int(11) unsigned DEFAULT NULL,
  `assignment_id` int(11) unsigned DEFAULT NULL,
  `finish_date` date DEFAULT NULL,
  PRIMARY KEY (`user_id`),
  KEY `relation` (`user_id`,`assignment_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

LOCK TABLES `s_milestone` WRITE;
/*!40000 ALTER TABLE `s_milestone` DISABLE KEYS */;

INSERT INTO `s_milestone` (`user_id`, `class_id`, `assignment_id`, `finish_date`)
VALUES
	(1,NULL,NULL,NULL);

/*!40000 ALTER TABLE `s_milestone` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table u_user
# ------------------------------------------------------------

DROP TABLE IF EXISTS `u_user`;

CREATE TABLE `u_user` (
  `user_id` bigint(11) unsigned NOT NULL AUTO_INCREMENT,
  `class_id` int(11) DEFAULT NULL,
  `email` varchar(200) NOT NULL DEFAULT '',
  `password` varchar(5) NOT NULL DEFAULT '',
  `is_student` tinyint(1) NOT NULL DEFAULT '1',
  `verify_confirmed` tinyint(1) NOT NULL DEFAULT '0',
  `verify_send` tinyint(1) NOT NULL DEFAULT '0',
  PRIMARY KEY (`user_id`),
  KEY `relation` (`class_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

LOCK TABLES `u_user` WRITE;
/*!40000 ALTER TABLE `u_user` DISABLE KEYS */;

INSERT INTO `u_user` (`user_id`, `class_id`, `email`, `password`, `is_student`, `verify_confirmed`, `verify_send`)
VALUES
	(1,1,'whoami@gmail.com','fool',1,0,0),
	(2,1,'info@hu.nl','',1,0,0),
	(3,5,'dow@gmail.com','',1,0,0),
	(4,5,'john@gmail.com','',1,0,0);

/*!40000 ALTER TABLE `u_user` ENABLE KEYS */;
UNLOCK TABLES;



/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
