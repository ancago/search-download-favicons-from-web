# search-download-favicons-from-web

Favicon is an icon to display on the tab in browser. Most web pages have icon references in the source code of their homepage. 
<br>**search-download-favicons-from-web** allows to find official website of a given company, download the available favicons and see the statistics per brand category (Cafe, Hotel/Motel, Market, Shop, Petrol Station).

# Overview: 
Enter and save the four parameters in **“A00_File_name.py”** script. Running the subsequent scripts in a given sequence results in:
1.	Creating a **“FileName_FINAL.csv”** file with URLs of all downloaded favicons.
2.	Creating a new folder (e.g. **'TRIAL_Statistics'**) where .png images of pie charts with statistics per category are saved.
3.	Creating a new folder (e.g. **'TRIAL_FavImages'**) where .png images of favicons of brands listed in input .csv file are downloaded.

# Requirements:
1.	Python 3, pandas, google, BeautifulSoup, BytesIO, time, sys, os, PIL, requests, matplotlib.pyplot. 

# Before running the scripts:
1.	Make sure the list of brands is in the file type: CSV (Comma delimited) *.csv
2.	The output file of the chosen script must be closed while running the script. 
3.	All cells of existing columns must have some values (not empty).
4.	Columns required: **“Official Chain Name”**, **“Category”**.
5.	Check Brand Names – if there are e.g. German or Polish phonetic signs, they will be changed into something like: ĂŁÂ©tĂŁÂ©gĂŁÂ©nĂŁÂ©. Change them into English letters.

# Shortcuts:
**WB** – Web Browser – stands for Google search; the browsed phrase is: **“Official Chain Name”** + **“Category”** + **“official website”**
<br>**FF** – Favicon Finder – the online tool for collecting favicons’ URLs (https://i.olsh.me/); requires brand’s website address

# Recommendations:
1.	Problems commented in red could be improved.
2.	URLs from column **“other sizes”** could be checked for favicon sizes and transferred to corresponding columns (e.g. to **“32 x 32”** column); thus, the column **“other sizes”** would only collect errors (column name could be changed into **“Errors”**).

# Run the scripts in a given sequence:

**Script name**	| **Input	/ Output** |	**Notes**
|---|---|---|
| **A00_File_name.py**	| 1. Enter the full *FileName* of .csv file containing the columns **“Official Chain Name”** and **“Category”** (e.g. ‘file_name.csv’) <br> 2. Enter the full *directory* where the above .csv file is located (e.g. '/Pycharm_Projects/Favicons/') <br> 3. Enter the name of *new folder*, where **statistics** images will be saved <br> 4. Enter the name of *new folder*, where **favicons' images** will be downloaded | Input for other scripts |	No need to run the script |
| **A01_WEB_BROWSER_get_Official_WWWs_create_COM_domain.py**	| Automatic |	1. Creates new file named: <br> **“FileName”** + **“_URLs_from_WB.csv”** <br> where the following columns will be added: <br> 1. **index** <br> 2. **“Official Web Page”** <br> –the list of official websites collected via Google search (WB) <br> 3. **“.com Web Page”** <br> – the list of automatically created .com domains (**“Official Chain Name”** + **“.com”**)	| 1. Check the file. Some websites in column **“Official Web Page”** will be missing (instead you’ll find “[]”). Find websites by yourself, usually only 2-3% of all brands miss the website. <br> 2. Check if there are no **“wikipedia”** or **“facebook”** websites in **“Official Web Page”** column. Change into correct ones. |
| **A02_get_favicons_URLs_from_both_WWWs.py**	| Automatic |	1. Creates columns with URLs of favicons of different sizes, in the previously created file: <br> **“FileName”** + **“_URLs_from_WB.csv”** |	Searches for favicons URLs based on websites from column **“Official Web Page”** and **“.com Web Page”**. <br><br> Error types are visible in column **“other sizes”.** |
| **A03_create_file_with_brands_with_NONE_or_16x16_favs.py** |	Automatic |	1. Creates new file named: <br> **“FileName”** + **“_NONE_or_16x16_favicons_ONLY.csv”** Extracts list of brands with no URLs of favicons or with favicons of size 16x16 only. <br> 2. Creates new column named **“Issue”** - Contains **“No favicons”** or **“16x16 ONLY”** comments. |	Use this script for any file. Follow the instructions in the script, written under the line: **“#######################”** on top and bottom of the script.|
| **A04_FAVICON_FINDER_for_brands_with_NONE_or_16x16_favs.py** |	Automatic	| 1. The same file (**“FileName”** + **“_NONE_or_16x16_favicons_ONLY.csv”**) <br> Contains columns with URLs of favicons of different sizes. <br> Uses Favicon Finder online tool.|
| **A05_compile_2_files__create_FINAL_file.py** |	Automatic	| 1. Creates new file named: <br> **“FileName”** + **“_FINAL.csv”** | Contains columns with URLs of favicons combined from Web Browser and Favicon Finder outputs. | Use this script to combine any two files. Follow the instructions in the script, written under the line: **“#######################”** on top and bottom of the script.
| **A06a_statistics_methods.py**	| Automatic |	Input for the next script	| No need to run the script. Contains methods. |
| **A06b_statistics_per_CATEGORY.py** |	Automatic |	1. Creates a new folder (e.g. **'TRIAL_Statistics'**) where .png images of pie charts are saved. Uses **“FileName”** + **“_FINAL.csv”** file for statistics. **Pie charts** with statistics per category, show % of: <br>  •	Brands with no favicons <br> •	Brands with only 16x16 favicons <br>  •	Brands with favicons of higher sizes <br> •	Errors|
| **A07_download_favicons.py** |	Automatic |	1. Creates a new folder (e.g. **'TRIAL_FavImages'**) with three folders inside: <br> •	16x16 <br> •	32x32 and 48x48 <br> •	higher_sizes <br> where .png images of favicons of corresponding sizes are being downloaded.	Uses **“FileName”** + **“_FINAL.csv”** file to get favicons URLs and download images. |
| **A08_DELETE_intermediate_files.py** | 	Automatic |	Deletes intermediate files: <br> •	**“FileName”** + **“_URLs_from_WB.csv”** <br> •	**“FileName”** + **“_NONE_or_16x16_favicons_ONLY.csv”** <br> Run if you want to get rid of intermediate files. |


# Other available scripts (but need to be adjusted):
1.	**Run_Full_Script.py** – automatically runs all scripts in sequence; requires parameters from the script “A00_File_name.py”.
2.	**A09_check_downloaded_brands_favs.py** – creates a column in “_FINAL.csv” file where all the names of each brand’s downloaded favicons are listed.
3.	**A10_RESIZE_image.py** – downsizes images from a given directory to a given size (e.g. from 114x114 to 32x32 size). Saves images in a given folder.
4.	**SIZE_checker.py** – checks the size of a favicon using its URL from a given column of .csv file.


