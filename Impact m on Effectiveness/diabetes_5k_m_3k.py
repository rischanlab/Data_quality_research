# -*- coding: utf-8 -*-
import pandas as pd


def data(table):
    db_name = 'diab_experiment'
    table = table

    data_set = {
                'miglitol': [('avg','time_in_hospital'),('avg','num_procedures'),('avg','num_medications'),('avg','number_outpatient'),('avg','number_emergency'),('avg','number_inpatient'), ('avg', 'number_diagnoses'),('max','time_in_hospital'),('max','num_procedures'),('max','num_medications'),('max','number_outpatient'),('max','number_emergency'),('max','number_inpatient'), ('max', 'number_diagnoses')],
                'acarbose': [('avg','time_in_hospital'),('avg','num_procedures'),('avg','num_medications'),('avg','number_outpatient'),('avg','number_emergency'),('avg','number_inpatient'), ('avg', 'number_diagnoses'),('max','time_in_hospital'),('max','num_procedures'),('max','num_medications'),('max','number_outpatient'),('max','number_emergency'),('max','number_inpatient'), ('max', 'number_diagnoses')],
                'acetohexamide': [('avg','time_in_hospital'),('avg','num_procedures'),('avg','num_medications'),('avg','number_outpatient'),('avg','number_emergency'),('avg','number_inpatient'), ('avg', 'number_diagnoses'),('max','time_in_hospital'),('max','num_procedures'),('max','num_medications'),('max','number_outpatient'),('max','number_emergency'),('max','number_inpatient'), ('max', 'number_diagnoses')],
                'glimepiride_pioglitazone': [('avg','time_in_hospital'),('avg','num_procedures'),('avg','num_medications'),('avg','number_outpatient'),('avg','number_emergency'),('avg','number_inpatient'), ('avg', 'number_diagnoses'),('max','time_in_hospital'),('max','num_procedures'),('max','num_medications'),('max','number_outpatient'),('max','number_emergency'),('max','number_inpatient'), ('max', 'number_diagnoses')],
                'diag_3': [('avg','time_in_hospital'),('avg','num_procedures'),('avg','num_medications'),('avg','number_outpatient'),('avg','number_emergency'),('avg','number_inpatient'), ('avg', 'number_diagnoses'),('max','time_in_hospital'),('max','num_procedures'),('max','num_medications'),('max','number_outpatient'),('max','number_emergency'),('max','number_inpatient'), ('max', 'number_diagnoses')],
                'diag_2': [('avg','time_in_hospital'),('avg','num_procedures'),('avg','num_medications'),('avg','number_outpatient'),('avg','number_emergency'),('avg','number_inpatient'), ('avg', 'number_diagnoses'),('max','time_in_hospital'),('max','num_procedures'),('max','num_medications'),('max','number_outpatient'),('max','number_emergency'),('max','number_inpatient'), ('max', 'number_diagnoses')],
                'gender': [('avg','time_in_hospital'),('avg','num_procedures'),('avg','num_medications'),('avg','number_outpatient'),('avg','number_emergency'),('avg','number_inpatient'), ('avg', 'number_diagnoses'),('max','time_in_hospital'),('max','num_procedures'),('max','num_medications'),('max','number_outpatient'),('max','number_emergency'),('max','number_inpatient'), ('max', 'number_diagnoses')],
                'diag_1': [('avg','time_in_hospital'),('avg','num_procedures'),('avg','num_medications'),('avg','number_outpatient'),('avg','number_emergency'),('avg','number_inpatient'), ('avg', 'number_diagnoses'),('max','time_in_hospital'),('max','num_procedures'),('max','num_medications'),('max','number_outpatient'),('max','number_emergency'),('max','number_inpatient'), ('max', 'number_diagnoses')],
                'tolazamide': [('avg','time_in_hospital'),('avg','num_procedures'),('avg','num_medications'),('avg','number_outpatient'),('avg','number_emergency'),('avg','number_inpatient'), ('avg', 'number_diagnoses'),('max','time_in_hospital'),('max','num_procedures'),('max','num_medications'),('max','number_outpatient'),('max','number_emergency'),('max','number_inpatient'), ('max', 'number_diagnoses')],
                'troglitazone': [('avg','time_in_hospital'),('avg','num_procedures'),('avg','num_medications'),('avg','number_outpatient'),('avg','number_emergency'),('avg','number_inpatient'), ('avg', 'number_diagnoses'),('max','time_in_hospital'),('max','num_procedures'),('max','num_medications'),('max','number_outpatient'),('max','number_emergency'),('max','number_inpatient'), ('max', 'number_diagnoses')],
                'age': [('avg','time_in_hospital'),('avg','num_procedures'),('avg','num_medications'),('avg','number_outpatient'),('avg','number_emergency'),('avg','number_inpatient'), ('avg', 'number_diagnoses'),('max','time_in_hospital'),('max','num_procedures'),('max','num_medications'),('max','number_outpatient'),('max','number_emergency'),('max','number_inpatient'), ('max', 'number_diagnoses')]
               }

    return db_name, table, data_set


if __name__ == '__main__':
    print(00)

# A = 11
# M = 7
# dim = 18
# F = 2
# total = 11*7*2= 154 views



