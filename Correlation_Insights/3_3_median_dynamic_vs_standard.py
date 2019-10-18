# -*- coding: utf-8 -*-
import csv
import aggregate_insight as ag
import glob




if __name__ == "__main__":

    k_list = [5, 10, 15, 20]
    m_list = [0, 1, 2, 3]
    percentage_list = [10, 20, 30, 40, 50, 60, 70, 80, 90]

    for default_k in k_list:
        for m in m_list:
            km = default_k + (m*default_k)
            print(default_k, m, km)
            for percent in percentage_list:
                for i in range(10):
                    file_name = 'raw_results/dynamic_db_' + str(percent) + 'missing' + str(i+1) + '_' + str(default_k) + '_' + str(m) + '.csv'
                    for missing_file in glob.glob(file_name):
                        #print(len(missing_file))
                        if len(missing_file) == 42:
                            standard = 'raw_results/standard_db_' + str(percent) + 'median' + str(i+1) +'.csv'
                            #print(standard)
                        else:
                            standard = 'raw_results/standard_db_' + str(percent) + 'median' + str(i+1) +'.csv'
                            #print(standard)
                        standard = ag.get_topk(default_k, standard)
                        dynamic = ag.get_topk(default_k, missing_file)
                        print("RBO Dynamic to Standard = {}".format(ag.rboresult(dynamic, standard)))
                        print("Jaccard Dynamic to Standard = {}".format(ag.jaccard_similarity(dynamic, standard)))
                        with open('results/dynamic_vs_standard_' + str(default_k) + '_' + str(m) +'.csv', 'a', newline='') as f:
                            fields = [percent, default_k, m, ag.rboresult(dynamic, standard), ag.jaccard_similarity(dynamic, standard)]
                            writer = csv.writer(f)
                            writer.writerow(fields)
