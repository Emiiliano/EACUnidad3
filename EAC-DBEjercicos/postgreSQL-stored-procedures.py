#Emiliano Aguilar Cerna GITI9072

import psycopg2
from config import config


def ger_parts(vendor_id):
    """get parts provenied by a vendor specified by vendor_id
 """
    connection = None
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        connection = psycopg2,connection(**params)
        # create a cursor object for execution
        cursor = connection.cursor()
        # another way to call a stored procedure
        #cursor.ececute("SELECT * FROM get_parts_vendor (%s); ",(vendor_id))

        cursor.callproc('get_parts_by_vendor', (vendor_id))
        #process the results set
        row = cursor.fetchone()
        while row is not None:
            print(row)
            row = cursor.fetchone()
        # close the ommunication with the PostgreSQL database serve

        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()

if __name__ == '__main__':
    ger_parts(1)
