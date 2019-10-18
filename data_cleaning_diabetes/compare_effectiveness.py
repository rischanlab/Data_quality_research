from pandas import read_excel
import aggregate_insight as ag

def get_topk(k, file):
    my_sheet = 'Sheet1'
    file_name = file  # name of your excel file
    df = read_excel(file_name, sheet_name=my_sheet)
    df.drop(df.columns[[0,4]], axis=1, inplace=True)
    df = df.drop(df[df.Attributes == 'readmitted'].index)
    df = df.head(k)
    return df # shows headers with top 5 rows

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
    all = [[a],[m],[f]]
    return all  # shows headers with top 5 rows

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


    default_k = 5
    m = default_k*2
    k = default_k + m
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
    dtopk10 = get_topk(k, ddiab10)
    dtopk20 = get_topk(k, ddiab20)
    dtopk30 = get_topk(k, ddiab30)
    dtopk40 = get_topk(k, ddiab40)
    dtopk50 = get_topk(k, ddiab50)
    dtopk60 = get_topk(k, ddiab60)
    dtopk70 = get_topk(k, ddiab70)
    dtopk80 = get_topk(k, ddiab80)
    dtopk90 = get_topk(k, ddiab90)

    hasil_ideal = get_unique(k, file)
    hasilddiab10 = get_unique(k, ddiab10)
    hasilddiab20 = get_unique(k, ddiab10)
    hasilddiab30 = get_unique(k, ddiab10)
    hasilddiab40 = get_unique(k, ddiab10)
    hasilddiab50 = get_unique(k, ddiab10)
    hasilddiab60 = get_unique(k, ddiab10)
    hasilddiab70 = get_unique(k, ddiab10)
    hasilddiab80 = get_unique(k, ddiab10)
    hasilddiab90 = get_unique(k, ddiab10)

    #print(hasil_ideal, len(hasil_ideal[0][0]),len(hasil_ideal[1][0]),len(hasil_ideal[2][0]))
    print(len(hasilddiab10[0][0]),len(hasilddiab10[1][0]),len(hasilddiab10[2][0]))
    print(hasilddiab20)
    print(hasilddiab30)
    print(hasilddiab40)
    print(hasilddiab50)
    print(hasilddiab60)
    print(hasilddiab70)
    print(hasilddiab80)
    print(hasilddiab90, len(hasilddiab90[0][0]),len(hasilddiab90[1][0]),len(hasilddiab90[2][0]))