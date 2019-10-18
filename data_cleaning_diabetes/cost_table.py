# -*- coding: utf-8 -*-
import pandas as pd

def data(table):
    db_name = 'seedb_data'
    table = table

    data_set = {
        'diag_1': [('avg','time_in_hospital'),('avg','num_lab_procedures'),('avg','num_procedures'),('avg','num_medications'),('avg','number_outpatient'),('avg','number_emergency'),('avg','number_inpatient')],
        'diag_2': [('avg','time_in_hospital'),('avg','num_lab_procedures'),('avg','num_procedures'),('avg','num_medications'),('avg','number_outpatient'),('avg','number_emergency'),('avg','number_inpatient')],
        'diag_3': [('avg','time_in_hospital'),('avg','num_lab_procedures'),('avg','num_procedures'),('avg','num_medications'),('avg','number_outpatient'),('avg','number_emergency'),('avg','number_inpatient')],
        'acetohexamide': [('avg','time_in_hospital'),('avg','num_lab_procedures'),('avg','num_procedures'),('avg','num_medications'),('avg','number_outpatient'),('avg','number_emergency'),('avg','number_inpatient')],
        'miglitol': [('avg','time_in_hospital'),('avg','num_lab_procedures'),('avg','num_procedures'),('avg','num_medications'),('avg','number_outpatient'),('avg','number_emergency'),('avg','number_inpatient')],
        'glimepiride_pioglitazone': [('avg','time_in_hospital'),('avg','num_lab_procedures'),('avg','num_procedures'),('avg','num_medications'),('avg','number_outpatient'),('avg','number_emergency'),('avg','number_inpatient')]
    }
    
    return db_name,table,data_set

if __name__ == '__main__':
    print(00)

# A = 34
# M = 8
# F = 3
# 816 views



