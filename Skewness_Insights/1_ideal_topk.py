import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import psycopg2 as pg
import pandas.io.sql as psql
import aggregate_insight as ag
import csv

# get connected to the database
connection = pg.connect("dbname=diab_numeric user=postgres password=zenvisage")

db = psql.read_sql("SELECT * FROM diabetes", connection)
db.drop(db.columns[[0]], axis=1, inplace=True)

#Plot matrix of Correlation from all possible combination of boston Housing
#print(db.head())
topk_nomissing = ag.generate_skewness_insights_with_score(db)
#topk_nomissing.to_csv('raw_results/ideal_topk.csv',)
print(topk_nomissing)