import random
import numpy as np
import pandas as pd
import pandas.io.sql as psql
import psycopg2 as pg
from sqlalchemy import create_engine
from sklearn.base import TransformerMixin
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer


def dropout(a, percent):
    # create a copy
    mat = a.copy()
    # number of values to replace
    prop = int(mat.size * percent)
    # indices to mask
    mask = random.sample(range(mat.size), prop)
    # replace with NaN
    np.put(mat, mask, [np.NaN]*len(mask))
    return mat

def missing_topk(db, topk, percentage):
    df = db.copy()
    df = df.astype(float)
    data = df.values
    modified = dropout(data, percentage)
    new_df = pd.DataFrame(modified)  # Change % of data to NA in the dataset
    columns = topk
    new_df.columns = columns
    return new_df

def get_topk(k, file):
    df = pd.read_csv(file, index_col=0)
    x = df.head(k).values.tolist()
    z = [item for sublist in x for item in sublist]
    return z

table_name = 'diabetes'
connection = pg.connect("dbname=diab_numeric user=postgres password=zenvisage")
db = psql.read_sql("SELECT * FROM " + table_name, connection)
db.drop(db.columns[[0]], axis=1, inplace=True)

k = 5
mlist = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]

file_ideal_topk = 'raw_results/ideal_topk.csv'
topk = get_topk(k, file_ideal_topk)
print(topk)
print("Data missing export to Postgre")
for i in mlist:
    for j in range(10):
        #print(int(i * 100), j)
        x = int(i * 100)
        #print(df)
        #print(df.columns.to_series().groupby(df.dtypes).groups)
        table_name1 = "db_" + str(x) + "missing_topk" + str(j+1)
        df = db.copy()
        print(df.shape)
        new_df_topk = df[topk]
        print(new_df_topk.shape)
        df.drop(topk, axis=1, inplace=True)
        print(df.shape)
        #df_float = df.select_dtypes(['float'])
        df_topk_missing = missing_topk(new_df_topk, topk, i)
        new_df_missing = pd.concat([df, df_topk_missing], axis=1, ignore_index=False, sort=False)
        engine = create_engine(r'postgresql+psycopg2://postgres:zenvisage@localhost:5432/diab_numeric')
        c = engine.connect()
        conn = c.connection
        print("Exporting...", table_name1)
        new_df_missing.to_sql(table_name1, engine)
