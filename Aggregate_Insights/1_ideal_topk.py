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
    df = df.head(k).reset_index(drop=True)
    #df = df.head(k).values.tolist()
    #x = convert_to_one(df)
    return df # shows headers with top 5 rows



k = 5
file = "results/diabetes.xlsx"
topk = get_topk(k, file)
print(topk)