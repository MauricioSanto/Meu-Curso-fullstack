create database PetShop;

use PetShop;

create table Sexo(
    id integer primary key auto_increment,
    Sexo  VARCHAR(100) not null,
    created_at TIMESTAMP null,
    updated_at TIMESTAMP null
);

create table Cliente(
    id integer primary key auto_increment,
    id_sexo integer not null,
    foreign key ( id_sexo) references Sexo (id),
    nome VARCHAR(100) not null,
    Sobrenome VARCHAR(100) not null,
    rua VARCHAR not null,
    Bairro VARCHAR not null,
    Numero_Casa VARCHAR not null,
    Cep INTEGER not null,
    Cidade VARCHAR not null,
    Telefone VARCHAR not null,
    Celular VARCHAR not null,
    Idade INTEGER  not null,
    ID_Admin  boolean  not null,
    email VARCHAR  not null,
    Usuario VARCHAR  not null,
    Senha VARCHAR  not null,
    
);

create table Porte(
    id integer primary key auto_increment,
    porte VARCHAR not nul,
    created_at TIMESTAMP null,
    updated_at TIMESTAMP null
);

create table Servico(
    id integer primary key auto_increment,
    Servico VARCHAR not null,
    created_at TIMESTAMP null,
    updated_at TIMESTAMP null
);

create table Atendente(
    id integer primary key auto_increment,
    atendente VARCHAR not null,
    DispInicio time not null,
    DispFinal time not null,
    created_at TIMESTAMP null,
    updated_at TIMESTAMP null
);

create table DisponibilidadeAgendamento(
    id integer primary key auto_increment,
    DispInicial time not null,
    DispFinal time not null,
    created_at TIMESTAMP null,
    updated_at TIMESTAMP null
);

create table Agendamento(
    id integer primary key auto_increment,
    id_Animal integer not null,
    foreign key (id_Animal) references Animal (id),
    id_Servico integer not null,
    foreign key (id_Servico) references Servico (id),
    id_Atendente integer not null,
    foreign key (id_Atendente) references Atendente (id),
    Data DATE not null,
    Hora_agend_Inicial time not null,
    Hora_agend_Final time not null,
    estatus boolean(1) not null,
    created_at TIMESTAMP null,
    updated_at TIMESTAMP null
);

create table Animal(
    id integer primary key auto_increment,
    id_porte integer not null,
    foreign key (id_porte) references Porte (id),
    id_Sexo integer not null,
    foreign key (id_Sexo) references Sexo (id),
    id_Cliente integer not null,
    foreign key (id_Cliente) references Cliente (id),
    animal VARCHAR not null,
    Raca VARCHAR not null,
    Data_Nascimento DATE not null,
    Cor_Pelagem VARCHAR not null,
    created_at TIMESTAMP null,
    updated_at TIMESTAMP null
);