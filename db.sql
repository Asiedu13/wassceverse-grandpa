-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 02, 2022 at 11:00 PM
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
  `id` int(11) NOT NULL,
  `school_name` text NOT NULL,
  `location` text NOT NULL,
  `country` text NOT NULL,
  `school_code` text DEFAULT NULL,
  `school_logo` blob NOT NULL,
  `school_email` text NOT NULL,
  `password` text NOT NULL,
  `verified` int(11) NOT NULL DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `registered_schools`
--

INSERT INTO `registered_schools` (`id`, `school_name`, `location`, `country`, `school_code`, `school_logo`, `school_email`, `password`, `verified`) VALUES
(1, 'Presbyterian Boys\' Secondary School', 'Greater Accra Region, Legon', 'Ghana', NULL, '', 'presbyterianboys@gmail.com', '14213d876a8cbfc849634312a39310fe', 0);

-- --------------------------------------------------------

--
-- Table structure for table `registered_students`
--

CREATE TABLE `registered_students` (
  `id` int(11) NOT NULL,
  `student` int(11) NOT NULL,
  `wassce_index_number` text DEFAULT NULL,
  `wassce_year` int(11) DEFAULT NULL,
  `cleared` int(11) NOT NULL DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `registered_students`
--

INSERT INTO `registered_students` (`id`, `student`, `wassce_index_number`, `wassce_year`, `cleared`) VALUES
(2, 4, NULL, NULL, 0);

-- --------------------------------------------------------

--
-- Table structure for table `student_details`
--

CREATE TABLE `student_details` (
  `id` int(11) NOT NULL,
  `school` int(11) NOT NULL,
  `surname` text NOT NULL,
  `first_name` text NOT NULL,
  `other_names` text NOT NULL,
  `course` text NOT NULL,
  `class` text NOT NULL,
  `index_number` text NOT NULL,
  `electives` text NOT NULL,
  `gender` int(11) NOT NULL,
  `parent_contact` text NOT NULL,
  `date_of_birth` text NOT NULL,
  `signature` blob NOT NULL,
  `image` blob NOT NULL,
  `fingerprint` blob NOT NULL,
  `bece_year` int(11) NOT NULL,
  `student_key` varchar(6) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `student_details`
--

INSERT INTO `student_details` (`id`, `school`, `surname`, `first_name`, `other_names`, `course`, `class`, `index_number`, `electives`, `gender`, `parent_contact`, `date_of_birth`, `signature`, `image`, `fingerprint`, `bece_year`, `student_key`) VALUES
(4, 1, 'Asiedu', 'Prince', 'Kofi', 'General Science', '3 Science 2', '0102034005', 'Chemistry,Physics,Elective ICT,Elective Mathematics', 0, '+233 (0) 2443455673', '21/01/2004', '', '', '', 2019, NULL);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `registered_schools`
--
ALTER TABLE `registered_schools`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `registered_students`
--
ALTER TABLE `registered_students`
  ADD PRIMARY KEY (`id`),
  ADD KEY `Student` (`student`);

--
-- Indexes for table `student_details`
--
ALTER TABLE `student_details`
  ADD PRIMARY KEY (`id`),
  ADD KEY `SCHOOL` (`school`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `registered_schools`
--
ALTER TABLE `registered_schools`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `registered_students`
--
ALTER TABLE `registered_students`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `student_details`
--
ALTER TABLE `student_details`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `registered_students`
--
ALTER TABLE `registered_students`
  ADD CONSTRAINT `registered_students_ibfk_1` FOREIGN KEY (`student`) REFERENCES `student_details` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `student_details`
--
ALTER TABLE `student_details`
  ADD CONSTRAINT `student_details_ibfk_1` FOREIGN KEY (`school`) REFERENCES `registered_schools` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
