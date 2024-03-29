# -*- coding: utf-8 -*-
import csv
import aggregate_insight as ag
import glob




if __name__ == "__main__":

    k_list = [5, 10, 15, 20]

    for k in k_list:
        file_ideal_topk = 'raw_results/ideal_topk.csv'
        topk = ag.get_topk(k, file_ideal_topk)
        print("Ideal topk", topk)
        percentage_list = [10, 20, 30, 40, 50, 60, 70, 80, 90]
        for percent in percentage_list:
            for i in range(10):
                file_name = 'raw_results/missing_db_' +str(percent) + 'missing' + str(i+1) + '.csv'
                for impute_file in glob.glob(file_name):
                    #print(percent, file_name, k)
                    missing = ag.get_topk(k, impute_file)
                    print("Missing topk: ", missing)
                    print("RBO Standard to Ideal = {}".format(ag.rboresult(missing, topk)))
                    print("Jaccard Standard to Ideal = {}".format(ag.jaccard_similarity(missing, topk)))
                    with open('results/missing_vs_ideal.csv', 'a', newline='') as f:
                        fields = [percent, k, ag.rboresult(missing, topk), ag.jaccard_similarity(missing, topk)]
                        writer = csv.writer(f)
                        writer.writerow(fields)
