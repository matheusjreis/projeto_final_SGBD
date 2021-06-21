import psycopg2
from psycopg2 import Error



def pgconnect():
    connection = None

    try:
        # Connect to an existing database
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

pgconn = pgconnect()
theTable = pgconn.cursor()
theTable.execute('SET search_path TO see')