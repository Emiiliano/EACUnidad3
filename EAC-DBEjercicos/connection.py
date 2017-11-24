#Emiliano Aguilar Cerna GITI9072
import psycopg2
from config import config

def connect ():
    """Connect to the Postgresql database server"""
    conn = None

    try:
        params = config()

        print('Connecting to the Postresql database...')
        conn = psycopg2.connect(**params)

        # Create cursor
        cursor = conn.cursor()

        print('Postgresql database version:')
        cursor.execute('SELECT version()')

        #Display the Postgresql databse server version

        db_version = cursor.fetchone()
        print(db_version)

        # Close the communication with the Postgresql
        cursor.close()
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed')

if __name__=='__main__':
    connect()


