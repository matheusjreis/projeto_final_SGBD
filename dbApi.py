import psycopg2 

dbparameters = {'host':'*' ,'database':'*' ,'user':'*' ,'password':'*'}

def pgconnect():
  conn = None
  try:
    conn = psycopg2.connect(**dbparameters) # connect
  except (Exception, psycopg2.DatabaseError) as error:
    return error
  finally:
    return conn


dbparameters['host'] = '200.131.206.13'
dbparameters['database']='SGBD 2021'
dbparameters['user']='matheus_reis99'
dbparameters['password']='********'

pgconn = pgconnect()
theTable = pgconn.cursor()
theTable.execute("set search_path to universidade")

# i
statement = ''

# Inclusão

# Inclusão 1

print('Insira os dados de Professor: ')
idProfessor    = str(input('idProfessor: '))
nomeProfessor  = str(input('nomeProfessor: '))
dataNascimento = str(input('dataNascimento: '))
salario        = str(input('salario: '))

statement = '''
            INSERT INTO professor (idProfessor, nomeProfessor, dataNascimento, salario)
            VALUES
            ({}, {},{}, {})
            '''.format(idProfessor, nomeProfessor, dataNascimento, salario)
try:
  theTable.execute(statement)
  pgconn.commit()
except Exception as error:
  return(" Não foi possível realizar a inserção")


# Inclusão 2

print('Insira os dados do Aluno: ')
telefone       = str(input('telefone: '))
cra            = str(input('cra: '))
idAluno        = str(input('idAluno: '))
dataNascimento = str(input('dataNascimento: '))
nomeAluno      = str(input('nomeAluno: '))

statement = '''
                  INSERT INTO aluno (telefone, cra, idAluno, dataNascimento, nomeAluno)
                  VALUES
                  ({}, {}, {}, {}, {})
                  '''.format(telefone, cra, idAluno, dataNascimento, nomeAluno)

try:  
  theTable.execute(statement)
  pgconn.commit()
except Exception as error:
  return(" Não foi possível realizar a inserção")


# Alteração

# Alteração 1

print('Digite a tabela, atributo e tipo do atributo a se adicionar: ')
table    = str(input('Table: '))
atributo = str(input('Atributo: '))
tipo     = str(input('Tipo: '))

statement = '''
            ALTER TABLE {} ADD {} {}
            '''.format(table, atributo, tipo)

try:
  theTable.execute(statement)
  pgconn.commit()
except Exception as error:
  return(" Não foi possível realizar a alteração")


# Alteração 2

print('Digite a tabela e o atributo a se dropar: ')
table    = str(input('Table: '))
atributo = str(input('Atributo: '))

statement = '''
            ALTER TABLE {} DROP COLUMN {}'
            '''.format(table, atributo)

try:
  theTable.execute(statement)
  pgconn.commit()
except Exception as error:
  return(" Não foi possível realizar a alteração")

# Exclusão

# Exlusão 1

print('Digite a tabela, o atributo e qual o atributo da tupla a se deletar')
table    = str(input('Table: '))
atributo = str(input('Atributo: '))
elemento = str(input('Elemento: '))

statement = '''
            DELETE FROM {} WHERE {} = {}
            '''.format(table, atributo, elemento)

try:
  theTable.execute(statement)
  pgconn.commit()
except Exception as error:
  return(" Não foi possível realizar a exclusão")


# Exclusão 2

statement = '''
            DELETE FROM discliplina WHERE siglaDisciplina = 'ED1'
            '''

try:
  theTable.execute(statement)
  pgconn.commit()
except Exception as error:
  return(" Não foi possível realizar a exclusão")


# Consulta

# Consulta 1 

tabela = str(input('Tabela: '))
atributo = str(input('Atributo: '))

statement = '''
            SELECT {}.{}
              FROM {}
            '''.format(tabela, atributo, atributo)

try:
  theTable.execute(statement)
  pgconn.commit()
except Exception as error:
  return(" Não foi possível realizar a consulta")


# Consulta 2 

tabela    = str(input('Tabela: '))
atributo  = str(input('Atributo: '))
condition = str(input('Condição: '))

statement = '''
            SELECT {}.{}
              FROM {}
                WHERE {}
            '''.format(tabela, atributo, atributo, condition)

try:
  theTable.execute(statement)
  pgconn.commit()
except Exception as error:
  return(" Não foi possível realizar a consulta")