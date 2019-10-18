from pandas import read_excel
import aggregate_insight as ag
import csv


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
    #standard = "diab10_standard_impute.xlsx"
    dynamic = "diab10_dynamic_impute.xlsx"

    k_list = [5, 10, 15, 20]
    with open('results/ideal_vs_dynamic_rbo.csv', 'w', newline='') as f:
        for k in k_list:
            topk = get_topk(k, file)
            topkdynamic = get_topk(k, dynamic)
            # topkdynamic = get_topk(k, dynamic)
            print("K ====== ", k)
            # print("Ideal Top-k")

            print("Ideal top-k vs dynamic")
            p_list = [0.80, 0.85, 0.90, 0.95, 0.99]
            for i in p_list:
                fields = [k, i, ag.rboresult(topk, topkdynamic, i)]
                print("Rbo p = {} dynamic to ideal is {}.".format(i, ag.rboresult(topk, topkdynamic, i)))
                writer = csv.writer(f)
                writer.writerow(fields)

    with open('results/ideal_vs_dynamic_jaccard.csv', 'w', newline='') as f:
        for k in k_list:
            topk = get_topk(k, file)
            topkdynamic = get_topk(k, dynamic)
            # topkdynamic = get_topk(k, dynamic)
            print("K ====== ", k)
            # print("Ideal Top-k")

            print("Ideal top-k vs dynamic")
            fields = [k, ag.jaccard_similarity(topk, topkdynamic)]
            print("Jaccard dynamic to ideal is {}.".format(ag.jaccard_similarity(topk, topkdynamic)))
            writer = csv.writer(f)
            writer.writerow(fields)



# C:\Anaconda\envs\data_cleaning\python.exe C:/Users/uqrmafru/PycharmProjects/Partial_Imputation/effectiveness_ideal_vs_dynamic.py
# K ======  5
# Ideal top-k vs Dynamic-Imputation
# Rbo distance dynamic to ideal is 0.9.
# Jaccard distance dynamic to ideal is 1.0.
# K ======  10
# Ideal top-k vs Dynamic-Imputation
# Rbo distance dynamic to ideal is 0.885436507936508.
# Jaccard distance dynamic to ideal is 0.8181818181818182.
# K ======  15
# Ideal top-k vs Dynamic-Imputation
# Rbo distance dynamic to ideal is 0.8665947015947018.
# Jaccard distance dynamic to ideal is 0.7647058823529411.
# K ======  20
# Ideal top-k vs Dynamic-Imputation
# Rbo distance dynamic to ideal is 0.8606510055561916.
# Jaccard distance dynamic to ideal is 0.7391304347826086.
#
# Process finished with exit code 0