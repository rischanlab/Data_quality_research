# -*- coding: utf-8 -*-
import csv
from pandas import read_excel
import aggregate_insight as ag


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
    file = "diabetes.xlsx"
    file10 = "diab10.xlsx"
    file20 = "diab20.xlsx"
    file30 = "diab30.xlsx"
    file40 = "diab40.xlsx"
    file50 = "diab50.xlsx"
    file60 = "diab60.xlsx"
    file70 = "diab70.xlsx"
    file80 = "diab80.xlsx"
    file90 = "diab90.xlsx"
    ddiab10 = "ddiab10.xlsx"
    ddiab20 = "ddiab20.xlsx"
    ddiab30 = "ddiab30.xlsx"
    ddiab40 = "ddiab40.xlsx"
    ddiab50 = "ddiab50.xlsx"
    ddiab60 = "ddiab60.xlsx"
    ddiab70 = "ddiab70.xlsx"
    ddiab80 = "ddiab80.xlsx"
    ddiab90 = "ddiab90.xlsx"

    cost_diab10 = "cost_diab10.xlsx"
    cost_diab20 = "cost_diab20.xlsx"
    cost_diab30 = "cost_diab30.xlsx"
    cost_diab40 = "cost_diab40.xlsx"
    cost_diab50 = "cost_diab50.xlsx"
    cost_diab60 = "cost_diab60.xlsx"
    cost_diab70 = "cost_diab70.xlsx"
    cost_diab80 = "cost_diab80.xlsx"
    cost_diab90 = "cost_diab90.xlsx"

    k = 10
    topk = get_topk(k, file)
    topk10 = get_topk(k, file10)
    topk20 = get_topk(k, file20)
    topk30 = get_topk(k, file30)
    topk40 = get_topk(k, file40)
    topk50 = get_topk(k, file50)
    topk60 = get_topk(k, file60)
    topk70 = get_topk(k, file70)
    topk80 = get_topk(k, file80)
    topk90 = get_topk(k, file90)

    # Attributes and Measures from Top-k Candidate
    # cost_topk10 = get_topk(k, cost_diab10)
    # cost_topk20 = get_topk(k, cost_diab20)
    # cost_topk30 = get_topk(k, cost_diab30)
    # cost_topk40 = get_topk(k, cost_diab40)
    # cost_topk50 = get_topk(k, cost_diab50)
    # cost_topk60 = get_topk(k, cost_diab60)
    # cost_topk70 = get_topk(k, cost_diab70)
    # cost_topk80 = get_topk(k, cost_diab80)
    # cost_topk90 = get_topk(k, cost_diab90)


    dtopk10 = get_topk(k, ddiab10)
    dtopk20 = get_topk(k, ddiab20)
    dtopk30 = get_topk(k, ddiab30)
    dtopk40 = get_topk(k, ddiab40)
    dtopk50 = get_topk(k, ddiab50)
    dtopk60 = get_topk(k, ddiab60)
    dtopk70 = get_topk(k, ddiab70)
    dtopk80 = get_topk(k, ddiab80)
    dtopk90 = get_topk(k, ddiab90)


