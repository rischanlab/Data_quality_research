import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import psycopg2 as pg
import pandas.io.sql as psql
import csv

# get connected to the database
connection = pg.connect("dbname=diab_numeric user=postgres password=zenvisage")

db = psql.read_sql("SELECT * FROM diabetes", connection)
db.drop(db.columns[[0]], axis=1, inplace=True)

#Plot matrix of Correlation from all possible combination of boston Housing
data = db
dataCorr = data.corr(method='pearson')
dataCorr = dataCorr[abs(dataCorr) >= 0.01].stack().reset_index()
dataCorr = dataCorr[dataCorr['level_0'].astype(str)!=dataCorr['level_1'].astype(str)]

# filtering out lower/upper triangular duplicates
dataCorr['ordered-cols'] = dataCorr.apply(lambda x: '-'.join(sorted([x['level_0'],x['level_1']])),axis=1)
dataCorr = dataCorr.drop_duplicates(['ordered-cols'])
dataCorr.drop(['ordered-cols'], axis=1, inplace=True)

topk_nomissing = dataCorr.sort_values(by=[0], ascending=False)
topk_nomissing = topk_nomissing[['level_0', 'level_1']]
#S = [item for sublist in topk_nomissing for item in sublist]
topk_nomissing = topk_nomissing.reset_index()
topk_nomissing.drop(topk_nomissing.columns[[0]], axis=1, inplace=True)
topk_nomissing = topk_nomissing.head(5)
list1 = topk_nomissing['level_0'].values.tolist()
list2 = topk_nomissing['level_1'].values.tolist()
list3 = list1 + list2
#print(list3)
print(topk_nomissing)
#topk_nomissing.to_csv('raw_results/ideal_topk.csv',)