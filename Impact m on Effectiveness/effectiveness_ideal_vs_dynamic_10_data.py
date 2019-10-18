from pandas import read_excel
import aggregate_insight as ag
import csv
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

    my_list = [0, 1, 2, 3]
    k = 5
    file = "diabetes.xlsx"
    topk = get_topk(k, file)
    for my in my_list:
        percentage_list = [10]
        for percent in percentage_list:
            for i in range(10):
                file_name = '5k_m_' + str(my) + 'k/db_' +str(percent) + 'diab' + str(i+1) + '.xlsx'
                for impute_file in glob.glob(file_name):
                    #print(percent, file_name, k)
                    standard = get_topk(k, impute_file)
                    print("RBO Standard to Ideal = {}".format(ag.rboresult(standard, topk)))
                    print("Jaccard Standard to Ideal = {}".format(ag.jaccard_similarity(standard, topk)))
                    with open('results/dynamic_vs_ideal_10_percent.csv', 'a', newline='') as f:
                        fields = [percent, my, ag.rboresult(standard, topk), ag.jaccard_similarity(standard, topk)]
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