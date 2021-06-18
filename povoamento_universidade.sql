SET search_path TO universidade;

--faculdade 
INSERT INTO faculdade VALUES ('3B', 'FACOM', 180, 3200, 4000000.00);
INSERT INTO faculdade VALUES ('5E', 'DLA', 190, 4200, 3000000.00);
INSERT INTO faculdade VALUES ('3C', 'FEST', 98, 900, 2500000.00);
INSERT INTO faculdade VALUES ('1R', 'FAMAT', 210, 1800, 3800000.00);
INSERT INTO faculdade VALUES ('5R', 'FAMED', 200, 2000, 18000000.00);
INSERT INTO faculdade VALUES ('5D', 'FADIR', 300, 5000, 38000000.00);


-- alunos
INSERT INTO aluno VALUES ('34988252674', 60, 1, '25-10-1985', 'Lebron James', 'FACOM');
INSERT INTO aluno VALUES ('34988252673', 82, 2, '26-08-1981', 'Steph Curry', 'DLA');
INSERT INTO aluno VALUES ('34988252672', 75, 3, '27-07-1981', 'Lionel Messi', 'FEST');
INSERT INTO aluno VALUES ('34988252671', 93, 4, '28-06-1986', 'Diego Ribas', 'FAMAT');
INSERT INTO aluno VALUES ('34988252670', 80, 5, '29-05-1999', 'Vinicius Jr', 'FAMED');

-- turma
INSERT INTO turma VALUES ('Computação 61', 2021, 6, 40,'3B');
INSERT INTO turma VALUES ('Letras 81', 2021, 8, 41,'5E');
INSERT INTO turma VALUES ('Estatística 17', 2021, 4, 42,'3C');
INSERT INTO turma VALUES ('Matemática 98', 2021, 7, 43,'1R');
INSERT INTO turma VALUES ('Medicina 108', 2021, 2, 44,'5R');
INSERT INTO turma VALUES ('Direito 201', 2021, 2, 45,'5D');

-- professor 
INSERT INTO professor VALUES (30, 'Kobe Bryant','27-05-1980', 17000.00, 'FACOM', 40);
INSERT INTO professor VALUES (31, 'Ronaldo Nazário','16-06-1980', 8000.00, 'DLA', 41);
INSERT INTO professor VALUES (32, 'Johan Cruyff','03-07-1947', 10000.00, 'FEST', 42);
INSERT INTO professor VALUES (33, 'Francesco Totti','17-08-1976', 15000.00, 'FAMAT', 43);
INSERT INTO professor VALUES (34, 'Andres Iniesta','23-03-1984', 18000.00, 'FAMED',44);
INSERT INTO professor VALUES (35, 'Dwayne Wade','17-01-1982', 13000.00, 'FAMAT', 41);
INSERT INTO professor VALUES (36, 'Mariana Castro','17-01-1990', 25000.00, 'FADIR', 45);


-- diretor
INSERT INTO diretor VALUES (30, 'FACOM');
INSERT INTO diretor VALUES (31, 'DLA');
INSERT INTO diretor VALUES (32, 'FEST');
INSERT INTO diretor VALUES (33, 'FAMAT');
INSERT INTO diretor VALUES (34, 'FAMED');
INSERT INTO diretor VALUES (35, 'FADIR');



-- disciplina 
INSERT INTO disciplina VALUES ('Estrutura de Dados 1', 'ED1', 2, 31, NULL, 'FACOM');
INSERT INTO disciplina VALUES ('Cálculo I', 'C1', 2, 35, NULL, 'FAMAT');
INSERT INTO disciplina VALUES ('Programação Funcional', 'PF', 3, 34, 'ED1', 'FACOM');
INSERT INTO disciplina VALUES ('Teoria da Computação', 'TC', 5, 30, 'ED1', 'FACOM');
INSERT INTO disciplina VALUES ('Cálculo II', 'C2', 3, 32,'C1', 'FAMAT');
INSERT INTO disciplina VALUES ('Inteligência Artificial', 'IA', 4, 33,'PF','FACOM');
INSERT INTO disciplina VALUES ('Direito e Legislação', 'DL', 1, 36, NULL,'FADIR');

-- sala 
INSERT INTO sala VALUES ('3B', 101, 50);
INSERT INTO sala VALUES ('3C', 202, 40);
INSERT INTO sala VALUES ('5E', 403, 30);
INSERT INTO sala VALUES ('1R', 104, 30);
INSERT INTO sala VALUES ('5R', 505, 35);