import psycopg2
from time import sleep
import os
from psycopg2 import Error

def getPassword():
    fileObj = open('senha.txt', 'r')

    for line in fileObj:
        password = line
    return password
    

def pgconnect():
    connection = None
    key = str(getPassword())

    try:
        connection = psycopg2.connect(user="matheus_reis99",
                                      password=key,
                                      host="200.131.206.13",
                                      port="5432",
                                      database="matheus_reis99")

    except (Exception, Error) as error:
        print("033[31mErro ao se conectar com o PostgreSQL\033[m", error)
        return
    finally:
        print('\033[32mSERVIDOR CONECTADO COM SUCESSO\033[m')
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
        print("\033[31m Não foi possível realizar a inserção --> \n{}\033[m".format(error))
    finally:
        print('\033[32m INSERÇÃO REALIZADA COM SUCESSO\033[m')
    return



def adicionaAtributo():
    print('Digite a tabela, o atributo e tipo do atributo a se adicionar: ')
    table    = str(input('Tabela: '))
    atributo = str(input('Atributo: '))
    tipo     = str(input('Tipo: '))

    sqlAlter = '''
                ALTER TABLE %(table)s ADD %(atributo)s %(tipo)s
                '''

    sqlAlter = sqlAlter % {'table':table,
                            'atributo':atributo,
                            'tipo':tipo}

    try:
        theTable.execute(sqlAlter)
        pgconn.commit()
    except Exception as error:
        print("\033[31m Não foi possível realizar a alteração --> \n{}\033[m".format(error))
    finally:
        print('\033[32m ALTERAÇÃO REALIZADA COM SUCESSO\033[m')
    return

def dropAtributo():
    print('Digite a tabela e o atributo a se dropar: ')
    table    = str(input('Tabela: '))
    atributo = str(input('Atributo: '))

    sqlAlter = '''
                ALTER TABLE %(table)s DROP COLUMN %(atributo)s
                '''

    sqlAlter = sqlAlter % {'table':table,
                            'atributo':atributo}

    try:
        theTable.execute(sqlAlter)
        pgconn.commit()
    except Exception as error:
        print("\033[31m Não foi possível realizar a alteração --> \n{}\033[m".format(error))
    finally:
        print('\033[32m ALTERAÇÃO REALIZADA COM SUCESSO\033[m')
    return

def excluiTupla():
    print('Digite a tabela, o atributo e qual o atributo da tupla a se deletar')
    table    = str(input('Tabela: '))
    atributo = str(input('Atributo: '))
    elemento = str(input('Especifique: '))

    sqlDelete = '''
                DELETE FROM %(table)s WHERE %(atributo)s = '%(elemento)s'
                '''
    sqlDelete = sqlDelete % {'table':table,
                            'atributo':atributo,
                            'elemento':elemento} 

    try:
        theTable.execute(sqlDelete)
        pgconn.commit()
    except Exception as error:
        print("\033[31m Não foi possível realizar a exclusão --> \n{}\033[m".format(error))
    finally:
        print('\033[32m TUPLA EXCLUÍDA COM SUCESSO\033[m')
    return

def consultaTodos():
    tabela = str(input('Tabela: '))

    sqlSelect = '''
                SELECT *
                FROM %(tabela)s
                '''

    sqlSelect = sqlSelect % {'tabela':tabela}
                            
    try:
        theTable.execute(sqlSelect)
        myResult = theTable.fetchall()

        print('='*20)
        for row in myResult:
            print(row)
        print('='*20)

        pgconn.commit()
    except Exception as error:
        print("\033[31m Não foi possível realizar a consultaEspecifico --> \n{}\033[m".format(error))
    return

def consultaEspecifico():
    tabela = str(input('Tabela: '))
    atributo = str(input('Atributo: '))

    sqlSelect = '''
                SELECT %(tabela)s.%(atributo)s
                FROM %(tabela)s
                '''

    sqlSelect = sqlSelect % {'tabela':tabela,
                            'atributo':atributo,
                            'tabela':tabela}
                            
    try:
        theTable.execute(sqlSelect)
        myResult = theTable.fetchall()

        print('='*20)
        for row in myResult:
            print('\033[34m'+row[0]+'\033[m')
        print('='*20)

        pgconn.commit()
    except Exception as error:
        print("\033[31m Não foi possível realizar a consultaEspecifico --> \n{}\033[m".format(error))
    return

if __name__ == "__main__":
    # Menu
    while True:
        sleep(2)
        system('cls' if os.name == 'nt' else 'clear')

        print('1 - Inserir Professor: ')
        print('2 - Adicionar Atributo: ')
        print('3 - Dropar Atributo: ')
        print('4 - Consultar toda a Tabela: ')
        print('5 - Consultar especifico: ')
        print('6 - Excluir Tupla: ')
        print('7 - Sair')

        op = int(input("\033[34mDigite uma opção: \033[m"))

        if(op == 1):
            insereProfessor()
        elif(op == 2):
            adicionaAtributo()
        elif(op == 3):
            dropAtributo()
        elif(op == 4):
            consultaTodos()
        elif(op == 5):
            consultaEspecifico()
        elif(op == 6):
            excluiTupla()
        elif(op == 7):
            print('\033[34mSaindo . . .\033[m')
            sleep(2)
            pgconn.close()
            break
        else:
            print('\033[31mOpção não existe\033[m')
