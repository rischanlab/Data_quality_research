# -*- coding: utf-8 -*-
from seedb import SeeDB
from diabetes import data

if __name__ == "__main__":

    top_k = 10
    list_table = ['ddiab10',
                  'ddiab20',
                  'ddiab30',
                  'ddiab40',
                  'ddiab50',
                  'ddiab60',
                  'ddiab70',
                  'ddiab80',
                  'ddiab90',
                  'diab10',
                  'diab20',
                  'diab30',
                  'diab40',
                  'diab50',
                  'diab60',
                  'diab70',
                  'diab80',
                  'diab90'
                  ]

    for i in list_table:
        db, table, data_set = data(i)
        print("running with db {}".format(i))
        framework = SeeDB(db,data_set,table,top_k)
        framework.main()
        print("done")

# list_table = [    'diab10',
#                   'diab20',
#                   'diab30',
#                   'diab40',
#                   'diab50',
#                   'diab60',
#                   'diab70',
#                   'diab80',
#                   'diab90']