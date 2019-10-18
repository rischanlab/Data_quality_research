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
    standard = "diab10_standard_impute.xlsx"
    #dynamic = "diab10_dynamic_impute.xlsx"

    k_list = [5, 10, 15, 20]
    with open('results/ideal_vs_standard_rbo.csv', 'w', newline='') as f:
        for k in k_list:
            topk = get_topk(k, file)
            topkstandard = get_topk(k, standard)
            #topkdynamic = get_topk(k, dynamic)
            print("K ====== ", k)
            #print("Ideal Top-k")

            print("Ideal top-k vs Standard")
            p_list = [0.80, 0.85, 0.90, 0.95, 0.99]
            for i in p_list:
                fields = [k, i, ag.rboresult(topk, topkstandard, i)]
                print("Rbo p = {} standard to ideal is {}.".format(i, ag.rboresult(topk, topkstandard, i)))
                writer = csv.writer(f)
                writer.writerow(fields)

    with open('results/ideal_vs_standard_jaccard.csv', 'w', newline='') as f:
        for k in k_list:
            topk = get_topk(k, file)
            topkstandard = get_topk(k, standard)
            # topkdynamic = get_topk(k, dynamic)
            print("K ====== ", k)
            # print("Ideal Top-k")

            print("Ideal top-k vs Standard")
            fields = [k, ag.jaccard_similarity(topk, topkstandard)]
            print("Jaccard standard to ideal is {}.".format(ag.jaccard_similarity(topk, topkstandard)))
            writer = csv.writer(f)
            writer.writerow(fields)

# , ag.jaccard_similarity(topk, topkstandard)
#print("Jaccard distance standard to ideal is {}.".format(ag.jaccard_similarity(topk, topkstandard)))
# C:\Anaconda\envs\data_cleaning\python.exe C:/Users/uqrmafru/PycharmProjects/Partial_Imputation/effectiveness_ideal_vs_standard.py
# K ======  5
# Ideal top-k vs Standard
# Rbo distance standard to ideal is 0.9.
# Jaccard distance standard to ideal is 1.0.
# K ======  10
# Ideal top-k vs Standard
# Rbo distance standard to ideal is 0.9065476190476189.
# Jaccard distance standard to ideal is 1.0.
# K ======  15
# Ideal top-k vs Standard
# Rbo distance standard to ideal is 0.9073032523032523.
# Jaccard distance standard to ideal is 0.7647058823529411.
# K ======  20
# Ideal top-k vs Standard
# Rbo distance standard to ideal is 0.8971170161108241.
# Jaccard distance standard to ideal is 0.8181818181818182.
#
# Process finished with exit code 0

