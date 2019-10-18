# -*- coding: utf-8 -*-
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
    df.drop(df.columns[[3]], axis=1, inplace=True)
    df = df.head(k).values.tolist()
    x = convert_to_one(df)
    return x # shows headers with top 5 rows



if __name__ == "__main__":
    file = "fAS.xlsx"
    file10 = "fAS10.xlsx"
    file20 = "fAS20.xlsx"
    file30 = "fAS30.xlsx"
    file40 = "fAS40.xlsx"
    file50 = "fAS50.xlsx"
    file60 = "fAS60.xlsx"
    file70 = "fAS70.xlsx"
    file80 = "fAS80.xlsx"
    file90 = "fAS90.xlsx"
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

    print("Distance between ground truth to ground truth is {}.".format(ag.rboresult(topk, topk)))
    print("Distance between ground truth to topk10 is {}.".format(ag.rboresult(topk, topk10)))
    print("Distance between ground truth to topk20 is {}.".format(ag.rboresult(topk, topk20)))
    print("Distance between ground truth to topk30 is {}.".format(ag.rboresult(topk, topk30)))
    print("Distance between ground truth to topk40 is {}.".format(ag.rboresult(topk, topk40)))
    print("Distance between ground truth to topk50 is {}.".format(ag.rboresult(topk, topk50)))
    print("Distance between ground truth to topk60 is {}.".format(ag.rboresult(topk, topk60)))
    print("Distance between ground truth to topk70 is {}.".format(ag.rboresult(topk, topk70)))
    print("Distance between ground truth to topk80 is {}.".format(ag.rboresult(topk, topk80)))
    print("Distance between ground truth to topk90 is {}.".format(ag.rboresult(topk, topk90)))

#
# Distance between ground truth to ground truth is 1.0.
# Distance between ground truth to topk10 is 0.8400000000000001.
# Distance between ground truth to topk20 is 0.9733333333333333.
# Distance between ground truth to topk30 is 0.8400000000000001.
# Distance between ground truth to topk40 is 0.7557142857142858.
# Distance between ground truth to topk50 is 0.8757142857142857.
# Distance between ground truth to topk60 is 0.8646031746031746.
# Distance between ground truth to topk70 is 0.7122619047619048.
# Distance between ground truth to topk80 is 0.6532539682539682.
# Distance between ground truth to topk90 is 0.7318650793650793.
