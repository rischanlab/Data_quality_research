# -*- coding: utf-8 -*-
import csv
from pandas import read_excel
import aggregate_insight as ag
import glob


def convert_to_one(item):
    S = []
    for i in item:
        S.append(((''.join(i))))
    return S

def get_topk(k, file):
    my_sheet = 'Sheet1'
    file_name = file  # name of your excel file
    df = read_excel(file_name, sheet_name=my_sheet)
    df.drop(df.columns[[0,4]], axis=1, inplace=True)
    df = df.drop(df[df.Attributes == 'readmitted'].index)
    df = df.head(k).values.tolist()
    x = convert_to_one(df)
    return x # shows headers with top 5 rows



if __name__ == "__main__":

    k_list = [5, 10, 15, 20]

    for k in k_list:
        percentage_list = [10, 20, 30, 40, 50, 60, 70, 80, 90]
        for percent in percentage_list:
            for i in range(10):
                file_name0 = 'results/db_' +str(percent) + 'mdiab' + str(i+1) + '.xlsx'
                #file_name1 = '10_percent_missing_m_3k/standard_db_' + str(percent) + 'diab' + str(i + 1) + '.xlsx'
                for impute_file in glob.glob(file_name0):
                    print(impute_file)

                    if len(impute_file) == 24:
                        standard_file = 'results/db_' + str(percent) + impute_file[-10:]
                        print(standard_file)
                    else:
                        standard_file = 'results/db_' + str(percent) + impute_file[-11:]
                        print(standard_file)
                    standard = get_topk(k, standard_file)
                    dynamic = get_topk(k, impute_file)
                    print("RBO Dynamic to Standard = {}".format(ag.rboresult(dynamic, standard)))
                    print("Jaccard Dynamic to Standard = {}".format(ag.jaccard_similarity(dynamic, standard)))
                    with open('summary/dynamic_vs_missing.csv', 'a', newline='') as f:
                        fields = [percent, k, ag.rboresult(dynamic, standard), ag.jaccard_similarity(dynamic, standard)]
                        writer = csv.writer(f)
                        writer.writerow(fields)