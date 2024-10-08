CREATE SCHEMA IF NOT EXISTS `blog` DEFAULT CHARACTER SET utf8 ;
USE `blog` ;

-- -----------------------------------------------------
-- Table `blog`.`usuarios`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `blog`.`usuarios` (
  `usuario_id` INT NOT NULL,
  `nome` VARCHAR(100) NOT NULL,
  `email` VARCHAR(100) NOT NULL,
  `senha` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`usuario_id`),
  UNIQUE INDEX `Email_UNIQUE` (`email` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `blog`.`postagens`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `blog`.`postagens` (
  `postagem_id` INT NOT NULL,
  `titulo` VARCHAR(200) NOT NULL,
  `conteudo` TEXT NOT NULL,
  `data_postagem` DATETIME NOT NULL,
  `usuarios_usuario_id` INT NOT NULL,
  PRIMARY KEY (`postagem_id`),
  INDEX `fk_Postagens_Usuarios1_idx` (`usuarios_usuario_id` ASC) VISIBLE,
  CONSTRAINT `fk_Postagens_Usuarios1`
    FOREIGN KEY (`usuarios_usuario_id`)
    REFERENCES `blog`.`usuarios` (`usuario_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `blog`.`mensagens`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `blog`.`mensagens` (
  `mensagem_id` INT NOT NULL,
  `conteudo` TEXT NOT NULL,
  `data_mensagem` DATETIME NOT NULL,
  `usuarios_usuario_id` INT NOT NULL,
  `postagens_postagem_id` INT NOT NULL,
  PRIMARY KEY (`mensagem_id`),
  INDEX `fk_Mensagens_Usuarios_idx` (`usuarios_usuario_id` ASC) VISIBLE,
  INDEX `fk_Mensagens_Postagens1_idx` (`postagens_postagem_id` ASC) VISIBLE,
  CONSTRAINT `fk_Mensagens_Usuarios`
    FOREIGN KEY (`usuarios_usuario_id`)
    REFERENCES `blog`.`usuarios` (`usuario_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Mensagens_Postagens1`
    FOREIGN KEY (`postagens_postagem_id`)
    REFERENCES `blog`.`postagens` (`postagem_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;