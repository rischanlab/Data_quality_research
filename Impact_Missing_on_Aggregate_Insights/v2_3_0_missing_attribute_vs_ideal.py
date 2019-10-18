# -*- coding: utf-8 -*-
import csv
import aggregate_insight as ag
import glob




if __name__ == "__main__":

    k_list = [5, 10, 15, 20]

    for k in k_list:
        file_ideal_topk = 'raw_results/diabetes_v2.xlsx'
        topk = ag.get_topk_aggregate(k, file_ideal_topk)
        print("Ideal topk", topk)
        for i in range(10):
            file_name = 'raw_results/db_missing_zipf_attr' + str(i+1) + '.xlsx'
            #file_name = 'raw_results/db_' + str(percent) + 'nodrop_attr' + str(i + 1) + '.xlsx'
            for file_view in glob.glob(file_name):
                print(file_name, k)
                missing = ag.get_topk_aggregate(k, file_view)
                #print("Missing topk: ", missing)
                #print("RBO Standard to Ideal = {}".format(ag.rboresult(missing, topk)))
                #print("Jaccard Standard to Ideal = {}".format(ag.jaccard_similarity(missing, topk)))
                with open('results/missing_zipf_attributes_vs_ideal.csv', 'a', newline='') as f:
                #with open('results/nodrop_attributes_vs_ideal.csv', 'a', newline='') as f:
                    fields = [k, ag.rboresult(missing, topk), ag.jaccard_similarity(missing, topk)]
                    writer = csv.writer(f)
                    writer.writerow(fields)

    for k in k_list:
        file_ideal_topk = 'raw_results/diabetes_v2.xlsx'
        topk = ag.get_topk_aggregate(k, file_ideal_topk)
        for i in range(10):
            #file_name = 'raw_results/db_' +str(percent) + 'dropnan_attr' + str(i+1) + '.xlsx'
            file_name = 'raw_results/db_missing_zipf_op_attr' + str(i + 1) + '.xlsx'
            for file_view in glob.glob(file_name):
                print(file_name, k)
                missing = ag.get_topk_aggregate(k, file_view)
                #print("Missing topk: ", missing)
                #print("RBO Standard to Ideal = {}".format(ag.rboresult(missing, topk)))
                #print("Jaccard Standard to Ideal = {}".format(ag.jaccard_similarity(missing, topk)))
                #with open('results/dropnan_attributes_vs_ideal.csv', 'a', newline='') as f:
                with open('results/missing_zipf_op_attributes_vs_ideal.csv', 'a', newline='') as f:
                    fields = [k, ag.rboresult(missing, topk), ag.jaccard_similarity(missing, topk)]
                    writer = csv.writer(f)
                    writer.writerow(fields)