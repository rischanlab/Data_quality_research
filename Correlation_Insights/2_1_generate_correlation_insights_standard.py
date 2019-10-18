import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import psycopg2 as pg
import pandas.io.sql as psql
import csv
import os
import aggregate_insight as ag


import psycopg2
conn = psycopg2.connect("dbname=median_impute user=postgres password=zenvisage")
connection = pg.connect("dbname=median_impute user=postgres password=zenvisage")

cursor = conn.cursor()
cursor.execute("""SELECT table_name FROM information_schema.tables
       WHERE table_schema = 'public'""")
mytable = cursor.fetchall()

for i in mytable:
    # get connected to the database
    db = psql.read_sql("SELECT * FROM " + str(i[0]), connection)
    print("Select all data from: ", i[0])
    db.drop(db.columns[[0]], axis=1, inplace=True)
    topk_nomissing = ag.generate_correlation_insights(db)
    print("Export data {} to csv".format(i[0]))
    topk_nomissing.to_csv('raw_results/standard_' + i[0] + '.csv',)