# Ini untuk perhitungan RBO nya

    print("Ideal Top-k")
    print("Distance between ground truth to ground truth is {}.".format(ag.rboresult(topk, topk)))
    print("Ideal top-k to Without Impute - directly running")
    #print(topk)
    print("Distance between ground truth to dtopk10 is {}.".format(ag.rboresult(topk, dtopk10)))
    print("Jaccard between ground truth to dtopk10 is {}.".format(ag.jaccard_similarity(topk, dtopk10)))
    #print(dtopk10)
    print("Distance between ground truth to dtopk20 is {}.".format(ag.rboresult(topk, dtopk20)))
    print("Distance between ground truth to dtopk30 is {}.".format(ag.rboresult(topk, dtopk30)))
    print("Distance between ground truth to dtopk40 is {}.".format(ag.rboresult(topk, dtopk40)))
    print("Distance between ground truth to dtopk50 is {}.".format(ag.rboresult(topk, dtopk50)))
    print("Distance between ground truth to dtopk60 is {}.".format(ag.rboresult(topk, dtopk60)))
    print("Distance between ground truth to dtopk70 is {}.".format(ag.rboresult(topk, dtopk70)))
    print("Distance between ground truth to dtopk80 is {}.".format(ag.rboresult(topk, dtopk80)))
    print("Distance between ground truth to dtopk90 is {}.".format(ag.rboresult(topk, dtopk90)))


    print("Ideal top-k to Top-k after impute")
    print("RBO distance between ground truth to topk10 is {}.".format(ag.rboresult(topk, topk10)))
    print("RBO distance between ground truth to topk20 is {}.".format(ag.rboresult(topk, topk20)))
    print("RBO distance between ground truth to topk30 is {}.".format(ag.rboresult(topk, topk30)))
    print("RBO distance between ground truth to topk40 is {}.".format(ag.rboresult(topk, topk40)))
    print("RBO distance between ground truth to topk50 is {}.".format(ag.rboresult(topk, topk50)))
    print("RBO distance between ground truth to topk60 is {}.".format(ag.rboresult(topk, topk60)))
    print("RBO distance between ground truth to topk70 is {}.".format(ag.rboresult(topk, topk70)))
    print("RBO distance between ground truth to topk80 is {}.".format(ag.rboresult(topk, topk80)))
    print("RBO distance between ground truth to topk90 is {}.".format(ag.rboresult(topk, topk90)))

    print("Jaccard distance between ground truth to topk10 is {}.".format(ag.jaccard_similarity(topk, topk10)))
    print("Jaccard distance between ground truth to topk20 is {}.".format(ag.jaccard_similarity(topk, topk20)))
    print("Jaccard distance between ground truth to topk30 is {}.".format(ag.jaccard_similarity(topk, topk30)))
    print("Jaccard distance between ground truth to topk40 is {}.".format(ag.jaccard_similarity(topk, topk40)))
    print("Jaccard distance between ground truth to topk50 is {}.".format(ag.jaccard_similarity(topk, topk50)))
    print("Jaccard distance between ground truth to topk60 is {}.".format(ag.jaccard_similarity(topk, topk60)))
    print("Jaccard distance between ground truth to topk70 is {}.".format(ag.jaccard_similarity(topk, topk70)))
    print("Jaccard distance between ground truth to topk80 is {}.".format(ag.jaccard_similarity(topk, topk80)))
    print("Jaccard distance between ground truth to topk90 is {}.".format(ag.jaccard_similarity(topk, topk90)))

    m_list = [topk10, topk20, topk30, topk40, topk50, topk60, topk70, topk80, topk90]
    with open('results/ideal_vs_standard.csv', 'w', newline='') as f:
        for m in m_list:
            fields = [ag.rboresult(topk, m), ag.jaccard_similarity(topk, m)]
            writer = csv.writer(f)
            writer.writerow(fields)

    # print("Ideal top-k to Top-k with att and measure from top-k candidate")
    # print("Distance between ground truth to cost_topk10 is {}.".format(ag.rboresult(topk, cost_topk10)))
    # print("Distance between ground truth to cost_topk20 is {}.".format(ag.rboresult(topk, cost_topk20)))
    # print("Distance between ground truth to cost_topk30 is {}.".format(ag.rboresult(topk, cost_topk30)))
    # print("Distance between ground truth to cost_topk40 is {}.".format(ag.rboresult(topk, cost_topk40)))
    # print("Distance between ground truth to cost_topk50 is {}.".format(ag.rboresult(topk, cost_topk50)))
    # print("Distance between ground truth to cost_topk60 is {}.".format(ag.rboresult(topk, cost_topk60)))
    # print("Distance between ground truth to cost_topk70 is {}.".format(ag.rboresult(topk, cost_topk70)))
    # print("Distance between ground truth to cost_topk80 is {}.".format(ag.rboresult(topk, cost_topk80)))
    # print("Distance between ground truth to cost_topk90 is {}.".format(ag.rboresult(topk, cost_topk90)))

# Ideal Top-k
# Distance between ground truth to ground truth is 1.0.
# Ideal top-k to Without Impute - directly running
# Distance between ground truth to dtopk10 is 0.8718253968253966.
# Distance between ground truth to dtopk20 is 0.9043253968253968.
# Distance between ground truth to dtopk30 is 0.5982539682539683.
# Distance between ground truth to dtopk40 is 0.46519841269841267.
# Distance between ground truth to dtopk50 is 0.0815079365079365.
# Distance between ground truth to dtopk60 is 0.10956349206349207.
# Distance between ground truth to dtopk70 is 0.3574603174603175.
# Distance between ground truth to dtopk80 is 0.08456349206349206.
# Distance between ground truth to dtopk90 is 0.0.
# Ideal top-k to Top-k after impute
# Distance between ground truth to topk10 is 0.6592063492063491.
# Distance between ground truth to topk20 is 0.9375.
# Distance between ground truth to topk30 is 0.7108730158730159.
# Distance between ground truth to topk40 is 0.5514285714285714.
# Distance between ground truth to topk50 is 0.0.
# Distance between ground truth to topk60 is 0.0.
# Distance between ground truth to topk70 is 0.0.
# Distance between ground truth to topk80 is 0.0.
# Distance between ground truth to topk90 is 0.0.