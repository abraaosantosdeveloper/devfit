create database devfit;
use devfit;

create table if not exists funcionario
(
id int not null auto_increment,
cpf varchar(11) not null,
nome varchar(80) not null,
nascimento date not null,
cargo varchar(50) not null,
especialidade varchar(50) not null,
contato varchar(11),
salario decimal(10, 2) not null,
data_contratacao date,
primary key(id)
);

create table if not exists plano(
id int not null auto_increment,
valor decimal(10, 2) not null,
periodo varchar(11) not null,
descricao varchar(30) not null,
primary key(id)
);

create table if not exists turma(
id int not null auto_increment,
horario time,

primary key(id)
);

create table if not exists aluno
(
id int not null auto_increment,
nome varchar(80) not null,
cpf varchar(11),
nascimento date not null,
endereco varchar(100),
contato varchar(11),
turma int not null,
plano int,

primary key(id),
foreign key(turma) references turma(id),
foreign key(plano) references plano(id)
);

create table if not exists fornecedor(
id int not null auto_increment,
nome varchar(80) not null,
endereco varchar(100) not null,
telefone varchar(11),
email varchar(80),
vigencia_contrato date,

primary key(id)
);

create table if not exists equipamento(
id int not null auto_increment,
descricao varchar(75) not null,
preco decimal(10, 2),
id_fornecedor int not null,
ultima_manutencao date,
proxima_manutencao date,
modalidade varchar(40) not null,
data_compra date,

primary key(id),
foreign key(id_fornecedor) references fornecedor(id)
);

create table usuario
(
id int not null auto_increment,
nome_usuario varchar(20) not null,
senha varchar(16) not null

);
