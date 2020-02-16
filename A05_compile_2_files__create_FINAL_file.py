import pandas as pd
from A03_create_file_with_brands_with_NONE_or_16x16_favs import output_file_2, file_name
from A02_get_favicons_URLs_from_both_WWWs import output_file_1

file_df_WB = pd.read_csv(output_file_1, encoding='latin-1', sep=';', index_col=[0])
file_df_FF = pd.read_csv(output_file_2, encoding='latin-1', sep=';', index_col=[0])


# #############################################################################################################
# """ ................................. compile any two files  ................................"""
# comment the above two lines of code #
# below, uncomment the four lines of code
# below, enter file names as first parameters: # file_df_WB = .... and file_df_FF = ...

# file_df_WB = pd.read_csv('Global_TopBrands_Draft_v.0.1_2column.csv', encoding='latin-1', sep=';')
# file_df_WB.drop(file_df_WB.columns[0], axis=1, inplace=True)

# file_df_FF = pd.read_csv('Global_TopBrands_Draft_v.0.1_2column.csv_NONE_16x16_favicons_ONLY.csv', encoding='latin-1', sep=';')
# file_df_FF.drop(file_df_FF.columns[0], axis=1, inplace=True)
# #############################################################################################################


print(file_df_WB.head())
print(file_df_FF.head())

column_names = ['16 x 16',	'32 x 32',	'48 x 48',	'57 x 57',	'60 x 60',	'64 x 64',
                '72 x 72',	'76 x 76',	'96 x 96',	'114 x 114',	'120 x 120',
                '144 x 144',	'152 x 152',	'180 x 180',	'192 x 192', 'other sizes']


def combine_values(idx_WB, idx_FF, column_name):
    combined_value = file_df_WB.loc[idx_WB, column_name]
    for value in file_df_FF.loc[idx_FF, column_name].split():
        if ('http' in value or '<class' in value) and value not in file_df_WB.loc[idx_WB, column_name]:
            combined_value += ' ' + value
            print('yhym')
        else:
            pass
    # print(combined_value)
    return combined_value

"""
compiles two files of different lengths (nb of rows)
fills file_WB with URLs from file_FF
WB - Web Browser
FF - Favicon Finder
"""


for brand_name in file_df_FF['Official Chain Name']:
    print(brand_name)
    if brand_name in file_df_WB['Official Chain Name'].tolist():
        index_WB = int(file_df_WB.index[file_df_WB['Official Chain Name'] == brand_name].values)
        index_FF = int(file_df_FF.index[file_df_FF['Official Chain Name'] == brand_name].values)
        print(index_FF, brand_name)
        print(index_WB, brand_name)
        print(' ')
        for name in column_names:
            file_df_WB.loc[index_WB, name] = combine_values(index_WB, index_FF, name)
    else:
        print(brand_name)


# #############################################################################################################
# """ ................................. compile any two files  ................................"""
# uncomment the below one line of code: # file_name = ...
# below, enter output file name #

# file_name = 'Global_TopBrands_Draft_v.0.1'
# #############################################################################################################


file_name_final = file_name + '_FINAL.csv'

file_df_WB.to_csv(file_name_final, sep=';')

