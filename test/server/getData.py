#! /usr/bin/env python3
import psycopg2
from config import config

def getData_1():
    """query data afrom the postgreSQL table using the fetchone method"""
    conn = None
    try: 
        # read connection parameters
        params = config('testData.ini')

        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        cur.execute("SELECT device, value FROM pythontest ORDER BY datetime;")
        row  = cur.fetchone()

        while row is not None:
            print(row)
            row = cur.fetchone()

        
        print("The number of fields:" , cur.rowcount)
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

if __name__ == '__main__':
    # test Method
    getData_1()

        

