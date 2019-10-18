# -*- coding: utf-8 -*-
from a_seedb_function import SeeDB
from a_seedb_db import data


if __name__ == "__main__":

    top_k = 10
    #atr = ['race', 'gender', 'age']
    atr = ['race', 'gender', 'age', 'admission_type_id',
        'discharge_disposition_id', 'admission_source_id', 'diag_1',
        'max_glu_serum', 'a1cresult', 'insulin', 'change', 'diabetesmed',
        'readmitted']
    #measure = ['time_in_hospital', 'num_lab_procedures', 'num_procedures']
    measure = ['time_in_hospital', 'num_lab_procedures', 'num_procedures',
               'num_medications', 'number_outpatient', 'number_emergency',
               'number_inpatient', 'number_diagnoses']

    func = ['sum', 'avg', 'max', 'count']

    mytable = ['db_10nodropnan_attr1', 'db_10nodropnan_measure1', 'db_10nodropnan_a_m1']
    for i in mytable:
        db, table, data_set = data(i[0], atr, measure, func)
        print("running with db {}".format(i[0]))
        framework = SeeDB(db,data_set,table,top_k)
        framework.main()
        print("done")
    # table = 'diabetes_v2'
    # db, table, data_set = data(table, atr, measure, func)
    # print("running with db {}".format(table))
    # framework = SeeDB(db,data_set,table,top_k)
    # framework.main()
    # print("done")