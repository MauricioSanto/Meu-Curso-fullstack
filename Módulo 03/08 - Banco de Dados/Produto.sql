create database Venda_Produto;

use Venda_Produto;

create table Produto_similar(
    id_produto integer primary key auto_increment,
    id_produto_similar integer not nul,
    foreign key ( id_produto_similar) references Produto_similar(id)
    created_at TIMESTAMP null,
    updated_at TIMESTAMP null
);

create table Marca(
    id integer primary key auto_increment,
    descricao Text not null,
    created_at TIMESTAMP null,
    updated_at TIMESTAMP null
);

create table Produto(
    id_produto integer primary key auto_increment,
    foreign key (id_produto) not null, 
    codigo VARCHAR(100) not null,
    descricao Text not null,
    id_SubCategoria INTEGER NOT NULL,
    id_Marca INTEGER NOT NULL,
    id_Unidade_Medida integer not null,
    foreign key (id_SubCategoria) references SubCategoria (id),
    foreign key (id_Marca) references Marca (id),
    foreign key ( id_Unidade_Medida) references Unidade_Medida (id),
    especificacao_tecnica text not null,
    estatus tinyint(1) not null,
    peso_bruto VARCHAR(100) not null,
    peso_liquido VARCHAR(100) not null,
    QTD_Mult VARCHAR(100) not null,
    QTD_Min VARCHAR(100) not null,
    COD_BARRA VARCHAR(100) not null,
    created_at TIMESTAMP null,
    updated_at TIMESTAMP null
);

create table Preco_Venda(
    id integer primary key auto_increment,
    id_produto INTEGER not null,
    foreign key ( id_produto) references Produto (id),
    Preco_venda  VARCHAR(100) not null,
    Data_validade_inicial VARCHAR(200) not null,
    Data_validade_final VARCHAR(200) not null,
    created_at TIMESTAMP null,
    updated_at TIMESTAMP null
);

create table Unidade_Medida(
    id_Unidade_Medida integer primary key auto_increment,
    foreign key ( id_Unidade_Medida ) references Unidade_Medida (id),
    descricao Text not null,
    id_produto INTEGER not null,
    foreign key ( id_produto) references Produto (id),
    created_at TIMESTAMP null,
    updated_at TIMESTAMP null
);

create table Departamento(
    id_departamento integer primary key auto_increment,
    descricao Text not null,
    created_at TIMESTAMP null,
    updated_at TIMESTAMP null
);

create table Categoria(
    id_Categoria integer primary key auto_increment,
    descricao Text not null,
    id_departamento integer not null,
    foreign key (id_departamento) references Departamento (id),
    created_at TIMESTAMP null,
    updated_at TIMESTAMP null
);

create table SubCategoria(
    id_SubCategoria integer primary key auto_increment,
    descricao Text not null,
    id_Categoria integer not null,
    foreign key (id_Categoria) references Categoria (id),
    created_at TIMESTAMP null,
    updated_at TIMESTAMP null
);