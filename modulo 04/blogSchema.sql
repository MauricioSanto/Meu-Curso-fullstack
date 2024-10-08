CREATE SCHEMA IF NOT EXISTS `blog` DEFAULT CHARACTER SET utf8 ;
USE `blog` ;

-- -----------------------------------------------------
-- Table `blog`.`Usuarios`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `blog`.`Usuarios` (
  `Usuario_id` INT NOT NULL,
  `Nome` VARCHAR(100) NOT NULL,
  `Email` VARCHAR(100) NOT NULL,
  `Senha` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`Usuario_id`),
  UNIQUE INDEX `Email_UNIQUE` (`Email` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `blog`.`Postagens`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `blog`.`Postagens` (
  `Postagem_id` INT NOT NULL,
  `Titulo` VARCHAR(200) NOT NULL,
  `Conteudo` TEXT NOT NULL,
  `Data_Postagem` DATETIME NOT NULL,
  `Usuarios_idUsuarios` INT NOT NULL,
  PRIMARY KEY (`Postagem_id`),
  INDEX `fk_Postagens_Usuarios1_idx` (`Usuarios_idUsuarios` ASC) VISIBLE,
  CONSTRAINT `fk_Postagens_Usuarios1`
    FOREIGN KEY (`Usuarios_idUsuarios`)
    REFERENCES `blog`.`Usuarios` (`Usuario_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `blog`.`Mensagens`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `blog`.`Mensagens` (
  `Mensagem_id` INT NOT NULL,
  `Conteudo` TEXT NOT NULL,
  `Data_Mensagem` DATETIME NOT NULL,
  `Usuarios_Usuario_id` INT NOT NULL,
  `Postagens_Postagem_id` INT NOT NULL,
  PRIMARY KEY (`Mensagem_id`),
  INDEX `fk_Mensagens_Usuarios_idx` (`Usuarios_Usuario_id` ASC) VISIBLE,
  INDEX `fk_Mensagens_Postagens1_idx` (`Postagens_Postagem_id` ASC) VISIBLE,
  CONSTRAINT `fk_Mensagens_Usuarios`
    FOREIGN KEY (`Usuarios_Usuario_id`)
    REFERENCES `blog`.`Usuarios` (`Usuario_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Mensagens_Postagens1`
    FOREIGN KEY (`Postagens_Postagem_id`)
    REFERENCES `blog`.`Postagens` (`Postagem_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;