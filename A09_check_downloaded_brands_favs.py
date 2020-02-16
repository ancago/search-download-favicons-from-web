from PIL import Image
import pandas as pd
import os
import sys

file_name = 'Global_TopBrands_Draft_v.0.1_FINAL.csv'

file = pd.read_csv(file_name, encoding='latin-1', sep=';')
file_df = pd.DataFrame(file)
file_df.drop(file_df.columns[0], axis=1, inplace=True)
print(file_df.head())

folder = os.fsencode('IMAGES/Top_Restaurants/')
favicons_filenames = []

for brand_name in file_df['Official Chain Name']:
    brand_favicons = []

    for image in os.listdir(folder):
        filename = os.fsdecode(image)
        print(filename)
        if brand_name in filename:
            brand_favicons.append(filename)
        else:
            pass

    favicons_filenames.append(brand_favicons)

file_df['Favicons Filenames'] = favicons_filenames

file_df.to_csv(file_name, sep=';')
