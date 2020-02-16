import pandas as pd
import requests
import sys
import os
from A00_File_name import file_name, file_directory, images_folder_name


folder_16x16 = '16x16'
folder_32x32and48x48 = '32x32 and 48x48'
folder_higher_sizes = 'higher_sizes'

directory = file_directory + images_folder_name
if not os.path.exists(directory):
    os.makedirs(directory)
    os.makedirs(directory + '/' + folder_16x16)
    os.makedirs(directory + '/' + folder_32x32and48x48)
    os.makedirs(directory + '/' + folder_higher_sizes)


file_df = pd.read_csv(file_name + '_FINAL.csv', encoding='latin-1', sep=';')
print(file_df.head())


brand_name_list = file_df['Official Chain Name'].tolist()
images = []


def cell_http_list(column_name, row_idx):
    if 'http' in file_df[column_name][row_idx]:
        http_list = str(file_df[column_name][row_idx][5:]).split()
        # print(http_list[0])
        return http_list
    else:
        return 'EMPTY'


def download_icon(images_file, _size_, fav_http, idx):
    try:
        img_data = requests.get(fav_http).content
        if '.png' in str(fav_http):
            img_name = str(images_file) + str(brand_name_list[index]) + '_' + str(_size_) + '_' + str(idx) + '.png'
        elif '.ico' in str(fav_http):
            img_name = str(images_file) + str(brand_name_list[index]) + '_' + str(_size_) + '_' + str(idx) + '.ico'
        else:
            img_name = str(images_file) + str(brand_name_list[index]) + '_' + str(_size_) + '_' + str(idx) + '.png'
            print(fav_http)
        with open(img_name, 'wb') as handler:
            handler.write(img_data)
            print(str(idx), 'downloaded')
            return 'downloaded '
            # images.append('downloaded')
    except:
        print(str(index) + ' ' + str(sys.exc_info()[0]))


brands_with_no_favicons = []
brands_with_errors = []

for index in range(len(file_df['Official Web Page'])):
    no_favicons = 0
    downloaded = []
    print(index)

    cell_https = cell_http_list('16 x 16', index)
    if cell_https == 'EMPTY':
        if file_df.loc[index, '16 x 16'] == '[]':
            no_favicons += 1
    else:
        for http in cell_https:
            print('http: ' + http)
            if 'http' in http:
                downloaded.append(download_icon(images_folder_name + '/16x16/', '16 x 16', http, cell_https.index(http)))

    for col_name in list(file_df.columns[file_df.columns.get_loc("32 x 32"): file_df.columns.get_loc("57 x 57")]):
        cell_https = cell_http_list(col_name, index)

        if cell_https == 'EMPTY':
            no_favicons += 1
        else:
            for http in cell_https:
                if 'http' in http:
                    downloaded.append(download_icon(images_folder_name + '/32x32 and 48x48/', col_name, http, cell_https.index(http)))

    for col_name in list(file_df.columns[file_df.columns.get_loc("57 x 57"): file_df.columns.get_loc("other sizes")]):
        cell_https = cell_http_list(col_name, index)

        if cell_https == 'EMPTY':
            no_favicons += 1
        else:
            for http in cell_https:
                if 'http' in http:
                    downloaded.append(download_icon(images_folder_name + '/higher_sizes/', col_name, http, cell_https.index(http)))

    cell_https = cell_http_list('other sizes', index)
    if cell_https == 'EMPTY':
        if file_df.loc[index, 'other sizes'] == '[]':
            no_favicons += 1
        elif '<class' in file_df.loc[index, 'other sizes']:
            brands_with_errors.append(index)
    else:
        for http in cell_https:
            if 'http' in http:
                downloaded.append(download_icon(images_folder_name + '/other_sizes/', 'other sizes', http, cell_https.index(http)))

    if no_favicons == 15:
        brands_with_no_favicons.append(index)

    images.append([str(index)] + downloaded)
    print(images)

print('NO favicons: ' + str(brands_with_no_favicons))
print('Errors : ' + str(brands_with_errors))


# file_df['Images'] = images
#
# file_df.to_csv(file_name, sep=';')
