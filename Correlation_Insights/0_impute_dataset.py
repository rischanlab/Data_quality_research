import random
import matplotlib.pyplot as plt
import psycopg2 as pg
import pandas.io.sql as psql
import numpy as np
import pandas as pd
from sqlalchemy import create_engine
import utilities as util

# get connected to the database


mlist = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]

print("Median Imputation export to Postgre")
for i in mlist:
    for j in range(10):
        #print(int(i * 100), j)
        x = int(i * 100)
        table_name = "db_" + str(x) + "missing" + str(j+1)
        connection = pg.connect("dbname=diab_numeric user=postgres password=zenvisage")
        db = psql.read_sql("SELECT * FROM " + table_name, connection)
        db.drop(db.columns[[0]], axis=1, inplace=True)
        #print(table_name)
        data = util.median_impute(db)
        engine = create_engine(r'postgresql+psycopg2://postgres:zenvisage@localhost:5432/median_impute')
        c = engine.connect()
        conn = c.connection
        new_table_name = "db_" + str(x) + "median" + str(j + 1)
        print("Exporting ... ", new_table_name)
        data.to_sql(new_table_name, engine)

print("MICE imputation export to Postgre")
for i in mlist:
    for j in range(10):
        #print(int(i * 100), j)
        x = int(i * 100)
        table_name = "db_" + str(x) + "missing" + str(j+1)
        connection = pg.connect("dbname=diab_numeric user=postgres password=zenvisage")
        db = psql.read_sql("SELECT * FROM " + table_name, connection)
        db.drop(db.columns[[0]], axis=1, inplace=True)
        #print(table_name)
        data = util.mice_impute(db)
        engine = create_engine(r'postgresql+psycopg2://postgres:zenvisage@localhost:5432/mice_impute')
        c = engine.connect()
        conn = c.connection
        new_table_name = "db_" + str(x) + "mice" + str(j + 1)
        print("Exporting ... ", new_table_name)
        data.to_sql(new_table_name, engine)
