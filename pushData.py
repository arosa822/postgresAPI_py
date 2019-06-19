#! /usr/bin/env python3

import psycopg2
from config import config

device = "01"
timestamp = "06/01/19 00:00:00"
state = 100

def insert_data(device, timestamp, state):
    """insert a new row into the table"""
    sql = """INSERT INTO statedata(device, datetime, state)
        VALUES(%s,%s,%s) RETURNING datapoint;"""
    conn = None
    datapoint = None
    try: 
        # read datebase configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.execute(sql,(device,timestamp,state,))
        # get the generated id back
        datapoint = cur.fetchone()[0]
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception,psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return datapoint

if __name__ == '__main__':
    # insert one row
    insert_data(device, timestamp, state)
