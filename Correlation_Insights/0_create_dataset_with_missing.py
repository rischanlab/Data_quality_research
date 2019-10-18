import random
import matplotlib.pyplot as plt
import psycopg2 as pg
import pandas.io.sql as psql
import numpy as np
import pandas as pd
from sqlalchemy import create_engine
import utilities as util

df = pd.read_csv('dataset/diabetic_data.csv')
df.replace('?',np.nan,inplace=True)
#dropping columns with high NA percentage
df.drop(['weight','medical_specialty','payer_code'],axis=1,inplace=True)
# dropping columns related to IDs
df.drop(['encounter_id','patient_nbr','admission_type_id','discharge_disposition_id','admission_source_id'],axis=1,inplace=True)
#removing invalid/unknown entries for gender
df=df[df['gender']!='Unknown/Invalid']
# dropping rows with NAs.
df.dropna(inplace=True)

diag_cols = ['diag_1', 'diag_2', 'diag_3']
for col in diag_cols:
    df[col] = df[col].str.replace('E', '-')
    df[col] = df[col].str.replace('V', '-')
    condition = df[col].str.contains('250')
    df.loc[condition, col] = '250'

df[diag_cols] = df[diag_cols].astype(float)

# diagnosis grouping
for col in diag_cols:
    df['temp'] = np.nan

    condition = df[col] == 250
    df.loc[condition, 'temp'] = 1  # Diabetes

    condition = (df[col] >= 390) & (df[col] <= 458) | (df[col] == 785)
    df.loc[condition, 'temp'] = 2  # Circulatory

    condition = (df[col] >= 460) & (df[col] <= 519) | (df[col] == 786)
    df.loc[condition, 'temp'] = 3  # Respiratory

    condition = (df[col] >= 520) & (df[col] <= 579) | (df[col] == 787)
    df.loc[condition, 'temp'] = 4  # Digestive

    condition = (df[col] >= 580) & (df[col] <= 629) | (df[col] == 788)
    df.loc[condition, 'temp'] = 5  # Genitourinary

    condition = (df[col] >= 800) & (df[col] <= 999)
    df.loc[condition, 'temp'] = 6  # Injury

    condition = (df[col] >= 710) & (df[col] <= 739)
    df.loc[condition, 'temp'] = 7  # Muscoloskeletal

    condition = (df[col] >= 140) & (df[col] <= 239)
    df.loc[condition, 'temp'] = 8  # Neoplasms

    condition = df[col] == 0
    df.loc[condition, col] = '?'
    df['temp'] = df['temp'].fillna(9)
    condition = df['temp'] == '0'
    df.loc[condition, 'temp'] = np.nan
    df[col] = df['temp']
    df.drop('temp', axis=1, inplace=True)

df.dropna(inplace=True)

df[diag_cols] = df[diag_cols].astype(int)

df['age'] = df['age'].str[1:].str.split('-', expand=True)[0]
df['age'] = df['age'].astype(int)
max_glu_serum_dict = {'None': 0,
                      'Norm': 100,
                      '>200': 200,
                      '>300': 300
                      }
df['max_glu_serum'] = df['max_glu_serum'].replace(max_glu_serum_dict)

A1Cresult_dict = {'None': 0,
                  'Norm': 5,
                  '>7': 7,
                  '>8': 8
                  }
df['A1Cresult'] = df['A1Cresult'].replace(A1Cresult_dict)

change_dict = {'No': -1,
               'Ch': 1
               }
df['change'] = df['change'].replace(change_dict)

diabetesMed_dict = {'No': -1,
                    'Yes': 1
                    }
df['diabetesMed'] = df['diabetesMed'].replace(diabetesMed_dict)

d24_feature_dict = {'Up': 10,
                    'Down': -10,
                    'Steady': 0,
                    'No': -20
                    }
d24_cols = ['metformin', 'repaglinide', 'nateglinide', 'chlorpropamide',
            'glimepiride', 'acetohexamide', 'glipizide', 'glyburide',
            'tolbutamide', 'pioglitazone', 'rosiglitazone', 'acarbose',
            'miglitol', 'troglitazone', 'tolazamide', 'examide',
            'citoglipton', 'insulin', 'glyburide-metformin', 'glipizide-metformin',
            'glimepiride-pioglitazone', 'metformin-rosiglitazone', 'metformin-pioglitazone']
for col in d24_cols:
    df[col] = df[col].replace(d24_feature_dict)

condition = df['readmitted'] != 'NO'
df['readmitted'] = np.where(condition, 1, 0)

gender = {'Female': 0,
          'Male': 1}

df['gender'] = df['gender'].replace(gender)
df['gender'] = df['gender'].astype(int)

race = {'Caucasian': 1,
        'AfricanAmerican': 2,
        'Asian': 3,
        'Hispanic': 4,
        'Other': 5
        }

df['race'] = df['race'].replace(race)
df['race'] = df['race'].astype(int)

df = df.astype(float)
df.rename(columns={'A1Cresult': 'a1cresult', 'glyburide-metformin': 'glyburide_metformin',
                  'glipizide-metformin': 'glipizide_metformin', 'glimepiride-pioglitazone': 'glimepiride_pioglitazone',
                  'metformin-rosiglitazone': 'metformin_rosiglitazone', 'metformin-pioglitazone': 'metformin_pioglitazone',
                  'diabetesMed': 'diabetesmed'}, inplace=True)


mlist = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]

print("Data missing export to Postgre")
for i in mlist:
    for j in range(10):
        #print(int(i * 100), j)
        x = int(i * 100)
        table_name = "db_" + str(x) + "missing" + str(j+1)
        #print(table_name)
        data = util.missing_data(df, i)
        engine = create_engine(r'postgresql+psycopg2://postgres:zenvisage@localhost:5432/diab_numeric')
        c = engine.connect()
        conn = c.connection
        print("Exporting ... ", table_name)
        data.to_sql(table_name, engine)
