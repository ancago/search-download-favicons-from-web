import os
from A00_File_name import file_directory

file_1 = "A00_TRIAL_FAVICONS_NONE_or_16x16_favicons_ONLY.csv"
file_2 = "A00_TRIAL_FAVICONS_URLs_from_WB.csv"

directory_1 = file_directory + '/' + file_1
if os.path.exists(directory_1):
    os.remove(file_1)

directory_2 = file_directory + '/' + file_2
if os.path.exists(directory_2):
    os.remove(file_2)
