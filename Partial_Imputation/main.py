# -*- coding: utf-8 -*-
from seedb import SeeDB
from diabetes import data

if __name__ == "__main__":
    top_k = 10

    list_table = ['db_50diab1',
                  'db_50diab2',
                  'db_50diab3',
                  'db_50diab4',
                  'db_50diab5',
                  'db_50diab6',
                  'db_50diab7',
                  'db_50diab8',
                  'db_50diab9',
                  'db_50diab10']

    for table_name in list_table:
        db, table, data_set = data(table_name)
        print("running with db {}".format(table_name))
        framework = SeeDB(db, data_set, table, top_k)
        framework.main()
        print("done")

    # import time
    # print("start... generate partial insights from ", table)
    # start_time = time.time()
    # framework = SeeDB(db,data_set,table,top_k)
    # framework.main()
    # print("--- %s seconds ---" % (time.time() - start_time))
    #
