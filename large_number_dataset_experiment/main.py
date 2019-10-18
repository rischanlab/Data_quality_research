# -*- coding: utf-8 -*-
from seedb import SeeDB
from diabetes import data
import psycopg2
conn = psycopg2.connect("dbname=median_impute user=postgres password=zenvisage")

cursor = conn.cursor()
cursor.execute("""SELECT table_name FROM information_schema.tables
       WHERE table_schema = 'public'""")
mytable = cursor.fetchall()


if __name__ == "__main__":

    top_k = 10

    for i in mytable:
        db, table, data_set = data(i[0])
        print("running with db {}".format(i[0]))
        framework = SeeDB(db,data_set,table,top_k)
        framework.main()
        print("done")

# list_table = [    'diab10',
#                   'diab20',
#                   'diab30',
#                   'diab40',
#                   'diab50',
#                   'diab60',
#                   'diab70',
#                   'diab80',
#                   'diab90']