# -*- coding: utf-8 -*-
import csv
import aggregate_insight as ag
import glob




if __name__ == "__main__":

    k_list = [5, 10, 15, 20]
    m_list = [0, 1, 2, 3]
    percentage_list = [10, 20, 30, 40, 50, 60, 70, 80, 90]

    for default_k in k_list:
        file_ideal_topk = 'raw_results/ideal_topk.csv'
        ideal_topk = ag.get_topk(default_k, file_ideal_topk)
        print("Ideal topk", ideal_topk)
        for m in m_list:
            km = default_k + (m*default_k)
            print(default_k, m, km)
            for percent in percentage_list:
                for i in range(10):
                    file_name = 'raw_results/dynamic_db_' + str(percent) + 'missing' + str(i+1) + '_' + str(default_k) + '_' + str(m) +'.csv'
                    #print(file_name)
                    for missing_file in glob.glob(file_name):
                        #print(missing_file)
                        dynamic = ag.get_topk(default_k, missing_file)
                        print("RBO Dynamic to Ideal = {}".format(ag.rboresult(dynamic, ideal_topk)))
                        print("Jaccard Dynamic to Ideal = {}".format(ag.jaccard_similarity(dynamic, ideal_topk)))
                        with open('results/dynamic_vs_ideal_' + str(default_k) + '_' + str(m) + '.csv', 'a',
                                  newline='') as f:
                            fields = [percent, default_k, m, ag.rboresult(dynamic, ideal_topk),
                                      ag.jaccard_similarity(dynamic, ideal_topk)]
                            writer = csv.writer(f)
                            writer.writerow(fields)