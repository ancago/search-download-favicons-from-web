import pandas as pd
from A00_File_name import file_name

output_file_1 = file_name[:-4] + '_URLs_from_WB.csv'
file_df = pd.read_csv(output_file_1, sep=';', encoding='latin-1', index_col=[0])

# #############################################################################################################
# """ .........run to check any file for brands missing favicons or having only 16x16 size ................."""
# comment (Ctrl + /) the above line of code (file_df = ...)#
# below, enter file name as first parameter #
# uncomment the below line of code and the last line of code in this script #

# file_df = pd.read_csv('Global_TopBrands_Draft_v.0.1_FINAL.csv', sep=';', encoding='latin-1')

# #############################################################################################################

print(file_df.head())


def brands_with_no_favicons(index):

    if 'http' not in file_df['16 x 16'][index] and 'http' not in file_df['32 x 32'][index] \
        and 'http' not in file_df['48 x 48'][index] and 'http' not in file_df['57 x 57'][index] \
        and 'http' not in file_df['60 x 60'][index] and 'http' not in file_df['64 x 64'][index] \
        and 'http' not in file_df['72 x 72'][index] and 'http' not in file_df['76 x 76'][index] \
        and 'http' not in file_df['96 x 96'][index] and 'http' not in file_df['114 x 114'][index] \
        and 'http' not in file_df['120 x 120'][index] and 'http' not in file_df['144 x 144'][index] \
        and 'http' not in file_df['152 x 152'][index] and 'http' not in file_df['180 x 180'][index] \
        and 'http' not in file_df['192 x 192'][index] and 'http' not in file_df['other sizes'][index]:

        return file_df['Official Chain Name'][index]
    else:
        return 0


def Brands_with_favicons_of_only_size_16x16(index):

    if 'http' in file_df['16 x 16'][index] and 'http' not in file_df['32 x 32'][index] \
        and 'http' not in file_df['48 x 48'][index] and 'http' not in file_df['57 x 57'][index] \
        and 'http' not in file_df['60 x 60'][index] and 'http' not in file_df['64 x 64'][index] \
        and 'http' not in file_df['72 x 72'][index] and 'http' not in file_df['76 x 76'][index] \
        and 'http' not in file_df['96 x 96'][index] and 'http' not in file_df['114 x 114'][index] \
        and 'http' not in file_df['120 x 120'][index] and 'http' not in file_df['144 x 144'][index] \
        and 'http' not in file_df['152 x 152'][index] and 'http' not in file_df['180 x 180'][index] \
        and 'http' not in file_df['192 x 192'][index] and 'http' not in file_df['other sizes'][index]:

        return file_df['Official Chain Name'][index]
    else:
        return 0


indexes = []
new_index = 0
Official_Chain_Name = []
Category = []
specialty = []
GDF_feature_code = []
Subcategory = []
Official_Web_Page = []
Issue = []

for index_ in range(len(file_df['Official Web Page'])):
    if brands_with_no_favicons(index_) == 0 and Brands_with_favicons_of_only_size_16x16(index_) == 0:
        pass
    else:
        indexes.append(new_index)
        new_index += 1
        Official_Chain_Name.append(file_df.loc[index_].values[0])
        Category.append(file_df.loc[index_].values[1])
        specialty.append(file_df.loc[index_].values[2])
        GDF_feature_code.append(file_df.loc[index_].values[3])
        Subcategory.append(file_df.loc[index_].values[4])
        Official_Web_Page.append(file_df.loc[index_].values[5])

        if brands_with_no_favicons(index_) != 0:
            Issue.append("NO favicons")
        elif Brands_with_favicons_of_only_size_16x16(index_) != 0:
            Issue.append("16x16 ONLY")

# print(file_df.columns.values.tolist()[:6])

new_file_df = pd.DataFrame()

new_file_df['Official Chain Name'] = Official_Chain_Name
new_file_df['Category'] = Category
new_file_df['specialty'] = specialty
new_file_df['GDF_feature_code'] = GDF_feature_code
new_file_df['Subcategory'] = Subcategory
new_file_df['Official Web Page'] = Official_Web_Page
new_file_df['Issue'] = Issue


output_file_2 = file_name[:-4] + '_NONE_or_16x16_favicons_ONLY.csv'
new_file_df.to_csv(output_file_2, sep=';')


# #############################################################################################################
# """ ......... run to check any file for brands missing favicons or having only 16x16 size ................"""
# comment the above two lines of code #
# below, enter output file name as first parameter #

# new_file_df.to_csv('Global_TopBrands_Draft_v.0.1_FINAL_NONE_or_16x16_favicons_ONLY.csv', sep=';')

# #############################################################################################################

