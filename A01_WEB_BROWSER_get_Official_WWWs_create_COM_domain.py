import pandas as pd
import time
from google import google
import sys
from A00_File_name import file_name


file_df = pd.read_csv(file_name, sep=';', encoding='latin-1')
print(file_df.head())

brand_names_list = file_df['Official Chain Name'].tolist()


'''
create a column with Official Brand WWWs
'''
#  https://github.com/abenassi/Google-Search-API

WWW = []
for index in range(len(brand_names_list)):
    search_results = google.search(str(brand_names_list[index]) +
                                   ' ' + str(file_df.iloc[index]['Category']) + " official website")
    time.sleep(3)
    result_nb = 0
    try:
        for i in range(len(search_results)):

            if "wiki" in str(search_results[i].link) or 'facebook' in str(search_results[i].link).lower() \
                    or'stackoverflow' in str(search_results[i].link).lower():
                print(str(index), 'wiki or facebook or stackoverflow')
                pass
            else:
                print(search_results[i].link)
                WWW.append("/".join(search_results[i].link.split("/", 3)[:3]))
                print(index, i)
                result_nb += 1
                break
        if result_nb == 0:
            WWW.append('[]')

    except OSError:
        WWW.append('Permission denial ' + str(sys.exc_info()[0]))
    except:
        WWW.append(sys.exc_info()[0])

print(len(brand_names_list))
print(len(WWW))


'''
create a column with .com domain
'''


def create_www_brand_COM(brand_name):
    newstr = brand_name.replace("'", "")
    newstr = newstr.replace(" ", "")
    newstr = newstr.replace(".", "")
    newstr = newstr.replace("&", "")
    newstr = newstr.replace("-", "")

    newstr = newstr + '.com'
    newstr = newstr.lower()
    print(newstr)
    return newstr


brands_wwws = []
for name in file_df['Official Chain Name']:
    brands_wwws.append(create_www_brand_COM(name))
    print(brands_wwws)


file_df['Official Web Page'] = WWW
file_df['.com Web Page'] = brands_wwws
print(file_df.head())

file_df.to_csv(file_name[:-4] + '_URLs_from_WB.csv', sep=';')
