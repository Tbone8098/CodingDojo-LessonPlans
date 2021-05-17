-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema store_db
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema store_db
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `store_db` DEFAULT CHARACTER SET utf8 ;
USE `store_db` ;

-- -----------------------------------------------------
-- Table `store_db`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `store_db`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(45) NULL,
  `last_name` VARCHAR(45) NULL,
  `created_at` DATETIME NULL DEFAULT now(),
  `updated_at` DATETIME NULL DEFAULT now() on update now(),
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `store_db`.`store`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `store_db`.`store` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NULL,
  `created_at` DATETIME NULL DEFAULT now(),
  `updated_at` DATETIME NULL DEFAULT now() on update now(),
  `user_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_store_users_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_store_users`
    FOREIGN KEY (`user_id`)
    REFERENCES `store_db`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `store_db`.`products`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `store_db`.`products` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NULL,
  `desc` VARCHAR(45) NULL,
  `price` DECIMAL NULL,
  `created_at` DATETIME NULL DEFAULT now(),
  `updated_at` DATETIME NULL DEFAULT now() on update now(),
  `store_id` INT NOT NULL,
  PRIMARY KEY (`id`, `store_id`),
  INDEX `fk_products_store1_idx` (`store_id` ASC) VISIBLE,
  CONSTRAINT `fk_products_store1`
    FOREIGN KEY (`store_id`)
    REFERENCES `store_db`.`store` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `store_db`.`users_shopping_cart`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `store_db`.`users_shopping_cart` (
  `users_id` INT NOT NULL,
  `products_id` INT NOT NULL,
  PRIMARY KEY (`users_id`, `products_id`),
  INDEX `fk_users_has_products_products1_idx` (`products_id` ASC) VISIBLE,
  INDEX `fk_users_has_products_users1_idx` (`users_id` ASC) VISIBLE,
  CONSTRAINT `fk_users_has_products_users1`
    FOREIGN KEY (`users_id`)
    REFERENCES `store_db`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_users_has_products_products1`
    FOREIGN KEY (`products_id`)
    REFERENCES `store_db`.`products` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
