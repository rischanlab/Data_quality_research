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
    dynamic = "diab10_dynamic_impute.xlsx"

    k_list = [5, 10, 15, 20]
    with open('results/standard_vs_dynamic_rbo.csv', 'w', newline='') as f:
        for k in k_list:
            topkstandard = get_topk(k, standard)
            topkdynamic = get_topk(k, dynamic)
            print("K ====== ", k)
            # print("Ideal Top-k")

            print("Standard vs dynamic")
            p_list = [0.80, 0.85, 0.90, 0.95, 0.99]
            for i in p_list:
                fields = [k, i, ag.rboresult(topkstandard, topkdynamic, i)]
                print("Rbo p = {} dynamic to standard is {}.".format(i, ag.rboresult(topkstandard, topkdynamic, i)))
                writer = csv.writer(f)
                writer.writerow(fields)

    with open('results/standard_vs_dynamic_jaccard.csv', 'w', newline='') as f:
        for k in k_list:
            topkstandard = get_topk(k, standard)
            topkdynamic = get_topk(k, dynamic)
            print("K ====== ", k)
            # print("Ideal Top-k")

            print("standard vs dynamic")
            fields = [k, ag.jaccard_similarity(topkstandard, topkdynamic)]
            print("Jaccard dynamic to standard is {}.".format(ag.jaccard_similarity(topkstandard, topkdynamic)))
            writer = csv.writer(f)
            writer.writerow(fields)



