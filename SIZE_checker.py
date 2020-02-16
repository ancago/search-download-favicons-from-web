from io import BytesIO
from PIL import Image
import requests
import pandas as pd
import sys


file = pd.read_csv('Favicons_Web.csv', encoding='latin-1', sep=';')
file_df = pd.DataFrame(file)
file_df.drop(file_df.columns[0], axis=1, inplace=True)
print(file_df.head())
column_name = 'size unknown'
WWW_list = file_df[column_name].tolist()


RANGE = 50000
sizes_list = []
index = 0
for cell in WWW_list:
    print(index)
    if cell == '[]':
        sizes_list.append('[]')
        index += 1
    else:
        try:
            cell = cell[1:-1]
            cell = cell.split(",")
            cell = str(cell).split("'")
            index += 1
            for www in range(len(cell)):
                if 'http' in cell[www]:
                    # print('yessss')
                    req = requests.get(cell[www], headers={'User-Agent': 'Mozilla5.0(Google spider)', 'Range': 'bytes=0-{}'.format(RANGE)})
                    im = Image.open(BytesIO(req.content))

                    # if im.size == (64, 64) or im.size == (48, 48) or im.size == (32, 32):
                    #     print('yessss')
                    # else:
                    #     print('no')
                    print(im.size)
        except:
            print(sys.exc_info()[0])

