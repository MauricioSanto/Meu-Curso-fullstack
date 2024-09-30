create database sistema ;

use sistema;

create table Contato(
    id integer primary key auto_increment,
    telefone VARCHAR(100) not null,
    email VARCHAR(100) not null,
    created_at TIMESTAMP null,
    updated_at TIMESTAMP null
);

create table Empresa(
    id integer primary key auto_increment,
    razao_social VARCHAR(100) not null,
    cnpj VARCHAR(100) not null,
    created_at TIMESTAMP null,
    updated_at TIMESTAMP null
);

create table Servico(
    id integer primary key auto_increment,
    tipo VARCHAR(100) not null,
    valor DECIMAL(8,2) not null,
    empresa_id INTEGER NOT NULL,
    categoria_id INTEGER NOT NULL,
    foreign key (empresa_id) references Empresa (id)
    foreign key (categoria_id) references categoria (id)
    created_at TIMESTAMP null,
    updated_at TIMESTAMP null
);

create table Clientes(
    id integer primary key auto_increment,
    nome VARCHAR(150) not null,
    data_nascimento VARCHAR(100) not null,
    foto  VARCHAR(200) not null,
    created_at TIMESTAMP null,
    updated_at TIMESTAMP null
);

create table Categoria(
    id integer primary key auto_increment,
    tipo VARCHAR(100) not null,
    created_at TIMESTAMP null,
    updated_at TIMESTAMP null
);

create table Produtos(
    id integer primary key auto_increment,
    nome VARCHAR(150) not null,
    valor DECIMAL(8,2) not null,
    descricao Text not null,
    created_at TIMESTAMP null,
    updated_at TIMESTAMP null
);

create table OrdemServico(
    id integer primary key auto_increment,
    empresa_id INTEGER NOT NULL,
    cliente_id INTEGER NOT NULL,
    servico_id INTEGER NOT NULL,
    foreign key (empresa_id) references Empresa (id),
    foreign key (cliente_id) references Clientes (id),
    foreign key (servico_id) references Servico (id),
    data_servico DATE null,
    data_finalizaçao DATE null,
    estatus tinyint(1) not null,
    created_at TIMESTAMP null,
    updated_at TIMESTAMP null
)

