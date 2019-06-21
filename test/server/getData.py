#! /usr/bin/env python3
import psycopg2
from config import config
params = config('testData.ini')

def getData_1():
    """query data afrom the postgreSQL table using the fetchone method"""
    conn = None
    try: 
        # read connection parameters
        params = config('testData.ini')
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute("SELECT device, value, datetime FROM pythontest ORDER BY datetime;")
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

def getData_2():
    """query data from the postgrsql table using the fetchall method"""
    conn = None
    try:
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute("SELECT device, value, datetime From pythontest ORDER BY datetime;")
        rows = cur.fetchall()
        for row in rows:
            print(row)
        print("The number of fields:" , cur.rowcount)
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

# this function specifies number of rows to fetch within the get_data method
def iter_row(cursor, size=10):
    while True:
        rows = cursor.fetchmany(size)
        if not rows:
            break
        for row in rows:
            yield row

def getData_3():
    """ query device data using the fetchmany function"""
    conn = None
    try:
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute("""
                SELECT datetime,device,value 
                FROM pythontest
                ORDER BY datetime;
                """)
        for row in iter_row(cur,10):
            print(row)
        print("The number of fields:", cur.rowcount)
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()



if __name__ == '__main__':
    # test Method
    getData_3()

        

