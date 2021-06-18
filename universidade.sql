DROP SCHEMA universidade Cascade;
CREATE SCHEMA universidade;
SET search_path TO universidade;

CREATE TABLE faculdade(
  nomeBloco varchar(3),
  siglaFaculdade varchar(8),
  numeroProfessores int,
  numeroAlunos int, 
  orcamento float,

  primary key (siglaFaculdade),
  unique (nomeBloco)
);


CREATE TABLE aluno(
  telefone varchar(15),
  cra float not null,
  idAluno int,
  dataNascimento date,
  nomeAluno varchar(50),
  
  primary key (idAluno),
  unique (nomeAluno)
);


CREATE TABLE professor(
  idProfessor int,
  nomeProfessor varchar(50),
  dataNascimento date,
  salario float,

  primary key (idProfessor)
);


CREATE TABLE disciplina(
  nomeDisciplina varchar(50),
  siglaDisciplina varchar(8),
  numeroCreditos int,
  idResponsavel int,
  siglaSuperDisciplina varchar(8),  --Pré-requisito

  foreign key (siglaSuperDisciplina) REFERENCES disciplina(siglaDisciplina),
  primary key (siglaDisciplina),
  foreign key (idResponsavel) REFERENCES professor(idProfessor)
);


CREATE TABLE turma(
  nomeTurma varchar(20),
  ano int,
  semestre int,
  idTurma int, 
  lugar varchar(20),

  primary key (idTurma)
);

CREATE TABLE sala(
  nomeBloco varchar(3),
  numeroSala int,
  capacidadeSala int,

  foreign key (nomeBloco) REFERENCES faculdade(nomeBloco)
);