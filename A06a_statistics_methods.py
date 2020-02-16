import pandas as pd
from A00_File_name import file_name

file_df = pd.read_csv(file_name + '_FINAL.csv', encoding='latin-1', sep=';', index_col=[0])
print(file_df.head())


def brands_with_no_favicons(index):
    none = 0
    other = 0
    if 'http' not in file_df['16 x 16'][index] and 'http' not in file_df['32 x 32'][index] \
        and 'http' not in file_df['48 x 48'][index] and 'http' not in file_df['57 x 57'][index] \
        and 'http' not in file_df['60 x 60'][index] and 'http' not in file_df['64 x 64'][index] \
        and 'http' not in file_df['72 x 72'][index] and 'http' not in file_df['76 x 76'][index] \
        and 'http' not in file_df['96 x 96'][index] and 'http' not in file_df['114 x 114'][index] \
        and 'http' not in file_df['120 x 120'][index] and 'http' not in file_df['144 x 144'][index] \
        and 'http' not in file_df['152 x 152'][index] and 'http' not in file_df['180 x 180'][index] \
        and 'http' not in file_df['192 x 192'][index] and 'http' not in file_df['other sizes'][index] \
        and '<' not in file_df['other sizes'][index]:
        none += 1
    else:
        other += 1
    return none


def Errors(index):

    Connection_Error = 0
    OS_Error = 0
    Value_Error = 0
    Key_Error = 0
    SSL_Error = 0
    Missing_Schema_Error = 0
    Unicode_Error = 0
    Too_Many_Redirects_Error = 0
    empty = 0
    http = 0

    if 'http' not in file_df['16 x 16'][index] and 'http' not in file_df['32 x 32'][index] \
        and 'http' not in file_df['48 x 48'][index] and 'http' not in file_df['57 x 57'][index] \
        and 'http' not in file_df['60 x 60'][index] and 'http' not in file_df['64 x 64'][index] \
        and 'http' not in file_df['72 x 72'][index] and 'http' not in file_df['76 x 76'][index] \
        and 'http' not in file_df['96 x 96'][index] and 'http' not in file_df['114 x 114'][index] \
        and 'http' not in file_df['120 x 120'][index] and 'http' not in file_df['144 x 144'][index] \
        and 'http' not in file_df['152 x 152'][index] and 'http' not in file_df['180 x 180'][index] \
        and 'http' not in file_df['192 x 192'][index] and 'http' not in file_df['other sizes'][index]:
        if "<class 'requests.exceptions.ConnectionError'>" in file_df['other sizes'][index]:
            Connection_Error += 1
        elif "<class 'OSError'>" in file_df['other sizes'][index]:
            OS_Error += 1
        elif "<class 'ValueError'>" in file_df['other sizes'][index]:
            Value_Error += 1
        elif "<class 'KeyError'>" in file_df['other sizes'][index]:
            Key_Error += 1
        elif "<class 'requests.exceptions.SSLError'>" in file_df['other sizes'][index]:
            SSL_Error += 1
        elif "<class 'requests.exceptions.MissingSchema'>" in file_df['other sizes'][index]:
            Missing_Schema_Error += 1
        elif "<class 'UnicodeError'>" in file_df['other sizes'][index]:
            Unicode_Error += 1
        elif "<class 'requests.exceptions.TooManyRedirects'>"in file_df['other sizes'][index]:
            Too_Many_Redirects_Error += 1
        else:
            empty += 1
    else:
        http += 1

    return Connection_Error, OS_Error, Value_Error, Key_Error, SSL_Error, Missing_Schema_Error, Unicode_Error, Too_Many_Redirects_Error


def Brands_with_favicons_of_only_size_16x16(index):

    only_16 = 0
    other = 0
    if 'http' in file_df['16 x 16'][index] and 'http' not in file_df['32 x 32'][index] \
        and 'http' not in file_df['48 x 48'][index] and 'http' not in file_df['57 x 57'][index] \
        and 'http' not in file_df['60 x 60'][index] and 'http' not in file_df['64 x 64'][index] \
        and 'http' not in file_df['72 x 72'][index] and 'http' not in file_df['76 x 76'][index] \
        and 'http' not in file_df['96 x 96'][index] and 'http' not in file_df['114 x 114'][index] \
        and 'http' not in file_df['120 x 120'][index] and 'http' not in file_df['144 x 144'][index] \
        and 'http' not in file_df['152 x 152'][index] and 'http' not in file_df['180 x 180'][index] \
        and 'http' not in file_df['192 x 192'][index] and 'http' not in file_df['other sizes'][index]:
        only_16 += 1
    else:
        other += 1
    return only_16


def Brands_with_favicons_of_sizes_higher_than_16x16(index):

    higher_than_16 = 0
    other = 0

    if 'http' in file_df['32 x 32'][index] \
        or 'http' in file_df['48 x 48'][index] or 'http' in file_df['57 x 57'][index] \
        or 'http' in file_df['60 x 60'][index] or 'http' in file_df['64 x 64'][index] \
        or 'http' in file_df['72 x 72'][index] or 'http' in file_df['76 x 76'][index] \
        or 'http' in file_df['96 x 96'][index] or 'http' in file_df['114 x 114'][index] \
        or 'http' in file_df['120 x 120'][index] or 'http' in file_df['144 x 144'][index] \
        or 'http' in file_df['152 x 152'][index] or 'http' in file_df['180 x 180'][index] \
        or 'http' in file_df['192 x 192'][index] or 'http' in file_df['other sizes'][index]:

        higher_than_16 += 1
    else:
        other += 1

    return higher_than_16



