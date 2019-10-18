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
    file10 = "diab10_dynamic_impute.xlsx"
    ddiab10 = "ddiab10.xlsx"

    k_list = [5, 10, 15, 20]
    for k in k_list:
        topk = get_topk(k, file)
        topk10 = get_topk(k, file10)
        dtopk10 = get_topk(k, ddiab10)

        # Ini untuk perhitungan RBO nya
        print("K ====== ", k)
        #print("Ideal Top-k")
        #print("RBO ideal to ideal is {}.".format(ag.rboresult(topk, topk)))
        #print("Jaccard ideal to ideal is {}.".format(ag.jaccard_similarity(topk, topk)))

        print("After median Impute to - Ideal top-k")
        print("Rbo Median impute to Ideal is {}.".format(ag.rboresult(topk, topk10)))
        print("Jaccard Median Impute to Ideal is {}.".format(ag.jaccard_similarity(topk, topk10)))
        # fields = ["Median Impute",k, ag.rboresult(topk, topk10), ag.jaccard_similarity(topk, topk10)]
        # with open('results/result.csv', 'a') as f:
        #     writer = csv.writer(f)
        #     writer.writerow(fields)
        print("No Impute to - Ideal top-k")
        print("RBO No Impute to Ideal is {}.".format(ag.rboresult(topk, dtopk10)))
        print("Jaccard No Impute to Ideal is {}.".format(ag.jaccard_similarity(topk, dtopk10)))
        fields = [k, ag.rboresult(topk, topk10), ag.jaccard_similarity(topk, topk10), ag.rboresult(topk, dtopk10), ag.jaccard_similarity(topk, dtopk10)]
        with open('results/result1.csv', 'a') as f:
            writer = csv.writer(f)
            writer.writerow(fields)



