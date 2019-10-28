# -*- coding: utf-8 -*-
import csv
import aggregate_insight as ag
import glob




if __name__ == "__main__":

    k_list = [5, 10, 15, 20]

    # for k in k_list:
    #     file_ideal_topk = 'raw_results/diabetes.xlsx'
    #     topk = ag.get_topk_aggregate(k, file_ideal_topk)
    #     print("Ideal topk", topk)
    #     percentage_list = [0,5,10,15]
    #     for percent in percentage_list:
    #         for i in range(10):
    #             file_name = 'raw_results/db_' +str(percent) + 'dropnan_measure' + str(i+1) + '.xlsx'
    #             #file_name = 'raw_results/db_' + str(percent) + 'nodrop_measure' + str(i + 1) + '.xlsx'
    #             for file_view in glob.glob(file_name):
    #                 #print(percent, file_name, k)
    #                 missing = ag.get_topk_aggregate(k, file_view)
    #                 print("Missing topk: ", missing)
    #                 print("RBO Standard to Ideal = {}".format(ag.rboresult(missing, topk)))
    #                 print("Jaccard Standard to Ideal = {}".format(ag.jaccard_similarity(missing, topk)))
    #                 with open('results/dropnan_measures_vs_ideal.csv', 'a', newline='') as f:
    #                 #with open('results/nodrop_measures_vs_ideal.csv', 'a', newline='') as f:
    #                     fields = [percent, k, ag.rboresult(missing, topk), ag.jaccard_similarity(missing, topk)]
    #                     writer = csv.writer(f)
    #                     writer.writerow(fields)
    #
    for k in k_list:
        file_ideal_topk = 'raw_results_100/diabetes.xlsx'
        topk = ag.get_topk_aggregate(k, file_ideal_topk)
        print("Ideal topk", topk)
        percentage_list = [0,5,10,15]
        for percent in percentage_list:
            for i in range(100):
                #file_name = 'raw_results/db_' +str(percent) + 'dropnan_measure' + str(i+1) + '.xlsx'
                file_name = 'raw_results_100/db_' + str(percent) + 'nodrop_measure' + str(i + 1) + '.xlsx'
                for file_view in glob.glob(file_name):
                    #print(percent, file_name, k)
                    missing = ag.get_topk_aggregate(k, file_view)
                    print("Missing topk: ", missing)
                    print("RBO Standard to Ideal = {}".format(ag.rboresult(missing, topk)))
                    print("Jaccard Standard to Ideal = {}".format(ag.jaccard_similarity(missing, topk)))
                    #with open('results/dropnan_measures_vs_ideal.csv', 'a', newline='') as f:
                    with open('results/100_nodrop_measures_vs_ideal.csv', 'a', newline='') as f:
                        fields = [percent, k, ag.rboresult(missing, topk), ag.jaccard_similarity(missing, topk)]
                        writer = csv.writer(f)
                        writer.writerow(fields)

    # for k in k_list:
    #     file_ideal_topk = 'insulin_steady_vs_no_steady/diabetes.xlsx'
    #     topk = ag.get_topk_aggregate(k, file_ideal_topk)
    #     print("Ideal topk", topk)
    #     percentage_list = [0,5,10,15]
    #     for percent in percentage_list:
    #         for i in range(10):
    #             #file_name = 'raw_results/db_' +str(percent) + 'dropnan_measure' + str(i+1) + '.xlsx'
    #             file_name = 'insulin_steady_vs_no_steady/db_' + str(percent) + 'nodrop_measure' + str(i + 1) + '.xlsx'
    #             for file_view in glob.glob(file_name):
    #                 #print(percent, file_name, k)
    #                 missing = ag.get_topk_aggregate(k, file_view)
    #                 print("Missing topk: ", missing)
    #                 print("RBO Standard to Ideal = {}".format(ag.rboresult(missing, topk)))
    #                 print("Jaccard Standard to Ideal = {}".format(ag.jaccard_similarity(missing, topk)))
    #                 #with open('results/dropnan_measures_vs_ideal.csv', 'a', newline='') as f:
    #                 with open('results/insulin_nodrop_measures_vs_ideal.csv', 'a', newline='') as f:
    #                     fields = [percent, k, ag.rboresult(missing, topk), ag.jaccard_similarity(missing, topk)]
    #                     writer = csv.writer(f)
    #                     writer.writerow(fields)