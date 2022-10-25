-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Oct 25, 2022 at 09:42 PM
-- Server version: 10.4.25-MariaDB
-- PHP Version: 8.1.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `wassceverse`
--

-- --------------------------------------------------------

--
-- Table structure for table `registered_schools`
--

CREATE TABLE `registered_schools` (
  `id` int(11) NOT NULL COMMENT 'TRIAL',
  `school_name` longtext NOT NULL COMMENT 'TRIAL',
  `location` longtext NOT NULL COMMENT 'TRIAL',
  `country` longtext NOT NULL COMMENT 'TRIAL',
  `school_code` int(11) NOT NULL COMMENT 'TRIAL',
  `school_logo` longblob DEFAULT NULL COMMENT 'TRIAL',
  `school_email` longtext DEFAULT NULL COMMENT 'TRIAL',
  `password` longtext DEFAULT NULL COMMENT 'TRIAL',
  `verified` int(11) NOT NULL DEFAULT 0 COMMENT 'TRIAL',
  `trial475` char(1) DEFAULT NULL COMMENT 'TRIAL'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='TRIAL';

--
-- Dumping data for table `registered_schools`
--

INSERT INTO `registered_schools` (`id`, `school_name`, `location`, `country`, `school_code`, `school_logo`, `school_email`, `password`, `verified`, `trial475`) VALUES
(1, 'Presbyterian Boys\' Secondary School', 'Legon, Accra', 'Ghana', 1, NULL, 'presbyterianboys@gmail.com', 'admin', 0, 'T'),
(2, 'Achimota School', 'Achimota', 'Ghana', 2, NULL, 'achimota@gmail.com', NULL, 0, 'T'),
(3, 'Wesley Girls High School', 'Cape Coast', 'Ghana', 3, NULL, 'wesleygirls@gmail.com', NULL, 0, 'T'),
(4, 'Prempeh College', 'Kumasi', 'Ghana', 4, NULL, 'prempeh@gmail.com', 'hello', 0, 'T'),
(5, 'Holy Child', 'Cape Coast', 'Ghana', 5, NULL, 'holychild@gmail.com', NULL, 0, 'T'),
(6, 'Robo.School', 'nowhere', 'Ghana', 14, NULL, 'school@robo.com', 'admin.admin', 1, 'T');

-- --------------------------------------------------------

--
-- Table structure for table `registered_students`
--

CREATE TABLE `registered_students` (
  `id` int(11) NOT NULL COMMENT 'TRIAL',
  `surname` longtext NOT NULL COMMENT 'TRIAL',
  `first_name` longtext NOT NULL COMMENT 'TRIAL',
  `other_names` longtext DEFAULT NULL COMMENT 'TRIAL',
  `course` longtext NOT NULL COMMENT 'TRIAL',
  `class` longtext DEFAULT NULL COMMENT 'TRIAL',
  `index_number` longtext NOT NULL COMMENT 'TRIAL',
  `year_completed` longtext NOT NULL COMMENT 'TRIAL',
  `electives` longtext NOT NULL COMMENT 'TRIAL',
  `school` longtext NOT NULL COMMENT 'TRIAL',
  `gender` longtext NOT NULL COMMENT 'TRIAL',
  `parent_contact` longtext NOT NULL COMMENT 'TRIAL',
  `date_of_birth` longtext DEFAULT NULL COMMENT 'TRIAL',
  `signature` longblob DEFAULT NULL COMMENT 'TRIAL',
  `image` longblob DEFAULT NULL COMMENT 'TRIAL',
  `fingerprint` longblob DEFAULT NULL COMMENT 'TRIAL',
  `trial478` char(1) DEFAULT NULL COMMENT 'TRIAL'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='TRIAL';

--
-- Dumping data for table `registered_students`
--

INSERT INTO `registered_students` (`id`, `surname`, `first_name`, `other_names`, `course`, `class`, `index_number`, `year_completed`, `electives`, `school`, `gender`, `parent_contact`, `date_of_birth`, `signature`, `image`, `fingerprint`, `trial478`) VALUES
(1, 'Engelberg', 'Davis', 'Kory', 'General Science', '3 Science 15', '0111010038', '2020', 'Physics, Chemistry, Biology', 'Presbyterian Boy\'s Secondary Schoool', 'Male', '0344279809', '30/05/2003', NULL, 0x20, 0x20, 'T'),
(2, 'Asiedu', 'Prince', 'Kofi', 'General Science', '3 Science 5', '019399209023', '2019', 'E-Math,Physics,Chemistry,E-ICT', 'Presbyterian Boys\' Secondary School', 'male', '+233244276809', '27/02/2004', NULL, NULL, NULL, 'T');

-- --------------------------------------------------------

--
-- Table structure for table `student_details`
--

CREATE TABLE `student_details` (
  `id` int(11) NOT NULL COMMENT 'TRIAL',
  `surname` longtext NOT NULL COMMENT 'TRIAL',
  `first_name` longtext NOT NULL COMMENT 'TRIAL',
  `other_names` longtext DEFAULT NULL COMMENT 'TRIAL',
  `course` longtext NOT NULL COMMENT 'TRIAL',
  `class` longtext DEFAULT NULL COMMENT 'TRIAL',
  `index_number` longtext NOT NULL COMMENT 'TRIAL',
  `year_completed` longtext NOT NULL COMMENT 'TRIAL',
  `electives` longtext NOT NULL COMMENT 'TRIAL',
  `school` longtext NOT NULL COMMENT 'TRIAL',
  `gender` longtext NOT NULL COMMENT 'TRIAL',
  `parent_contact` longtext NOT NULL COMMENT 'TRIAL',
  `date_of_birth` longtext DEFAULT NULL COMMENT 'TRIAL',
  `signature` longblob DEFAULT NULL COMMENT 'TRIAL',
  `image` longblob DEFAULT NULL COMMENT 'TRIAL',
  `fingerprint` longblob DEFAULT NULL COMMENT 'TRIAL',
  `trial481` char(1) DEFAULT NULL COMMENT 'TRIAL'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='TRIAL';

--
-- Dumping data for table `student_details`
--

INSERT INTO `student_details` (`id`, `surname`, `first_name`, `other_names`, `course`, `class`, `index_number`, `year_completed`, `electives`, `school`, `gender`, `parent_contact`, `date_of_birth`, `signature`, `image`, `fingerprint`, `trial481`) VALUES
(1, 'Debrah', 'Derrick', 'Kofi', 'General Science', '3 Science 1', '0111010038', '2019', 'E-Math,Physics,Chemistry,Biology', 'Presbyterian Boys\' Secondary School', 'Male', '+233244276809', '21/02/2004', NULL, NULL, NULL, 'T'),
(3, 'Allan', 'Barry', 'Speed Force', 'General Science', '3 Science 21', '00123456789', '2019', 'Chemistry,Biology,Business Management,Financial Accounting', 'Presbyterian Boys\' Secondary School', 'Male', '+233244276809', '12/08/2003', NULL, NULL, NULL, 'T'),
(5, 'Asem', 'Flex', '', 'General Science', '3 Business 6', '0102050002', '2019', 'Business Management,Elective Mathematics,Economics,Financial Accounting', 'Presbyterian Boys\' Secondary School', 'Male', '+233244789653', '01/01/01', NULL, NULL, NULL, 'T'),
(6, 'Biden', 'Joe', '', 'General Science', '3 Science 6', '0020011023', '', 'Biology,Chemistry,Elective ICT,Elective Mathematics', 'Presbyterian Boys\' Secondary School', 'Male', '+1 344-7683', '01/01/01', NULL, NULL, NULL, 'T'),
(7, 'Doe', 'John', 'Kofi', 'Business', '', '', '', 'Business Management,Principles of Costing,Elective Mathematics,Financial Accounting', 'Presbyterian Boys\' Secondary School', 'Male', '+233 (0) 65435674', '01/01/01', NULL, NULL, NULL, 'T');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `registered_schools`
--
ALTER TABLE `registered_schools`
  ADD PRIMARY KEY (`id`,`school_code`);

--
-- Indexes for table `registered_students`
--
ALTER TABLE `registered_students`
  ADD PRIMARY KEY (`id`,`index_number`(255));

--
-- Indexes for table `student_details`
--
ALTER TABLE `student_details`
  ADD PRIMARY KEY (`id`,`index_number`(255));

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `registered_schools`
--
ALTER TABLE `registered_schools`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'TRIAL', AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `registered_students`
--
ALTER TABLE `registered_students`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'TRIAL', AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `student_details`
--
ALTER TABLE `student_details`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'TRIAL', AUTO_INCREMENT=8;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
