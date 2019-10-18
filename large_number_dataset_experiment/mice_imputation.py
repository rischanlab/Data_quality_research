import random
import matplotlib.pyplot as plt
import psycopg2 as pg
import pandas.io.sql as psql
import numpy as np
import pandas as pd
from sqlalchemy import create_engine
import utilities as util

db = pd.read_csv('dataset/diabetic_data.csv')
db.replace('?',np.nan,inplace=True)
#dropping columns with high NA percentage
db.drop(['weight','medical_specialty','payer_code'],axis=1,inplace=True)
# dropping columns related to IDs
db.drop(['encounter_id','patient_nbr','admission_type_id','discharge_disposition_id','admission_source_id'],axis=1,inplace=True)
#removing invalid/unknown entries for gender
db=db[db['gender']!='Unknown/Invalid']
# dropping rows with NAs.
db.dropna(inplace=True)

mlist = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]

print("Missing + Impute Start export to postgre")
for i in mlist:
    for j in range(10):
        #print(int(i * 100), j)
        x = int(i * 100)
        table_name = "mice_" + str(x) + "diab" + str(j+1)
        #print(table_name)
        data = util.mice_impute(db, i)
        engine = create_engine(r'postgresql+psycopg2://postgres:zenvisage@localhost:5432/mice_impute')
        c = engine.connect()
        conn = c.connection
        print("Exporting ... ", table_name)
        data.to_sql(table_name, engine)



# data = util.missing_data(db, i)
# engine = create_engine(r'postgresql+psycopg2://postgres:zenvisage@localhost:5432/data_cleaning')
# c = engine.connect()
# conn = c.connection
# table_name = str(int(i*100))
# data.to_sql('diabetes', engine)

# from sqlalchemy import create_engine
# engine = create_engine(r'postgresql+psycopg2://postgres:zenvisage@localhost:5432/data_cleaning')
# c = engine.connect()
# conn = c.connection
# db.to_sql('diabetes', engine)
#
# conn.close()