import csv
import aggregate_insight as ag
import glob

if __name__ == "__main__":

    k_list = [5, 10, 15, 20]

    for k in k_list:
        percentage_list = [0,5,10,15]
        for percent in percentage_list:
            for i in range(10):
                file_name = 'insulin_steady_vs_no_steady/db_' +str(percent) + 'nodrop_attr' + str(i+1) + '.xlsx'
                #file_name = 'raw_results/db_' + str(percent) + 'nodrop_attr' + str(i + 1) + '.xlsx'
                for file_view in glob.glob(file_name):
                    print(percent, file_name, k)                    #print("Missing topk: ", missing)
                    #print("RBO Standard to Ideal = {}".format(ag.rboresult(missing, topk)))
                    #print("Jaccard Standard to Ideal = {}".format(ag.jaccard_similarity(missing, topk)))
                    with open('results/variance_insulin_steady_vs_no_steady_nodrop_attr.csv', 'a', newline='') as f:
                    #with open('results/nodrop_attributes_vs_ideal.csv', 'a', newline='') as f:
                        fields = [percent, k, ag.get_topk_variance(k, file_name)]
                        writer = csv.writer(f)
                        writer.writerow(fields)
        for percent in percentage_list:
            for i in range(10):
                file_name = 'insulin_steady_vs_no_steady/db_' +str(percent) + 'nodrop_measure' + str(i+1) + '.xlsx'
                #file_name = 'raw_results/db_' + str(percent) + 'nodrop_attr' + str(i + 1) + '.xlsx'
                for file_view in glob.glob(file_name):
                    print(percent, file_name, k)                    #print("Missing topk: ", missing)
                    #print("RBO Standard to Ideal = {}".format(ag.rboresult(missing, topk)))
                    #print("Jaccard Standard to Ideal = {}".format(ag.jaccard_similarity(missing, topk)))
                    with open('results/variance_insulin_steady_vs_no_steady_nodrop_measure.csv', 'a', newline='') as f:
                    #with open('results/nodrop_attributes_vs_ideal.csv', 'a', newline='') as f:
                        fields = [percent, k, ag.get_topk_variance(k, file_name)]
                        writer = csv.writer(f)
                        writer.writerow(fields)

        for percent in percentage_list:
            for i in range(10):
                file_name = 'insulin_steady_vs_no_steady/db_' +str(percent) + 'nodrop_a_m' + str(i+1) + '.xlsx'
                #file_name = 'raw_results/db_' + str(percent) + 'nodrop_attr' + str(i + 1) + '.xlsx'
                for file_view in glob.glob(file_name):
                    print(percent, file_name, k)                    #print("Missing topk: ", missing)
                    #print("RBO Standard to Ideal = {}".format(ag.rboresult(missing, topk)))
                    #print("Jaccard Standard to Ideal = {}".format(ag.jaccard_similarity(missing, topk)))
                    with open('results/variance_insulin_steady_vs_no_steady_nodrop_a_m.csv', 'a', newline='') as f:
                    #with open('results/nodrop_attributes_vs_ideal.csv', 'a', newline='') as f:
                        fields = [percent, k, ag.get_topk_variance(k, file_name)]
                        writer = csv.writer(f)
                        writer.writerow(fields)


    # for k in k_list:
    #     percentage_list = [0,5,10,15]
    #     for percent in percentage_list:
    #         for i in range(10):
    #             file_name = 'readmitted_no_vs_yes/db_' +str(percent) + 'nodrop_attr' + str(i+1) + '.xlsx'
    #             #file_name = 'raw_results/db_' + str(percent) + 'nodrop_attr' + str(i + 1) + '.xlsx'
    #             for file_view in glob.glob(file_name):
    #                 print(percent, file_name, k)                    #print("Missing topk: ", missing)
    #                 #print("RBO Standard to Ideal = {}".format(ag.rboresult(missing, topk)))
    #                 #print("Jaccard Standard to Ideal = {}".format(ag.jaccard_similarity(missing, topk)))
    #                 with open('results/variance_readmitted_no_vs_yes_nodrop_attr.csv', 'a', newline='') as f:
    #                 #with open('results/nodrop_attributes_vs_ideal.csv', 'a', newline='') as f:
    #                     fields = [percent, k, ag.get_topk_variance(k, file_name)]
    #                     writer = csv.writer(f)
    #                     writer.writerow(fields)
    #     for percent in percentage_list:
    #         for i in range(10):
    #             file_name = 'readmitted_no_vs_yes/db_' +str(percent) + 'nodrop_measure' + str(i+1) + '.xlsx'
    #             #file_name = 'raw_results/db_' + str(percent) + 'nodrop_attr' + str(i + 1) + '.xlsx'
    #             for file_view in glob.glob(file_name):
    #                 print(percent, file_name, k)                    #print("Missing topk: ", missing)
    #                 #print("RBO Standard to Ideal = {}".format(ag.rboresult(missing, topk)))
    #                 #print("Jaccard Standard to Ideal = {}".format(ag.jaccard_similarity(missing, topk)))
    #                 with open('results/variance_readmitted_no_vs_yes_nodrop_measure.csv', 'a', newline='') as f:
    #                 #with open('results/nodrop_attributes_vs_ideal.csv', 'a', newline='') as f:
    #                     fields = [percent, k, ag.get_topk_variance(k, file_name)]
    #                     writer = csv.writer(f)
    #                     writer.writerow(fields)
    #
    #     for percent in percentage_list:
    #         for i in range(10):
    #             file_name = 'readmitted_no_vs_yes/db_' +str(percent) + 'nodrop_a_m' + str(i+1) + '.xlsx'
    #             #file_name = 'raw_results/db_' + str(percent) + 'nodrop_attr' + str(i + 1) + '.xlsx'
    #             for file_view in glob.glob(file_name):
    #                 print(percent, file_name, k)                    #print("Missing topk: ", missing)
    #                 #print("RBO Standard to Ideal = {}".format(ag.rboresult(missing, topk)))
    #                 #print("Jaccard Standard to Ideal = {}".format(ag.jaccard_similarity(missing, topk)))
    #                 with open('results/variance_readmitted_no_vs_yes_nodrop_a_m.csv', 'a', newline='') as f:
    #                 #with open('results/nodrop_attributes_vs_ideal.csv', 'a', newline='') as f:
    #                     fields = [percent, k, ag.get_topk_variance(k, file_name)]
    #                     writer = csv.writer(f)
    #                     writer.writerow(fields)