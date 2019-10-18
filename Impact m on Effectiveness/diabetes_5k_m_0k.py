# -*- coding: utf-8 -*-
import pandas as pd


def data(table):
    db_name = 'diab_experiment'
    table = table

    data_set = {
                'miglitol': [('avg','time_in_hospital'),('avg','num_procedures'),('avg','number_outpatient'),('avg','number_inpatient')],
                'acarbose': [('avg','time_in_hospital'),('avg','num_procedures'),('avg','number_outpatient'),('avg','number_inpatient')],
                'acetohexamide': [('avg','time_in_hospital'),('avg','num_procedures'),('avg','number_outpatient'),('avg','number_inpatient')],
                'glimepiride_pioglitazone': [('avg','time_in_hospital'),('avg','num_procedures'),('avg','number_outpatient'),('avg','number_inpatient')]
                  }

    return db_name, table, data_set


if __name__ == '__main__':
    print(00)

# A = 11
# M = 7
# dim = 18
# F = 2
# total = 11*7*2= 154 views



