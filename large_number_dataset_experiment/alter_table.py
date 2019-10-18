import psycopg2 as pg

mlist = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]

print("Alter table missing name ")
for i in mlist:
    for j in range(10):
        #print(int(i * 100), j)
        x = int(i * 100)
        table_name = str(x) + "mdiab" + str(j+1)
        #print(table_name)
        old_name = "`"+ table_name + "`"
        new_name = "db_" + table_name
        print(new_name)
        # connection = pg.connect("dbname=data_cleaning user=postgres password=zenvisage")
        conn = pg.connect(database='data_cleaning', user='postgres', password='zenvisage')
        query = "alter table " + old_name + " rename to " + new_name
        cur = conn.cursor()
        cur.execute(query)
        conn.commit()
        conn.close()

print("Alter table name for table after impute")
for i in mlist:
    for j in range(10):
        #print(int(i * 100), j)
        x = int(i * 100)
        table_name = str(x) + "diab" + str(j+1)
        #print(table_name)
        old_name = "`"+ table_name + "`"
        new_name = "db_" + table_name
        print(new_name)
        # connection = pg.connect("dbname=data_cleaning user=postgres password=zenvisage")
        conn = pg.connect(database='data_cleaning', user='postgres', password='zenvisage')
        query = "alter table " + old_name + " rename to " + new_name
        cur = conn.cursor()
        cur.execute(query)
        conn.commit()
        conn.close()


# old_name = "diabetes"
# new_name = "diab"
# #connection = pg.connect("dbname=data_cleaning user=postgres password=zenvisage")
# conn = pg.connect(database='data_cleaning',user='postgres',password='zenvisage')
# query = "alter table " + old_name + " rename to " + new_name
# cur = conn.cursor()
# cur.execute(query)
# conn.commit()
# conn.close()