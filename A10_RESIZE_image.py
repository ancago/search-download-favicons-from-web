from PIL import Image
import os
import sys
import pandas as pd

file_name = 'top_40_restaurants_COMPILED.csv'

file = pd.read_csv(file_name, encoding='latin-1', sep=';')
file_df = pd.DataFrame(file)
file_df.drop(file_df.columns[0], axis=1, inplace=True)
print(file_df.head())


def resize(image_name, width, height):
    im1 = Image.open(image_name)
    im5 = im1.resize((width, height), Image.ANTIALIAS)
    ext = ".png"
    im5.save(image_name + '_' + str(width) + 'x' +
             str(height) + '_RESIZED_' + ext)
    print('resized')

# folder_higher_sizes = os.fsencode("higher_sizes/")
folder_other_sizes = os.fsencode("IMAGES/Top_Restaurants/RESIZED/")

# images_higher_sizes = []
# images_other_sizes = []
invalid_file = []

# for file in os.listdir(folder_higher_sizes):
#     filename = "higher_sizes/" + str(os.fsdecode(file))
#     # images_higher_sizes.append(filename)
#     try:
#         resize(filename, 32, 32)
#         resize(filename, 48, 48)
#     except:
#         print(str(sys.exc_info()[0]))
#         invalid_file.append(filename)

# images_higher_sizes.sort()

for file in os.listdir(folder_other_sizes):
    filename = "IMAGES/Top_Restaurants/RESIZED/" + str(os.fsdecode(file))
#     images_other_sizes.append(filename)
    print(filename)
    try:
        resize(str(filename), 32, 32)
        resize(str(filename), 48, 48)
    except:
        print(str(sys.exc_info()[0]))
        invalid_file.append(filename)


# images_other_sizes.sort()






























# open an image file (.bmp,.jpg,.png,.gif) you have in the working folder
# imageFile = "Original_192x192.png"
# im1 = Image.open(imageFile)

# adjust width and height to your needs
# width = 32
# height = 32

# use one of these filter options to resize the image
# im2 = im1.resize((width, height), Image.NEAREST)      # use nearest neighbour (bad for down-sizing)
# im3 = im1.resize((width, height), Image.BILINEAR)     # linear interpolation in a 2x2 environment
# im4 = im1.resize((width, height), Image.BICUBIC)      # cubic spline interpolation in a 4x4 environment
# im5 = im1.resize((width, height), Image.ANTIALIAS)    # best down-sizing filter

# ext = ".png"
# im2.save(imageFile + '_' + str(width) + 'x' + str(height) + "NEAREST" + ext)
# im3.save(imageFile + '_' + str(width) + 'x' + str(height) + "BILINEAR" + ext)
# im4.save(imageFile + '_' + str(width) + 'x' + str(height) + "BICUBIC" + ext)
# im5.save(imageFile + '_' + str(width) + 'x' + str(height) + "ANTIALIAS" + ext)



# optional image viewer ...
# image viewer  i_view32.exe   free download from:  http://www.irfanview.com/
# avoids the many huge bitmap files generated by PIL's show()
# import os
# os.system("IMAGES\Caltex_YYYYYYYYYYy.png")