import psycopg2
from psycopg2 import Error



def pgconnect():
    connection = None

    try:
        connection = psycopg2.connect(user="matheus_reis99",
                                      password="forfrodo",
                                      host="200.131.206.13",
                                      port="5432",
                                      database="matheus_reis99")

    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL", error)
        return
    finally:
        return connection


############################################
pgconn = pgconnect()
theTable = pgconn.cursor()
theTable.execute('SET search_path TO universidade')

def insereProfessor():
    print('Insira os dados de Professor: ')
    idProfessor    = str(input('id do Professor: '))
    nomeProfessor  = str(input('Nome do Professor: '))
    dataNascimento = str(input('Data de Nascimento: '))
    salario        = str(input('Salario: '))
    siglaFaculdade = str(input('Sigla da Faculdade: '))
    idTurma        = str(input('Id da Turma: '))

    sqlInsert = '''
                INSERT INTO professor (idProfessor, nomeProfessor, dataNascimento, salario, siglaFaculdade, idTurma)
                VALUES
                ('%(idProfessor)s' ,'%(nomeProfessor)s' ,'%(dataNascimento)s' ,'%(salario)s','%(siglaFaculdade)s','%(idTurma)s')
                '''
    sqlInsert = sqlInsert % {'idProfessor':idProfessor,
                            'nomeProfessor':nomeProfessor,
                            'dataNascimento':dataNascimento,
                            'salario':salario,
                            'siglaFaculdade':siglaFaculdade,
                            'idTurma':idTurma}

    try:
        theTable.execute(sqlInsert)
        pgconn.commit()
    except Exception as error:
        print(" Não foi possível realizar a inserção --> {}".format(error))

        pgconn.close()
    return



