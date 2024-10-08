CREATE DATABASE blog;

USE blog;

CREATE TABLE Usuarios (
    Usuario_id INT AUTO_INCREMENT PRIMARY KEY,
    Nome VARCHAR(100) NOT NULL,
    Email VARCHAR(100) NOT NULL UNIQUE,
    Senha VARCHAR(255) NOT NULL
);

-- 
CREATE TABLE Postagens (
    Postagem_id INT AUTO_INCREMENT PRIMARY KEY,
    Titulo VARCHAR(255) NOT NULL,
    Conteudo TEXT NOT NULL,
    Data_Postagem date NOT NULL,
    Usuario_id INT,
    FOREIGN KEY (Usuario_id) REFERENCES Usuarios(Usuario_id)
);

CREATE TABLE Mensagens (
    Mensagem_id INT AUTO_INCREMENT PRIMARY KEY,
    Conteudo TEXT NOT NULL,
    Data_Mensagem date NOT NULL,
    Usuario_id INT,
    Postagem_id INT,
    FOREIGN KEY (Usuario_id) REFERENCES Usuarios(Usuario_id),
    FOREIGN KEY (Postagem_id) REFERENCES Postagens(Postagem_id)
);