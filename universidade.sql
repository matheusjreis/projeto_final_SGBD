-- DROP SCHEMA universidade Cascade;
CREATE SCHEMA universidade;
SET search_path TO universidade;

CREATE TABLE faculdade(
  nomeBloco varchar(3),
  siglaFaculdade varchar(8),
  numeroProfessores int,
  numeroAlunos int, 
  orcamento float,
  idDiretor int,

  -- Disciplinas oferecidas 
  idDisciplina int,

  PRIMARY KEY (siglaFaculdade),
  UNIQUE (nomeBloco)
);


CREATE TABLE aluno(
  telefone varchar(15),
  cra float not null,
  idAluno int,
  dataNascimento date,
  nomeAluno varchar(50),
  siglaFaculdade varchar(8),

  FOREIGN KEY (siglaFaculdade) REFERENCES faculdade(siglaFaculdade),  
  PRIMARY KEY (idAluno),
  UNIQUE (nomeAluno)
);


CREATE TABLE professor(
  idProfessor int,
  nomeProfessor varchar(50),
  dataNascimento date,
  salario float,
  siglaFaculdade varchar(8),
  idTurma int,

  FOREIGN KEY (siglaFaculdade) REFERENCES faculdade(siglaFaculdade),
  PRIMARY KEY (idProfessor)
);


CREATE TABLE disciplina(
  nomeDisciplina varchar(50),
  siglaDisciplina varchar(8),
  numeroCreditos int,
  idResponsavel int,  
  siglaSuperDisciplina varchar(8),  --Pré-requisito
  siglaFaculdade varchar(8),
  
  FOREIGN KEY (siglaFaculdade) REFERENCES faculdade(siglaFaculdade),
  FOREIGN KEY (siglaSuperDisciplina) REFERENCES disciplina(siglaDisciplina),
  PRIMARY KEY (siglaDisciplina),
  FOREIGN KEY (idResponsavel) REFERENCES professor(idProfessor)
);


CREATE TABLE turma(
  nomeTurma varchar(20),
  ano int,
  semestre int,
  idTurma int, 
  lugar varchar(20),

  FOREIGN KEY (lugar) REFERENCES faculdade(nomeBloco),
  PRIMARY KEY (idTurma)
);


CREATE TABLE sala(
  nomeBloco varchar(3),
  numeroSala int,
  capacidadeSala int,
  
  FOREIGN KEY (nomeBloco) REFERENCES faculdade(nomeBloco)
);


-------- ALTER TABLES --------

ALTER TABLE faculdade
        ADD FOREIGN KEY (idDiretor) REFERENCES professor(idProfessor);

ALTER TABLE professor
        ADD FOREIGN KEY (idTurma) REFERENCES turma(idTurma);