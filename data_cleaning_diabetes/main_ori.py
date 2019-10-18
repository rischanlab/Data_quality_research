# -*- coding: utf-8 -*-
from seedb import SeeDB
from diabetes_ori import data

if __name__ == "__main__":
    db,table,data_set = data()

    top_k = 10
    import time

    start_time = time.time()
    framework = SeeDB(db,data_set,table,top_k)
    framework.main()
    print("--- %s seconds ---" % (time.time() - start_time))

