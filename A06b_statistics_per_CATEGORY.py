from A06a_statistics_methods import *
from A00_File_name import file_directory, statistics_folder_name
import matplotlib.pyplot as plt
import os


directory = file_directory + statistics_folder_name
if not os.path.exists(directory):
    os.makedirs(directory)


def statistics_per_brand(category):

    category_none = 0
    category_16x16 = 0
    category_higher = 0
    connection_err = 0
    os_err = 0
    other_err = 0
    count = 0

    for i in range(len(file_df['Category'])):

        if category in file_df.loc[i, 'Category']:

            count += 1
            category_none += brands_with_no_favicons(i)
            category_16x16 += Brands_with_favicons_of_only_size_16x16(i)
            category_higher += Brands_with_favicons_of_sizes_higher_than_16x16(i)
            connection_err += Errors(i)[0]
            os_err += Errors(i)[1]

            other_err += Errors(i)[2] + Errors(i)[3] + Errors(i)[4] \
                         + Errors(i)[5] + Errors(i)[6] + Errors(i)[7]
        else:
            pass
    return category_none, category_16x16, category_higher, connection_err, os_err, other_err, count


print(statistics_per_brand('Restaurant'))
print(statistics_per_brand('Caf'))
print(statistics_per_brand('Hotel'))
print(statistics_per_brand('Petrol Station'))
print(statistics_per_brand('Market'))
print(statistics_per_brand('Bank'))


""" create pie charts with statistics """


restaurants = 'Restaurant'
cafes = 'Caf'
hotels = 'Hotel'
petrol_stations = 'Petrol Station'
supermarkets = 'Market'
shops = 'Shop'


labels = 'Brands with no favicons', 'Brands with only 16x16 favicons', 'Brands with favicons of higher sizes', \
         'Connection_Error', 'OS_Error', 'Other_Errors'

rest_caf = [statistics_per_brand(restaurants)[0] + statistics_per_brand(cafes)[0],
            statistics_per_brand(restaurants)[1] + statistics_per_brand(cafes)[1],
            statistics_per_brand(restaurants)[2] + statistics_per_brand(cafes)[2],
            statistics_per_brand(restaurants)[3] + statistics_per_brand(cafes)[3],
            statistics_per_brand(restaurants)[4] + statistics_per_brand(cafes)[4],
            statistics_per_brand(restaurants)[5] + statistics_per_brand(cafes)[5]]

hot = [statistics_per_brand(hotels)[0], statistics_per_brand(hotels)[1], statistics_per_brand(hotels)[2],
       statistics_per_brand(hotels)[3], statistics_per_brand(hotels)[4], statistics_per_brand(hotels)[5]]

station = [statistics_per_brand(petrol_stations)[0], statistics_per_brand(petrol_stations)[1],
           statistics_per_brand(petrol_stations)[2], statistics_per_brand(petrol_stations)[3],
           statistics_per_brand(petrol_stations)[4], statistics_per_brand(petrol_stations)[5]]

market = [statistics_per_brand(supermarkets)[0], statistics_per_brand(supermarkets)[1],
          statistics_per_brand(supermarkets)[2], statistics_per_brand(supermarkets)[3],
          statistics_per_brand(supermarkets)[4], statistics_per_brand(supermarkets)[5]]

shop = [statistics_per_brand(shops)[0], statistics_per_brand(shops)[1],
        statistics_per_brand(shops)[2], statistics_per_brand(shops)[3],
        statistics_per_brand(shops)[4], statistics_per_brand(shops)[5]]


""" save statistics images in new file"""

print(rest_caf)
plt.pie(rest_caf, labels=labels, autopct='%.0f%%', shadow=True, explode=(0, 0, 0.1, 0, 0, 0))
name = 'Restaurants and Cafes (' + str(statistics_per_brand(restaurants)[6]
                                       + statistics_per_brand(cafes)[6]) + ' brands)'
plt.title(label=name)
plt.savefig(directory + '/' + name + '.png', bbox_inches='tight')
plt.show()

plt.pie(hot, labels=labels, autopct='%.0f%%', shadow=True, explode=(0, 0, 0.1, 0, 0, 0))
name = 'Hotels (' + str(statistics_per_brand(hotels)[6]) + ' brands)'
plt.title(label=name)
plt.savefig(directory + '/' + name + '.png', bbox_inches='tight')
plt.show()

plt.pie(station, labels=labels, autopct='%.0f%%', shadow=True, explode=(0, 0, 0.1, 0, 0, 0))
name = 'Petrol stations (' + str(statistics_per_brand(petrol_stations)[6]) + ' brands)'
plt.title(label=name)
plt.savefig(directory + '/' + name + '.png', bbox_inches='tight')
plt.show()

plt.pie(market, labels=labels, autopct='%.0f%%', shadow=True, explode=(0, 0, 0.1, 0, 0, 0))
name = 'Supermarkets (' + str(statistics_per_brand(supermarkets)[6]) + ' brands)'
plt.title(label=name)
plt.savefig(directory + '/' + name + '.png', bbox_inches='tight')
plt.show()

plt.pie(shop, labels=labels, autopct='%.0f%%', shadow=True, explode=(0, 0, 0.1, 0, 0, 0))
name = 'Shops (' + str(statistics_per_brand(shops)[6]) + ' brands)'
plt.title(label=name)
plt.savefig(directory + '/' + name + '.png', bbox_inches='tight')
plt.show()
