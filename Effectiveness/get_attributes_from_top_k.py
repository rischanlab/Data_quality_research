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

def get_unique(k,file):
    my_sheet = 'Sheet1'
    file_name = file  # name of your excel file
    df = read_excel(file_name, sheet_name=my_sheet)
    df.drop(df.columns[[0, 4]], axis=1, inplace=True)
    df = df.drop(df[df.Attributes == 'readmitted'].index)
    df = df.head(k)
    a = df.Attributes.unique().tolist()
    m = df.Meassure.unique().tolist()
    f = df.Function.unique().tolist()
    all = a + m + f
    return all  # shows headers with top 5 rows



if __name__ == "__main__":
    file = "diabetes.xlsx"
    file10 = "diab10_dynamic_impute.xlsx"
    ddiab10 = "ddiab10.xlsx"
    k = 10
    #topk = get_topk(k, file)
    #topk10 = get_topk(k, file10)
    dtopk10 = get_topk(k, ddiab10)
    attr_dtopk10 = get_unique(2*k,ddiab10)

    print(dtopk10)
    print(attr_dtopk10)
    # only top-k 6 Attributes, 6 measures, 1 aggr. function = 12 columns
    # ['miglitol', 'acarbose', 'acetohexamide', 'glimepiride_pioglitazone',
    # 'diag_3', 'diag_2', 'number_outpatient', 'number_inpatient', 'time_in_hospital',
    # 'num_procedures', 'number_emergency', 'num_medications', 'avg']

    # 2*K 11 Attributes, 7 measures, 2 aggregate function = 18 columns
    # ['miglitol', 'acarbose', 'acetohexamide', 'glimepiride_pioglitazone', 'diag_3', 'diag_2', 'gender', 'diag_1',
    # 'tolazamide', 'troglitazone', 'age', 'number_outpatient', 'number_inpatient', 'time_in_hospital', 'num_procedures',
    # 'number_emergency', 'num_medications', 'number_diagnoses', 'avg', 'max']

