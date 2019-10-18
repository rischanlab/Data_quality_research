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
db.head()
#dropping columns with high NA percentage
db.drop(['weight','medical_specialty','payer_code'],axis=1,inplace=True)

# dropping columns related to IDs
db.drop(['encounter_id','patient_nbr','admission_type_id','discharge_disposition_id','admission_source_id'],axis=1,inplace=True)

#removing invalid/unknown entries for gender
db=db[db['gender']!='Unknown/Invalid']

# dropping rows with NAs.
db.dropna(inplace=True)

db.rename(columns={'A1Cresult': 'a1cresult', 'glyburide-metformin': 'glyburide_metformin',
                  'glipizide-metformin': 'glipizide_metformin', 'glimepiride-pioglitazone': 'glimepiride_pioglitazone',
                  'metformin-rosiglitazone': 'metformin_rosiglitazone', 'metformin-pioglitazone': 'metformin_pioglitazone',
                  'diabetesMed': 'diabetesmed'}, inplace=True)
db.isnull().sum()

df = db.copy()


mlist = [0.05] #, 0.1, 0.15, 0.2

print("Data missing export to Postgre")
for i in mlist:
    for j in range(1):
        #print(int(i * 100), j)
        x = int(i * 100)
        #print(df)
        #print(df.columns.to_series().groupby(df.dtypes).groups)
        table_name1 = "db_" + str(x) + "missing_attr" + str(j+1)
        table_name2 = "db_" + str(x) + "missing_measure" + str(j + 1)
        table_name3 = "db_" + str(x) + "missing_a_m" + str(j + 1)
        #print(table_name)
        df_attr = df.select_dtypes(['object'])
        # df_float = df.select_dtypes(['float'])
        df_measure = df.select_dtypes(['int64']).astype(float)
        df_attr_missing = util.missing_data_attr(df_attr, i)
        new_df_attr = pd.concat([df_attr_missing, df_measure], axis=1, ignore_index=False, sort=False)
        df_measure_missing = util.missing_data_measure(df_measure, i)
        new_df_measure = pd.concat([df_attr, df_measure_missing], axis=1, ignore_index=False, sort=False)
        new_df_a_m = pd.concat([df_attr_missing, df_measure_missing], axis=1, ignore_index=False, sort=False)
        print(new_df_attr.shape)
        print(new_df_measure.shape)
        print(new_df_a_m.shape)
        engine = create_engine(r'postgresql+psycopg2://postgres:zenvisage@localhost:5432/impact_missing')
        c = engine.connect()
        conn = c.connection
        print("Exporting ... ", table_name1, table_name2, table_name3)
        # new_df_attr.to_sql(table_name1, engine)
        # new_df_measure.to_sql(table_name2, engine)
        # new_df_a_m.to_sql(table_name3, engine)

