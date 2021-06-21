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
        print("Erro ao se conectar com o PostgreSQL", error)
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
        print(" Não foi possível realizar a alteração --> {}".format(error))
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
        print(" Não foi possível realizar a alteração --> {}".format(error))
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
        print(" Não foi possível realizar a exclusão --> {}".format(error))
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
        print(" Não foi possível realizar a consultaEspecifico --> {}".format(error))
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
            print(row[0])
        print('='*20)

        pgconn.commit()
    except Exception as error:
        print(" Não foi possível realizar a consultaEspecifico --> {}".format(error))
    return

if __name__ == "__main__":
    # Menu
    while True:
        print('1 - Inserir Professor: ')
        print('2 - Adicionar Atributo: ')
        print('3 - Dropar Atributo: ')
        print('4 - Consultar toda a Tabela: ')
        print('5 - Consultar especifico: ')
        print('6 - Excluir Tupla: ')
        print('7 - Sair')

        op = int(input("Digite uma opção: "))

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
            pgconn.close()
            break
        else:
            print('Opção não existe')
