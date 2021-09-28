-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `wolftrack` DEFAULT CHARACTER SET utf8 ;
USE `wolftrack` ;

-- -----------------------------------------------------
-- Table `wolftrack`.`user`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `wolftrack`.`user` ;

CREATE TABLE IF NOT EXISTS `wolftrack`.`user` (
  `user_id` INT NOT NULL AUTO_INCREMENT,
  `email` VARCHAR(45) NOT NULL,
  `full_name` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`user_id`),
  UNIQUE INDEX `email_UNIQUE` (`email` ASC) VISIBLE,
  UNIQUE INDEX `first_name_UNIQUE` (`full_name` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `wolftrack`.`user_login`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `wolftrack`.`user_login` ;

CREATE TABLE IF NOT EXISTS `wolftrack`.`user_login` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `user_id` INT NOT NULL,
  `password` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `user_id_idx` (`user_id` ASC) VISIBLE,
    FOREIGN KEY (`user_id`)
    REFERENCES `wolftrack`.`user` (`user_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `wolftrack`.`user_details`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `wolftrack`.`user_details` ;

CREATE TABLE IF NOT EXISTS `wolftrack`.`user_details` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `user_id` INT NOT NULL,
  `linkedin_link` VARCHAR(45) NULL,
  `github_link` VARCHAR(45) NULL,
  `profile_link` VARCHAR(45) NULL,
  PRIMARY KEY (`id`),
  INDEX `user_id_idx` (`user_id` ASC) VISIBLE,
    FOREIGN KEY (`user_id`)
    REFERENCES `wolftrack`.`user` (`user_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `wolftrack`.`company`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `wolftrack`.`company` ;

CREATE TABLE IF NOT EXISTS `wolftrack`.`company` (
  `company_id` INT NOT NULL AUTO_INCREMENT,
  `company_name` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`company_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `wolftrack`.`roles`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `wolftrack`.`roles` ;

CREATE TABLE IF NOT EXISTS `wolftrack`.`roles` (
  `role_id` INT NOT NULL AUTO_INCREMENT,
  `role` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`role_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `wolftrack`.`recruiter`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `wolftrack`.`recruiter` ;

CREATE TABLE IF NOT EXISTS `wolftrack`.`recruiter` (
  `recruiter_id` INT NOT NULL AUTO_INCREMENT,
  `company_id` INT NOT NULL,
  `name` VARCHAR(45) NOT NULL,
  `email` VARCHAR(45) NULL,
  `link` VARCHAR(45) NULL,
  PRIMARY KEY (`recruiter_id`),
  INDEX `company_id_idx` (`company_id` ASC) VISIBLE,
    FOREIGN KEY (`company_id`)
    REFERENCES `wolftrack`.`company` (`company_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `wolftrack`.`application`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `wolftrack`.`application` ;

CREATE TABLE IF NOT EXISTS `wolftrack`.`application` (
  `application_id` INT NOT NULL AUTO_INCREMENT,
  `user_id` INT NOT NULL,
  `company_id` INT NOT NULL,
  `role_id` INT NOT NULL,
  `recruiter_id` INT NULL,
  `application_date` TIMESTAMP NOT NULL,
  `job_description` VARCHAR(100) NULL,
  `salary` FLOAT NULL,
  `location` VARCHAR(45) NOT NULL,
  `imortant_links` VARCHAR(45) NULL,
  `status` ENUM("TO_DO", "APPLIED", "IN_PROCESS", "ACCEPTED", "DECLINED") NOT NULL,
  `due_date` TIMESTAMP NOT NULL,
  PRIMARY KEY (`application_id`),
  INDEX `user_id_idx` (`user_id` ASC) VISIBLE,
  INDEX `role_id_idx` (`role_id` ASC) VISIBLE,
  INDEX `company_id_idx` (`company_id` ASC) VISIBLE,
  INDEX `recruiter_id_idx` (`recruiter_id` ASC) VISIBLE,
    FOREIGN KEY (`user_id`)
    REFERENCES `wolftrack`.`user` (`user_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
    FOREIGN KEY (`role_id`)
    REFERENCES `wolftrack`.`roles` (`role_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
    FOREIGN KEY (`company_id`)
    REFERENCES `wolftrack`.`company` (`company_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
    FOREIGN KEY (`recruiter_id`)
    REFERENCES `wolftrack`.`recruiter` (`recruiter_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
