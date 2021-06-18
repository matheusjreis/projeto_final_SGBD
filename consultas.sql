-- Consulta 1
SELECT DISTINCT professor.nomeProfessor, disciplina.nomeDisciplina
  FROM professor, disciplina
      WHERE professor.idProfessor = disciplina.idResponsavel AND
            disciplina.numeroCreditos>2;

-- Consulta 2
SELECT sala.numeroSala, sala.nomeBlocoFROM sala NATURAL JOIN faculdade
  WHERE faculdade.numeroAlunos>2000;


-- Consulta 3
SELECT f_1.siglaFaculdadeFROM faculdade as f_1
  WHERE EXISTS 
    (SELECT sala
        FROM sala
          WHERE sala.nomeBloco = f_1.nomeBloco AND
                sala.capacidadeSala>35);

------------------------------------------------------------------------------

-- Consulta 1
SELECT professor.nomeProfessor, disciplina.nomeDisciplina
  FROM professor INNER JOIN disciplina
    ON professor.idProfessor = disciplina.idResponsavel;

-- Consulta 2
SELECT sala.numeroSala, faculdade.sigla
  FROM sala NATURAL JOIN faculdade
    WHERE sala.numeroSala BETWEEN 100 AND 200;

-- Consulta 3
SELECT sala.numeroSala, sala.nomeBloco, min(sala.capacidadeSala) as menorCapacidade
  FROM sala
    GROUP BY sala.numeroSala, sala.nomeBloco

------------------------------------------------------------------------------

-- Consulta Recursiva
WITH RECURSIVE tSup (nivel, siglaSuperDisciplina, siglaDisciplina, nomeDisciplina) AS 
  (SELECT 1, root.siglaSuperDisciplina, root.siglaDisciplina, root.nomeDisciplina
    FROM Disciplina root
      UNION ALL
  SELECT nivel+1, child.siglaSuperDisciplina, child.siglaDisciplina, child.nomeDisciplina
    FROM tSup parent, Disciplina child
      WHERE parent.siglaDisciplina = child.siglaSuperDisciplina
  )
  SELECT DISTINCT nivel, siglaSuperDisciplina, siglaDisciplina, nomeDisciplina
    FROM tSup;


-- Visão
CREATE VIEW vmatematicos 
  AS 
  SELECT professor.nomeProfessor, professor.dataNascimento, disciplina.nomeDisciplina
    FROM professor, disciplinaWHERE professor.idProfessor = disciplina.idResponsavel AND
      disciplina.nomeDisciplina LIKE'Cálculo%';

SELECT * FROM vmatematicos;