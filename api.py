#! /usr/bin/env python3

import psycopg2
from config import config

def testConn():
    """ Connect to the PostgreSQL database server"""
    conn = None
    try:
        # read connection parameters
        params = config('testData.ini')

        # connect to the PostgreSQL server
        print ('Connecting to the database...')
        conn = psycopg2.connect(**params)

        # create a cursor
        cur = conn.cursor()

        # execute a statement
        print('PostgreSQL database version:')
        cur.execute('SELECT version()')

        # display the postgresql database sserver version
        db_version = cur.fetchone()
        print(db_version)

        # close the communication with the db
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')

def push(device,timestamp,value):
    "use to push data into db"
    sql = """INSERT INTO pythontest(device,datetime,value)
        VALUES(%s,%s,%s) RETURNING testpt;"""
    conn = None
    datapoint = None
    try: 
        # read database configuration
        params = config('testData.ini')
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.execute(sql,(device, timestamp,value,))
        # get the generated id block
        testpt = cur.fetchone()[0]
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception,psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
    return testpt
