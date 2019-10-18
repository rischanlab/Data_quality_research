# -*- coding: utf-8 -*-
import csv
import aggregate_insight as ag
import utilities as util
import psycopg2 as pg
import pandas.io.sql as psql
import pandas as pd
import glob


if __name__ == "__main__":


    k_list = [5, 10, 15, 20]
    m_list = [0, 1, 2, 3]
    percentage_list = [10, 20, 30, 40, 50, 60, 70, 80, 90]

    for default_k in k_list:
        for m in m_list:
            km = default_k + (m*default_k)
            print(default_k, m, km)
            for percent in percentage_list:
                for i in range(10):
                    file_name = 'raw_results/db_' +str(percent) + 'mdiab' + str(i+1) + '.xlsx'
                    print(file_name)
                    for missing_file in glob.glob(file_name):
                        attr = ag.get_unique_excel(km, missing_file)
                        print(attr)
                        connection = pg.connect("dbname=diab_experiment user=postgres password=zenvisage")
                        print(len(missing_file))
                        table_name = 'db_' + str(percent) + 'mdiab' + str(i+1)
                        df = psql.read_sql("SELECT * FROM " + table_name , connection)
                        df.drop(df.columns[[0]], axis=1, inplace=True)
                        # print(df.head(), df.shape)
                        df_impute = df[attr]
                        df.drop(attr, axis=1, inplace=True)
                        df_impute = util.median_impute(df_impute)
                        data = pd.concat([df, df_impute], axis=1)
                        from sqlalchemy import create_engine
                        engine = create_engine(r'postgresql+psycopg2://postgres:zenvisage@localhost:5432/diab_mk')
                        c = engine.connect()
                        conn = c.connection
                        df.to_sql('dynamic_' + table_name + '_' + str(default_k) + '_' + str(m), engine)
                        print('dynamic_' + table_name + '_' + str(default_k) + '_' + str(m))
                        #topk = ag.generate_correlation_insights(data)
                        #topk.to_csv('raw_results/dynamic_' + table_name + '_' + str(default_k) + '_' + str(m) +'.csv')




# default_k = 5
# m = default_k*0
# k = default_k + m
#
# attr = ag.get_unique(k, 'raw_results/missing_db_10missing1.csv')
# print(attr)
# connection = pg.connect("dbname=diab_numeric user=postgres password=zenvisage")
# df = psql.read_sql("SELECT * FROM db_10missing1", connection)
# df.drop(df.columns[[0]], axis=1, inplace=True)
# #print(df.head(), df.shape)
# df_impute = df[attr]
# df.drop(attr,axis=1,inplace=True)
# df_impute = util.median_impute(df_impute)
#
# data = pd.concat([df, df_impute], axis=1)
# topk = ag.generate_correlation_insights(data)
# topk.to_csv('raw_results/standard_' + i[0] + '.csv',)
#print(df_impute.head(), df_impute.shape)
#print(df.head(), df.shape)
#print(result.head(), result.shape)
