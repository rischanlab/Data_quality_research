# -*- coding: utf-8 -*-
from a_seedb_function import SeeDB
from a_seedb_db import data
import psycopg2
conn = psycopg2.connect("dbname=diab_experiment user=postgres password=zenvisage")

cursor = conn.cursor()
cursor.execute("""SELECT table_name FROM information_schema.tables
       WHERE table_schema = 'public'""")
mytable = cursor.fetchall()


if __name__ == "__main__":

    top_k = 10
    atr = ['race', 'gender', 'age', 'diag_1', 'diag_2', 'diag_3', 'max_glu_serum',
           'a1cresult', 'metformin', 'repaglinide', 'nateglinide',
           'chlorpropamide', 'glimepiride', 'acetohexamide', 'glipizide',
           'glyburide', 'tolbutamide', 'pioglitazone', 'rosiglitazone', 'acarbose',
           'miglitol', 'troglitazone', 'tolazamide', 'examide', 'citoglipton',
           'insulin', 'glyburide_metformin', 'glipizide_metformin',
           'glimepiride_pioglitazone', 'metformin_rosiglitazone',
           'metformin_pioglitazone', 'change', 'diabetesmed', 'readmitted']
    measure = ['time_in_hospital', 'num_lab_procedures', 'num_procedures',
               'num_medications', 'number_outpatient', 'number_emergency',
               'number_inpatient', 'number_diagnoses']

    func = ['sum', 'avg', 'max']

    for i in mytable:
        db, table, data_set = data(i[0], atr, measure, func)
        print("running with db {}".format(i[0]))
        framework = SeeDB(db,data_set,table,top_k)
        framework.main()
        print("done")
