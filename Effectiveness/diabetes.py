# -*- coding: utf-8 -*-
import pandas as pd

def data():
    db_name = 'seedb_data'
    table = "ddiab10"

    data_set = {
        'race': [('sum', 'time_in_hospital'), ('sum', 'num_lab_procedures'), ('sum', 'num_procedures'),
                 ('sum', 'num_medications'), ('sum', 'number_outpatient'), ('sum', 'number_emergency'),
                 ('sum', 'number_inpatient'), ('sum', 'number_diagnoses'), ('avg', 'time_in_hospital'),
                 ('avg', 'num_lab_procedures'), ('avg', 'num_procedures'), ('avg', 'num_medications'),
                 ('avg', 'number_outpatient'), ('avg', 'number_emergency'), ('avg', 'number_inpatient'),
                 ('avg', 'number_diagnoses'), ('max', 'time_in_hospital'), ('max', 'num_lab_procedures'),
                 ('max', 'num_procedures'), ('max', 'num_medications'), ('max', 'number_outpatient'),
                 ('max', 'number_emergency'), ('max', 'number_inpatient'), ('max', 'number_diagnoses')],
        'gender': [('sum', 'time_in_hospital'), ('sum', 'num_lab_procedures'), ('sum', 'num_procedures'),
                   ('sum', 'num_medications'), ('sum', 'number_outpatient'), ('sum', 'number_emergency'),
                   ('sum', 'number_inpatient'), ('sum', 'number_diagnoses'), ('avg', 'time_in_hospital'),
                   ('avg', 'num_lab_procedures'), ('avg', 'num_procedures'), ('avg', 'num_medications'),
                   ('avg', 'number_outpatient'), ('avg', 'number_emergency'), ('avg', 'number_inpatient'),
                   ('avg', 'number_diagnoses'), ('max', 'time_in_hospital'), ('max', 'num_lab_procedures'),
                   ('max', 'num_procedures'), ('max', 'num_medications'), ('max', 'number_outpatient'),
                   ('max', 'number_emergency'), ('max', 'number_inpatient'), ('max', 'number_diagnoses')],
        'age': [('sum', 'time_in_hospital'), ('sum', 'num_lab_procedures'), ('sum', 'num_procedures'),
                ('sum', 'num_medications'), ('sum', 'number_outpatient'), ('sum', 'number_emergency'),
                ('sum', 'number_inpatient'), ('sum', 'number_diagnoses'), ('avg', 'time_in_hospital'),
                ('avg', 'num_lab_procedures'), ('avg', 'num_procedures'), ('avg', 'num_medications'),
                ('avg', 'number_outpatient'), ('avg', 'number_emergency'), ('avg', 'number_inpatient'),
                ('avg', 'number_diagnoses'), ('max', 'time_in_hospital'), ('max', 'num_lab_procedures'),
                ('max', 'num_procedures'), ('max', 'num_medications'), ('max', 'number_outpatient'),
                ('max', 'number_emergency'), ('max', 'number_inpatient'), ('max', 'number_diagnoses')],
        'diag_1': [('sum', 'time_in_hospital'), ('sum', 'num_lab_procedures'), ('sum', 'num_procedures'),
                   ('sum', 'num_medications'), ('sum', 'number_outpatient'), ('sum', 'number_emergency'),
                   ('sum', 'number_inpatient'), ('sum', 'number_diagnoses'), ('avg', 'time_in_hospital'),
                   ('avg', 'num_lab_procedures'), ('avg', 'num_procedures'), ('avg', 'num_medications'),
                   ('avg', 'number_outpatient'), ('avg', 'number_emergency'), ('avg', 'number_inpatient'),
                   ('avg', 'number_diagnoses'), ('max', 'time_in_hospital'), ('max', 'num_lab_procedures'),
                   ('max', 'num_procedures'), ('max', 'num_medications'), ('max', 'number_outpatient'),
                   ('max', 'number_emergency'), ('max', 'number_inpatient'), ('max', 'number_diagnoses')],
        'diag_2': [('sum', 'time_in_hospital'), ('sum', 'num_lab_procedures'), ('sum', 'num_procedures'),
                   ('sum', 'num_medications'), ('sum', 'number_outpatient'), ('sum', 'number_emergency'),
                   ('sum', 'number_inpatient'), ('sum', 'number_diagnoses'), ('avg', 'time_in_hospital'),
                   ('avg', 'num_lab_procedures'), ('avg', 'num_procedures'), ('avg', 'num_medications'),
                   ('avg', 'number_outpatient'), ('avg', 'number_emergency'), ('avg', 'number_inpatient'),
                   ('avg', 'number_diagnoses'), ('max', 'time_in_hospital'), ('max', 'num_lab_procedures'),
                   ('max', 'num_procedures'), ('max', 'num_medications'), ('max', 'number_outpatient'),
                   ('max', 'number_emergency'), ('max', 'number_inpatient'), ('max', 'number_diagnoses')],
        'diag_3': [('sum', 'time_in_hospital'), ('sum', 'num_lab_procedures'), ('sum', 'num_procedures'),
                   ('sum', 'num_medications'), ('sum', 'number_outpatient'), ('sum', 'number_emergency'),
                   ('sum', 'number_inpatient'), ('sum', 'number_diagnoses'), ('avg', 'time_in_hospital'),
                   ('avg', 'num_lab_procedures'), ('avg', 'num_procedures'), ('avg', 'num_medications'),
                   ('avg', 'number_outpatient'), ('avg', 'number_emergency'), ('avg', 'number_inpatient'),
                   ('avg', 'number_diagnoses'), ('max', 'time_in_hospital'), ('max', 'num_lab_procedures'),
                   ('max', 'num_procedures'), ('max', 'num_medications'), ('max', 'number_outpatient'),
                   ('max', 'number_emergency'), ('max', 'number_inpatient'), ('max', 'number_diagnoses')],
        'max_glu_serum': [('sum', 'time_in_hospital'), ('sum', 'num_lab_procedures'), ('sum', 'num_procedures'),
                          ('sum', 'num_medications'), ('sum', 'number_outpatient'), ('sum', 'number_emergency'),
                          ('sum', 'number_inpatient'), ('sum', 'number_diagnoses'), ('avg', 'time_in_hospital'),
                          ('avg', 'num_lab_procedures'), ('avg', 'num_procedures'), ('avg', 'num_medications'),
                          ('avg', 'number_outpatient'), ('avg', 'number_emergency'), ('avg', 'number_inpatient'),
                          ('avg', 'number_diagnoses'), ('max', 'time_in_hospital'), ('max', 'num_lab_procedures'),
                          ('max', 'num_procedures'), ('max', 'num_medications'), ('max', 'number_outpatient'),
                          ('max', 'number_emergency'), ('max', 'number_inpatient'), ('max', 'number_diagnoses')],
        'a1cresult': [('sum', 'time_in_hospital'), ('sum', 'num_lab_procedures'), ('sum', 'num_procedures'),
                      ('sum', 'num_medications'), ('sum', 'number_outpatient'), ('sum', 'number_emergency'),
                      ('sum', 'number_inpatient'), ('sum', 'number_diagnoses'), ('avg', 'time_in_hospital'),
                      ('avg', 'num_lab_procedures'), ('avg', 'num_procedures'), ('avg', 'num_medications'),
                      ('avg', 'number_outpatient'), ('avg', 'number_emergency'), ('avg', 'number_inpatient'),
                      ('avg', 'number_diagnoses'), ('max', 'time_in_hospital'), ('max', 'num_lab_procedures'),
                      ('max', 'num_procedures'), ('max', 'num_medications'), ('max', 'number_outpatient'),
                      ('max', 'number_emergency'), ('max', 'number_inpatient'), ('max', 'number_diagnoses')],
        'metformin': [('sum', 'time_in_hospital'), ('sum', 'num_lab_procedures'), ('sum', 'num_procedures'),
                      ('sum', 'num_medications'), ('sum', 'number_outpatient'), ('sum', 'number_emergency'),
                      ('sum', 'number_inpatient'), ('sum', 'number_diagnoses'), ('avg', 'time_in_hospital'),
                      ('avg', 'num_lab_procedures'), ('avg', 'num_procedures'), ('avg', 'num_medications'),
                      ('avg', 'number_outpatient'), ('avg', 'number_emergency'), ('avg', 'number_inpatient'),
                      ('avg', 'number_diagnoses'), ('max', 'time_in_hospital'), ('max', 'num_lab_procedures'),
                      ('max', 'num_procedures'), ('max', 'num_medications'), ('max', 'number_outpatient'),
                      ('max', 'number_emergency'), ('max', 'number_inpatient'), ('max', 'number_diagnoses')],
        'repaglinide': [('sum', 'time_in_hospital'), ('sum', 'num_lab_procedures'), ('sum', 'num_procedures'),
                        ('sum', 'num_medications'), ('sum', 'number_outpatient'), ('sum', 'number_emergency'),
                        ('sum', 'number_inpatient'), ('sum', 'number_diagnoses'), ('avg', 'time_in_hospital'),
                        ('avg', 'num_lab_procedures'), ('avg', 'num_procedures'), ('avg', 'num_medications'),
                        ('avg', 'number_outpatient'), ('avg', 'number_emergency'), ('avg', 'number_inpatient'),
                        ('avg', 'number_diagnoses'), ('max', 'time_in_hospital'), ('max', 'num_lab_procedures'),
                        ('max', 'num_procedures'), ('max', 'num_medications'), ('max', 'number_outpatient'),
                        ('max', 'number_emergency'), ('max', 'number_inpatient'), ('max', 'number_diagnoses')],
        'nateglinide': [('sum', 'time_in_hospital'), ('sum', 'num_lab_procedures'), ('sum', 'num_procedures'),
                        ('sum', 'num_medications'), ('sum', 'number_outpatient'), ('sum', 'number_emergency'),
                        ('sum', 'number_inpatient'), ('sum', 'number_diagnoses'), ('avg', 'time_in_hospital'),
                        ('avg', 'num_lab_procedures'), ('avg', 'num_procedures'), ('avg', 'num_medications'),
                        ('avg', 'number_outpatient'), ('avg', 'number_emergency'), ('avg', 'number_inpatient'),
                        ('avg', 'number_diagnoses'), ('max', 'time_in_hospital'), ('max', 'num_lab_procedures'),
                        ('max', 'num_procedures'), ('max', 'num_medications'), ('max', 'number_outpatient'),
                        ('max', 'number_emergency'), ('max', 'number_inpatient'), ('max', 'number_diagnoses')],
        'chlorpropamide': [('sum', 'time_in_hospital'), ('sum', 'num_lab_procedures'), ('sum', 'num_procedures'),
                           ('sum', 'num_medications'), ('sum', 'number_outpatient'), ('sum', 'number_emergency'),
                           ('sum', 'number_inpatient'), ('sum', 'number_diagnoses'), ('avg', 'time_in_hospital'),
                           ('avg', 'num_lab_procedures'), ('avg', 'num_procedures'), ('avg', 'num_medications'),
                           ('avg', 'number_outpatient'), ('avg', 'number_emergency'), ('avg', 'number_inpatient'),
                           ('avg', 'number_diagnoses'), ('max', 'time_in_hospital'), ('max', 'num_lab_procedures'),
                           ('max', 'num_procedures'), ('max', 'num_medications'), ('max', 'number_outpatient'),
                           ('max', 'number_emergency'), ('max', 'number_inpatient'), ('max', 'number_diagnoses')],
        'glimepiride': [('sum', 'time_in_hospital'), ('sum', 'num_lab_procedures'), ('sum', 'num_procedures'),
                        ('sum', 'num_medications'), ('sum', 'number_outpatient'), ('sum', 'number_emergency'),
                        ('sum', 'number_inpatient'), ('sum', 'number_diagnoses'), ('avg', 'time_in_hospital'),
                        ('avg', 'num_lab_procedures'), ('avg', 'num_procedures'), ('avg', 'num_medications'),
                        ('avg', 'number_outpatient'), ('avg', 'number_emergency'), ('avg', 'number_inpatient'),
                        ('avg', 'number_diagnoses'), ('max', 'time_in_hospital'), ('max', 'num_lab_procedures'),
                        ('max', 'num_procedures'), ('max', 'num_medications'), ('max', 'number_outpatient'),
                        ('max', 'number_emergency'), ('max', 'number_inpatient'), ('max', 'number_diagnoses')],
        'acetohexamide': [('sum', 'time_in_hospital'), ('sum', 'num_lab_procedures'), ('sum', 'num_procedures'),
                          ('sum', 'num_medications'), ('sum', 'number_outpatient'), ('sum', 'number_emergency'),
                          ('sum', 'number_inpatient'), ('sum', 'number_diagnoses'), ('avg', 'time_in_hospital'),
                          ('avg', 'num_lab_procedures'), ('avg', 'num_procedures'), ('avg', 'num_medications'),
                          ('avg', 'number_outpatient'), ('avg', 'number_emergency'), ('avg', 'number_inpatient'),
                          ('avg', 'number_diagnoses'), ('max', 'time_in_hospital'), ('max', 'num_lab_procedures'),
                          ('max', 'num_procedures'), ('max', 'num_medications'), ('max', 'number_outpatient'),
                          ('max', 'number_emergency'), ('max', 'number_inpatient'), ('max', 'number_diagnoses')],
        'glipizide': [('sum', 'time_in_hospital'), ('sum', 'num_lab_procedures'), ('sum', 'num_procedures'),
                      ('sum', 'num_medications'), ('sum', 'number_outpatient'), ('sum', 'number_emergency'),
                      ('sum', 'number_inpatient'), ('sum', 'number_diagnoses'), ('avg', 'time_in_hospital'),
                      ('avg', 'num_lab_procedures'), ('avg', 'num_procedures'), ('avg', 'num_medications'),
                      ('avg', 'number_outpatient'), ('avg', 'number_emergency'), ('avg', 'number_inpatient'),
                      ('avg', 'number_diagnoses'), ('max', 'time_in_hospital'), ('max', 'num_lab_procedures'),
                      ('max', 'num_procedures'), ('max', 'num_medications'), ('max', 'number_outpatient'),
                      ('max', 'number_emergency'), ('max', 'number_inpatient'), ('max', 'number_diagnoses')],
        'glyburide': [('sum', 'time_in_hospital'), ('sum', 'num_lab_procedures'), ('sum', 'num_procedures'),
                      ('sum', 'num_medications'), ('sum', 'number_outpatient'), ('sum', 'number_emergency'),
                      ('sum', 'number_inpatient'), ('sum', 'number_diagnoses'), ('avg', 'time_in_hospital'),
                      ('avg', 'num_lab_procedures'), ('avg', 'num_procedures'), ('avg', 'num_medications'),
                      ('avg', 'number_outpatient'), ('avg', 'number_emergency'), ('avg', 'number_inpatient'),
                      ('avg', 'number_diagnoses'), ('max', 'time_in_hospital'), ('max', 'num_lab_procedures'),
                      ('max', 'num_procedures'), ('max', 'num_medications'), ('max', 'number_outpatient'),
                      ('max', 'number_emergency'), ('max', 'number_inpatient'), ('max', 'number_diagnoses')],
        'tolbutamide': [('sum', 'time_in_hospital'), ('sum', 'num_lab_procedures'), ('sum', 'num_procedures'),
                        ('sum', 'num_medications'), ('sum', 'number_outpatient'), ('sum', 'number_emergency'),
                        ('sum', 'number_inpatient'), ('sum', 'number_diagnoses'), ('avg', 'time_in_hospital'),
                        ('avg', 'num_lab_procedures'), ('avg', 'num_procedures'), ('avg', 'num_medications'),
                        ('avg', 'number_outpatient'), ('avg', 'number_emergency'), ('avg', 'number_inpatient'),
                        ('avg', 'number_diagnoses'), ('max', 'time_in_hospital'), ('max', 'num_lab_procedures'),
                        ('max', 'num_procedures'), ('max', 'num_medications'), ('max', 'number_outpatient'),
                        ('max', 'number_emergency'), ('max', 'number_inpatient'), ('max', 'number_diagnoses')],
        'pioglitazone': [('sum', 'time_in_hospital'), ('sum', 'num_lab_procedures'), ('sum', 'num_procedures'),
                         ('sum', 'num_medications'), ('sum', 'number_outpatient'), ('sum', 'number_emergency'),
                         ('sum', 'number_inpatient'), ('sum', 'number_diagnoses'), ('avg', 'time_in_hospital'),
                         ('avg', 'num_lab_procedures'), ('avg', 'num_procedures'), ('avg', 'num_medications'),
                         ('avg', 'number_outpatient'), ('avg', 'number_emergency'), ('avg', 'number_inpatient'),
                         ('avg', 'number_diagnoses'), ('max', 'time_in_hospital'), ('max', 'num_lab_procedures'),
                         ('max', 'num_procedures'), ('max', 'num_medications'), ('max', 'number_outpatient'),
                         ('max', 'number_emergency'), ('max', 'number_inpatient'), ('max', 'number_diagnoses')],
        'rosiglitazone': [('sum', 'time_in_hospital'), ('sum', 'num_lab_procedures'), ('sum', 'num_procedures'),
                          ('sum', 'num_medications'), ('sum', 'number_outpatient'), ('sum', 'number_emergency'),
                          ('sum', 'number_inpatient'), ('sum', 'number_diagnoses'), ('avg', 'time_in_hospital'),
                          ('avg', 'num_lab_procedures'), ('avg', 'num_procedures'), ('avg', 'num_medications'),
                          ('avg', 'number_outpatient'), ('avg', 'number_emergency'), ('avg', 'number_inpatient'),
                          ('avg', 'number_diagnoses'), ('max', 'time_in_hospital'), ('max', 'num_lab_procedures'),
                          ('max', 'num_procedures'), ('max', 'num_medications'), ('max', 'number_outpatient'),
                          ('max', 'number_emergency'), ('max', 'number_inpatient'), ('max', 'number_diagnoses')],
        'acarbose': [('sum', 'time_in_hospital'), ('sum', 'num_lab_procedures'), ('sum', 'num_procedures'),
                     ('sum', 'num_medications'), ('sum', 'number_outpatient'), ('sum', 'number_emergency'),
                     ('sum', 'number_inpatient'), ('sum', 'number_diagnoses'), ('avg', 'time_in_hospital'),
                     ('avg', 'num_lab_procedures'), ('avg', 'num_procedures'), ('avg', 'num_medications'),
                     ('avg', 'number_outpatient'), ('avg', 'number_emergency'), ('avg', 'number_inpatient'),
                     ('avg', 'number_diagnoses'), ('max', 'time_in_hospital'), ('max', 'num_lab_procedures'),
                     ('max', 'num_procedures'), ('max', 'num_medications'), ('max', 'number_outpatient'),
                     ('max', 'number_emergency'), ('max', 'number_inpatient'), ('max', 'number_diagnoses')],
        'miglitol': [('sum', 'time_in_hospital'), ('sum', 'num_lab_procedures'), ('sum', 'num_procedures'),
                     ('sum', 'num_medications'), ('sum', 'number_outpatient'), ('sum', 'number_emergency'),
                     ('sum', 'number_inpatient'), ('sum', 'number_diagnoses'), ('avg', 'time_in_hospital'),
                     ('avg', 'num_lab_procedures'), ('avg', 'num_procedures'), ('avg', 'num_medications'),
                     ('avg', 'number_outpatient'), ('avg', 'number_emergency'), ('avg', 'number_inpatient'),
                     ('avg', 'number_diagnoses'), ('max', 'time_in_hospital'), ('max', 'num_lab_procedures'),
                     ('max', 'num_procedures'), ('max', 'num_medications'), ('max', 'number_outpatient'),
                     ('max', 'number_emergency'), ('max', 'number_inpatient'), ('max', 'number_diagnoses')],
        'troglitazone': [('sum', 'time_in_hospital'), ('sum', 'num_lab_procedures'), ('sum', 'num_procedures'),
                         ('sum', 'num_medications'), ('sum', 'number_outpatient'), ('sum', 'number_emergency'),
                         ('sum', 'number_inpatient'), ('sum', 'number_diagnoses'), ('avg', 'time_in_hospital'),
                         ('avg', 'num_lab_procedures'), ('avg', 'num_procedures'), ('avg', 'num_medications'),
                         ('avg', 'number_outpatient'), ('avg', 'number_emergency'), ('avg', 'number_inpatient'),
                         ('avg', 'number_diagnoses'), ('max', 'time_in_hospital'), ('max', 'num_lab_procedures'),
                         ('max', 'num_procedures'), ('max', 'num_medications'), ('max', 'number_outpatient'),
                         ('max', 'number_emergency'), ('max', 'number_inpatient'), ('max', 'number_diagnoses')],
        'tolazamide': [('sum', 'time_in_hospital'), ('sum', 'num_lab_procedures'), ('sum', 'num_procedures'),
                       ('sum', 'num_medications'), ('sum', 'number_outpatient'), ('sum', 'number_emergency'),
                       ('sum', 'number_inpatient'), ('sum', 'number_diagnoses'), ('avg', 'time_in_hospital'),
                       ('avg', 'num_lab_procedures'), ('avg', 'num_procedures'), ('avg', 'num_medications'),
                       ('avg', 'number_outpatient'), ('avg', 'number_emergency'), ('avg', 'number_inpatient'),
                       ('avg', 'number_diagnoses'), ('max', 'time_in_hospital'), ('max', 'num_lab_procedures'),
                       ('max', 'num_procedures'), ('max', 'num_medications'), ('max', 'number_outpatient'),
                       ('max', 'number_emergency'), ('max', 'number_inpatient'), ('max', 'number_diagnoses')],
        'examide': [('sum', 'time_in_hospital'), ('sum', 'num_lab_procedures'), ('sum', 'num_procedures'),
                    ('sum', 'num_medications'), ('sum', 'number_outpatient'), ('sum', 'number_emergency'),
                    ('sum', 'number_inpatient'), ('sum', 'number_diagnoses'), ('avg', 'time_in_hospital'),
                    ('avg', 'num_lab_procedures'), ('avg', 'num_procedures'), ('avg', 'num_medications'),
                    ('avg', 'number_outpatient'), ('avg', 'number_emergency'), ('avg', 'number_inpatient'),
                    ('avg', 'number_diagnoses'), ('max', 'time_in_hospital'), ('max', 'num_lab_procedures'),
                    ('max', 'num_procedures'), ('max', 'num_medications'), ('max', 'number_outpatient'),
                    ('max', 'number_emergency'), ('max', 'number_inpatient'), ('max', 'number_diagnoses')],
        'citoglipton': [('sum', 'time_in_hospital'), ('sum', 'num_lab_procedures'), ('sum', 'num_procedures'),
                        ('sum', 'num_medications'), ('sum', 'number_outpatient'), ('sum', 'number_emergency'),
                        ('sum', 'number_inpatient'), ('sum', 'number_diagnoses'), ('avg', 'time_in_hospital'),
                        ('avg', 'num_lab_procedures'), ('avg', 'num_procedures'), ('avg', 'num_medications'),
                        ('avg', 'number_outpatient'), ('avg', 'number_emergency'), ('avg', 'number_inpatient'),
                        ('avg', 'number_diagnoses'), ('max', 'time_in_hospital'), ('max', 'num_lab_procedures'),
                        ('max', 'num_procedures'), ('max', 'num_medications'), ('max', 'number_outpatient'),
                        ('max', 'number_emergency'), ('max', 'number_inpatient'), ('max', 'number_diagnoses')],
        'insulin': [('sum', 'time_in_hospital'), ('sum', 'num_lab_procedures'), ('sum', 'num_procedures'),
                    ('sum', 'num_medications'), ('sum', 'number_outpatient'), ('sum', 'number_emergency'),
                    ('sum', 'number_inpatient'), ('sum', 'number_diagnoses'), ('avg', 'time_in_hospital'),
                    ('avg', 'num_lab_procedures'), ('avg', 'num_procedures'), ('avg', 'num_medications'),
                    ('avg', 'number_outpatient'), ('avg', 'number_emergency'), ('avg', 'number_inpatient'),
                    ('avg', 'number_diagnoses'), ('max', 'time_in_hospital'), ('max', 'num_lab_procedures'),
                    ('max', 'num_procedures'), ('max', 'num_medications'), ('max', 'number_outpatient'),
                    ('max', 'number_emergency'), ('max', 'number_inpatient'), ('max', 'number_diagnoses')],
        'glyburide_metformin': [('sum', 'time_in_hospital'), ('sum', 'num_lab_procedures'), ('sum', 'num_procedures'),
                                ('sum', 'num_medications'), ('sum', 'number_outpatient'), ('sum', 'number_emergency'),
                                ('sum', 'number_inpatient'), ('sum', 'number_diagnoses'), ('avg', 'time_in_hospital'),
                                ('avg', 'num_lab_procedures'), ('avg', 'num_procedures'), ('avg', 'num_medications'),
                                ('avg', 'number_outpatient'), ('avg', 'number_emergency'), ('avg', 'number_inpatient'),
                                ('avg', 'number_diagnoses'), ('max', 'time_in_hospital'), ('max', 'num_lab_procedures'),
                                ('max', 'num_procedures'), ('max', 'num_medications'), ('max', 'number_outpatient'),
                                ('max', 'number_emergency'), ('max', 'number_inpatient'), ('max', 'number_diagnoses')],
        'glipizide_metformin': [('sum', 'time_in_hospital'), ('sum', 'num_lab_procedures'), ('sum', 'num_procedures'),
                                ('sum', 'num_medications'), ('sum', 'number_outpatient'), ('sum', 'number_emergency'),
                                ('sum', 'number_inpatient'), ('sum', 'number_diagnoses'), ('avg', 'time_in_hospital'),
                                ('avg', 'num_lab_procedures'), ('avg', 'num_procedures'), ('avg', 'num_medications'),
                                ('avg', 'number_outpatient'), ('avg', 'number_emergency'), ('avg', 'number_inpatient'),
                                ('avg', 'number_diagnoses'), ('max', 'time_in_hospital'), ('max', 'num_lab_procedures'),
                                ('max', 'num_procedures'), ('max', 'num_medications'), ('max', 'number_outpatient'),
                                ('max', 'number_emergency'), ('max', 'number_inpatient'), ('max', 'number_diagnoses')],
        'glimepiride_pioglitazone': [('sum', 'time_in_hospital'), ('sum', 'num_lab_procedures'),
                                     ('sum', 'num_procedures'), ('sum', 'num_medications'),
                                     ('sum', 'number_outpatient'), ('sum', 'number_emergency'),
                                     ('sum', 'number_inpatient'), ('sum', 'number_diagnoses'),
                                     ('avg', 'time_in_hospital'), ('avg', 'num_lab_procedures'),
                                     ('avg', 'num_procedures'), ('avg', 'num_medications'),
                                     ('avg', 'number_outpatient'), ('avg', 'number_emergency'),
                                     ('avg', 'number_inpatient'), ('avg', 'number_diagnoses'),
                                     ('max', 'time_in_hospital'), ('max', 'num_lab_procedures'),
                                     ('max', 'num_procedures'), ('max', 'num_medications'),
                                     ('max', 'number_outpatient'), ('max', 'number_emergency'),
                                     ('max', 'number_inpatient'), ('max', 'number_diagnoses')],
        'metformin_rosiglitazone': [('sum', 'time_in_hospital'), ('sum', 'num_lab_procedures'),
                                    ('sum', 'num_procedures'), ('sum', 'num_medications'), ('sum', 'number_outpatient'),
                                    ('sum', 'number_emergency'), ('sum', 'number_inpatient'),
                                    ('sum', 'number_diagnoses'), ('avg', 'time_in_hospital'),
                                    ('avg', 'num_lab_procedures'), ('avg', 'num_procedures'),
                                    ('avg', 'num_medications'), ('avg', 'number_outpatient'),
                                    ('avg', 'number_emergency'), ('avg', 'number_inpatient'),
                                    ('avg', 'number_diagnoses'), ('max', 'time_in_hospital'),
                                    ('max', 'num_lab_procedures'), ('max', 'num_procedures'),
                                    ('max', 'num_medications'), ('max', 'number_outpatient'),
                                    ('max', 'number_emergency'), ('max', 'number_inpatient'),
                                    ('max', 'number_diagnoses')],
        'metformin_pioglitazone': [('sum', 'time_in_hospital'), ('sum', 'num_lab_procedures'),
                                   ('sum', 'num_procedures'), ('sum', 'num_medications'), ('sum', 'number_outpatient'),
                                   ('sum', 'number_emergency'), ('sum', 'number_inpatient'),
                                   ('sum', 'number_diagnoses'), ('avg', 'time_in_hospital'),
                                   ('avg', 'num_lab_procedures'), ('avg', 'num_procedures'), ('avg', 'num_medications'),
                                   ('avg', 'number_outpatient'), ('avg', 'number_emergency'),
                                   ('avg', 'number_inpatient'), ('avg', 'number_diagnoses'),
                                   ('max', 'time_in_hospital'), ('max', 'num_lab_procedures'),
                                   ('max', 'num_procedures'), ('max', 'num_medications'), ('max', 'number_outpatient'),
                                   ('max', 'number_emergency'), ('max', 'number_inpatient'),
                                   ('max', 'number_diagnoses')],
        'change': [('sum', 'time_in_hospital'), ('sum', 'num_lab_procedures'), ('sum', 'num_procedures'),
                   ('sum', 'num_medications'), ('sum', 'number_outpatient'), ('sum', 'number_emergency'),
                   ('sum', 'number_inpatient'), ('sum', 'number_diagnoses'), ('avg', 'time_in_hospital'),
                   ('avg', 'num_lab_procedures'), ('avg', 'num_procedures'), ('avg', 'num_medications'),
                   ('avg', 'number_outpatient'), ('avg', 'number_emergency'), ('avg', 'number_inpatient'),
                   ('avg', 'number_diagnoses'), ('max', 'time_in_hospital'), ('max', 'num_lab_procedures'),
                   ('max', 'num_procedures'), ('max', 'num_medications'), ('max', 'number_outpatient'),
                   ('max', 'number_emergency'), ('max', 'number_inpatient'), ('max', 'number_diagnoses')],
        'diabetesmed': [('sum', 'time_in_hospital'), ('sum', 'num_lab_procedures'), ('sum', 'num_procedures'),
                        ('sum', 'num_medications'), ('sum', 'number_outpatient'), ('sum', 'number_emergency'),
                        ('sum', 'number_inpatient'), ('sum', 'number_diagnoses'), ('avg', 'time_in_hospital'),
                        ('avg', 'num_lab_procedures'), ('avg', 'num_procedures'), ('avg', 'num_medications'),
                        ('avg', 'number_outpatient'), ('avg', 'number_emergency'), ('avg', 'number_inpatient'),
                        ('avg', 'number_diagnoses'), ('max', 'time_in_hospital'), ('max', 'num_lab_procedures'),
                        ('max', 'num_procedures'), ('max', 'num_medications'), ('max', 'number_outpatient'),
                        ('max', 'number_emergency'), ('max', 'number_inpatient'), ('max', 'number_diagnoses')],
        'readmitted': [('sum', 'time_in_hospital'), ('sum', 'num_lab_procedures'), ('sum', 'num_procedures'),
                       ('sum', 'num_medications'), ('sum', 'number_outpatient'), ('sum', 'number_emergency'),
                       ('sum', 'number_inpatient'), ('sum', 'number_diagnoses'), ('avg', 'time_in_hospital'),
                       ('avg', 'num_lab_procedures'), ('avg', 'num_procedures'), ('avg', 'num_medications'),
                       ('avg', 'number_outpatient'), ('avg', 'number_emergency'), ('avg', 'number_inpatient'),
                       ('avg', 'number_diagnoses'), ('max', 'time_in_hospital'), ('max', 'num_lab_procedures'),
                       ('max', 'num_procedures'), ('max', 'num_medications'), ('max', 'number_outpatient'),
                       ('max', 'number_emergency'), ('max', 'number_inpatient'), ('max', 'number_diagnoses')]
    }
    
    return db_name,table,data_set

if __name__ == '__main__':
    print(00)

# A = 34
# M = 8
# F = 3 (avg, sum, max)
# tot = 34*8*3 = 816 views

#dim = 42