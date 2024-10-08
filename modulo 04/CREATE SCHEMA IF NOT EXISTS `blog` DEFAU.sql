CREATE SCHEMA IF NOT EXISTS `blog` DEFAULT CHARACTER SET utf8 ;
USE `blog` ;

-- -----------------------------------------------------
-- Table `blog`.`usuarios`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `blog`.`usuarios` (
  `id` INT NOT NULL,
  `nome` VARCHAR(100) NOT NULL,
  `email` VARCHAR(100) NOT NULL,
  `senha` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `Email_UNIQUE` (`email` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `blog`.`postagens`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `blog`.`postagens` (
  `id` INT NOT NULL,
  `titulo` VARCHAR(200) NOT NULL,
  `conteudo` TEXT NOT NULL,
  `data_postagem` DATETIME NOT NULL,
  `usuarios_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_postagens_usuarios_idx` (`usuarios_id` ASC) VISIBLE,
  CONSTRAINT `fk_postagens_usuarios`
    FOREIGN KEY (`usuarios_id`)
    REFERENCES `blog`.`usuarios` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `blog`.`mensagens`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `blog`.`mensagens` (
  `id` INT NOT NULL,
  `conteudo` TEXT NOT NULL,
  `data_mensagem` DATETIME NOT NULL,
  `postagens_id` INT NOT NULL,
  `usuarios_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_mensagens_postagens1_idx` (`postagens_id` ASC) VISIBLE,
  INDEX `fk_mensagens_usuarios1_idx` (`usuarios_id` ASC) VISIBLE,
  CONSTRAINT `fk_mensagens_postagens1`
    FOREIGN KEY (`postagens_id`)
    REFERENCES `blog`.`postagens` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_mensagens_usuarios1`
    FOREIGN KEY (`usuarios_id`)
    REFERENCES `blog`.`usuarios` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;
