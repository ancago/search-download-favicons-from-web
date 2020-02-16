from bs4 import BeautifulSoup
import pandas as pd
import sys
from io import BytesIO
from PIL import Image
import requests as req
from A00_File_name import file_name

output_file_1 = file_name[:-4] + '_URLs_from_WB.csv'
file_df = pd.read_csv(output_file_1, encoding='latin-1', sep=';', index_col=[0])
print(file_df.head())


def create_img_link(href):
    if 'http' in href:
        icon_link = href
        return icon_link
    elif 'http' not in href:
        if prefix_found == 1:
            icon_link = str(prefix) + href
            return icon_link
        else:
            icon_link = str(www) + href
            return icon_link
    else:
        icon_link = '!!! PROBLEM !!!'
        print('LINK error')
        return icon_link


def insert_string_with_size(size):
    size_found = 0
    for i in range(len(strings_list)):
        if strings_list[i][1:3] == size:
            strings_list[i] += create_img_link(tag['href']) + ' '
            size_found += 1
            return strings_list
        else:
            pass
    if size_found == 0:
        strings_list[15] += create_img_link(tag['href']) + ' '
        return strings_list
    else:
        pass


size_16x16 = []
size_32x32 = []
size_48x48 = []
size_57x57 = []
size_60x60 = []
size_64x64 = []
size_72x72 = []
size_76x76 = []
size_96x96 = []
size_114x114 = []
size_120x120 = []
size_144x144 = []
size_152x152 = []
size_180x180 = []
size_192x192 = []
size_other = []

prefix_found = 0
RANGE = 50000

column_name = ['Official Web Page', '.com Web Page']

for index in range(len(file_df['Official Web Page'])):

    strings_list = []

    both_WWWs = [file_df.loc[index, 'Official Web Page'], file_df.loc[index, '.com Web Page']]
    errors = ''

    for www in both_WWWs:

        if strings_list == []:

            strings_list.append('[16] ')
            strings_list.append('[32] ')
            strings_list.append('[48] ')
            strings_list.append('[57] ')
            strings_list.append('[60] ')
            strings_list.append('[64] ')
            strings_list.append('[72] ')
            strings_list.append('[76] ')
            strings_list.append('[96] ')
            strings_list.append('[114] ')
            strings_list.append('[120] ')
            strings_list.append('[144] ')
            strings_list.append('[152] ')
            strings_list.append('[180] ')
            strings_list.append('[192] ')
            strings_list.append('[] ')
        else:
            pass
        print('index: ' + str(index))

        if www == both_WWWs[1] and both_WWWs[1] in both_WWWs[0]:
            pass
        else:
            if www == both_WWWs[0]:
                web = www
            else:
                web = 'http://www.' + str(www)

            try:
                print(web)
                page = req.get(web, timeout=20)
                soup = BeautifulSoup(page.text, 'html.parser')
                soup.prettify()
                prefix = www

                for tag in soup.find_all("link", rel="canonical"):
                    prefix = "/".join(tag['href'].split("/", 3)[:3])
                    prefix_found = 1

                for tag in soup.find_all("link"):
                    if 'icon' in tag['rel'] or 'Icon' in tag['rel'] or 'icon' in tag['rel'][0] or 'Icon' in tag['rel'][0]:

                        link = create_img_link(tag['href'])
                        img_link = req.get(link, headers={'User-Agent': 'Mozilla5.0(Google spider)',
                                                    'Range': 'bytes=0-{}'.format(RANGE)})
                        im = Image.open(BytesIO(img_link.content))
                        print(im.size)

                        strings_list = insert_string_with_size(str(im.size[0])[0:2])

                prefix_found = 0

            except:
                errors += str(sys.exc_info()[0]) + ' '
                print('!!! Some other Error !!!', sys.exc_info()[0])
                continue

    strings_list[15] += errors

    print('length before: ' + str(len(size_16x16)))
    size_16x16.append(strings_list[0])
    print('length after: ' + str(len(size_16x16)))
    # print(size_16x16)
    size_32x32.append(strings_list[1])
    size_48x48.append(strings_list[2])
    size_57x57.append(strings_list[3])
    size_60x60.append(strings_list[4])
    size_64x64.append(strings_list[5])
    size_72x72.append(strings_list[6])
    size_76x76.append(strings_list[7])
    size_96x96.append(strings_list[8])
    size_114x114.append(strings_list[9])
    size_120x120.append(strings_list[10])
    size_144x144.append(strings_list[11])
    size_152x152.append(strings_list[12])
    size_180x180.append(strings_list[13])
    size_192x192.append(strings_list[14])
    size_other.append(strings_list[15])

print(len(size_16x16))
print(len(file_df[column_name]))

file_df['16 x 16'] = size_16x16
file_df['32 x 32'] = size_32x32
file_df['48 x 48'] = size_48x48
file_df['57 x 57'] = size_57x57
file_df['60 x 60'] = size_60x60
file_df['64 x 64'] = size_64x64
file_df['72 x 72'] = size_72x72
file_df['76 x 76'] = size_76x76
file_df['96 x 96'] = size_96x96
file_df['114 x 114'] = size_114x114
file_df['120 x 120'] = size_120x120
file_df['144 x 144'] = size_144x144
file_df['152 x 152'] = size_152x152
file_df['180 x 180'] = size_180x180
file_df['192 x 192'] = size_192x192
file_df['other sizes'] = size_other


file_df.to_csv(output_file_1, sep=';')


