import glob
import shutil

file_name = 'db_0nan_measure1.xlsx'
full_name = 'raw_results/' + file_name

for i in range(9):
    src_dir = full_name
    dst_dir = "raw_results/db_0nan_measure" + str(i + 2) + ".xlsx"
    shutil.copy(src_dir, dst_dir)
