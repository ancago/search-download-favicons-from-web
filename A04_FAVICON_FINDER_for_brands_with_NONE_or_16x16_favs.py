from bs4 import BeautifulSoup
import pandas as pd
import requests as req
from A00_File_name import file_name

output_file_2 = file_name[:-4] + '_NONE_or_16x16_favicons_ONLY.csv'
file_df = pd.read_csv(output_file_2, encoding='latin-1', sep=';', index_col=[0])
print(file_df.head())

'''
create links for Favicon Finder
'''

column_name = 'Official Web Page'
WWW_list = file_df[column_name].tolist()

'''
remove 'http..' prefix
'''

clean_www = []
for www in WWW_list:
    if 'https://' in www:
        clean_www.append(www[8:])
    elif 'http://' in www:
        clean_www.append(www[7:])
    elif 'www' in www:
        clean_www.append(www)
    else:
        clean_www.append('???????????????????')

print(clean_www)

'''
create request URL for Favicon Finder
'''

favs_www = []
for www in clean_www:
    if www[-3:] == '.pl':
        favs_www.append('http://icons.better-idea.org/icons?url=https%3A%2F%2F' + str(www) + '#result ' \
                        + 'http://icons.better-idea.org/icons?url=https%3A%2F%2F' + str(www)[:-3] + '.com#result')
    else:
        favs_www.append('http://icons.better-idea.org/icons?url=https%3A%2F%2F' + str(www) + '#result')

file_df['icons_web'] = favs_www


'''
get URLs of favicons from Favicon Finder
'''

column_name = 'icons_web'
WWW_list = file_df[column_name].tolist()

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

index = 0
for icon_web_list in WWW_list:

    string_16x16 = '[16] '
    string_32x32 = '[32] '
    string_48x48 = '[48] '
    string_57x57 = '[57] '
    string_60x60 = '[60] '
    string_64x64 = '[64] '
    string_72x72 = '[72] '
    string_76x76 = '[76] '
    string_96x96 = '[96] '
    string_114x114 = '[114] '
    string_120x120 = '[120] '
    string_144x144 = '[144] '
    string_152x152 = '[152] '
    string_180x180 = '[180] '
    string_192x192 = '[192] '
    string_other = '[] '

    for www in icon_web_list.split():

        page = req.get(www)
        soup = BeautifulSoup(page.text, 'html.parser')
        soup.prettify()

        for tag in soup.find_all("img"):

            if tag.get('width') == '8':
                string_16x16 = string_16x16 + (tag.get('src')) + ' '
            elif tag.get('width') == '16':
                string_32x32 = string_32x32 + (tag.get('src')) + ' '
            elif tag.get('width') == '24':
                string_48x48 = string_48x48 + (tag.get('src')) + ' '
            elif tag.get('width') == '28':
                string_57x57 = string_57x57 + (tag.get('src')) + ' '
            elif tag.get('width') == '30':
                string_60x60 = string_60x60 + (tag.get('src')) + ' '
            elif tag.get('width') == '32':
                string_64x64 = string_64x64 + (tag.get('src')) + ' '
            elif tag.get('width') == '36':
                string_72x72 = string_72x72 + (tag.get('src')) + ' '
            elif tag.get('width') == '38':
                string_76x76 = string_76x76 + (tag.get('src')) + ' '
            elif tag.get('width') == '48':
                string_96x96 = string_96x96 + (tag.get('src')) + ' '
            elif tag.get('width') == '57':
                string_114x114 = string_114x114 + (tag.get('src')) + ' '
            elif tag.get('width') == '60':
                if '80..120..200' in tag.get('src'):
                    pass
                else:
                    string_120x120 = string_120x120 + (tag.get('src')) + ' '
            elif tag.get('width') == '72':
                string_144x144 = string_144x144 + (tag.get('src')) + ' '
            elif tag.get('width') == '76':
                string_152x152 = string_152x152 + (tag.get('src')) + ' '
            elif tag.get('width') == '90':
                string_180x180 = string_180x180 + (tag.get('src')) + ' '
            elif tag.get('width') == '96':
                string_192x192 = string_192x192 + (tag.get('src')) + ' '
            elif tag.get('src') == './icon.svg':
                pass
            elif '/icon?url=https%3a%2f%2f' in tag.get('src'):
                pass
            else:
                string_other = string_other + (tag.get('src')) + ' '

    size_16x16.append(string_16x16)
    size_32x32.append(string_32x32)
    size_48x48.append(string_48x48)
    size_57x57.append(string_57x57)
    size_60x60.append(string_60x60)
    size_64x64.append(string_64x64)
    size_72x72.append(string_72x72)
    size_76x76.append(string_76x76)
    size_96x96.append(string_96x96)
    size_114x114.append(string_114x114)
    size_120x120.append(string_120x120)
    size_144x144.append(string_144x144)
    size_152x152.append(string_152x152)
    size_180x180.append(string_180x180)
    size_192x192.append(string_192x192)
    size_other.append(string_other)

    index += 1

    print(index, len(size_16x16))
    print(index, len(size_32x32))
    print(index, len(size_48x48))
    print(index, len(size_64x64))
    print(index, len(size_other))


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


file_df.to_csv(output_file_2, sep=';')

