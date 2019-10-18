from seedb import SeeDB
from cost_table import data

if __name__ == "__main__":

    top_k = 10
    list_table = [
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
        import time
        start_time = time.time()
        framework = SeeDB(db,data_set,table,top_k)
        framework.main()
        print("--- %s seconds ---" % (time.time() - start_time))
        print("done")

# This running file for cost comparison between import from diabetes and import from cost table.
# Compare the cost.

