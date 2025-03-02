# import os
# import urllib.request as request
#
# data_url = "https://github.com/entbappy/Branching-tutorial/raw/master/articles.zip"
#
# def download_file():
#
#     filename, headers = request.urlretrieve(
#         url = data_url,
#         filename = "articles.zip"
#     )
#
#
# download_file()
# os.system("unzip articles.zip")
# os.system("rm -rf articles.zip")


import os
import urllib.request as request
import zipfile

data_url = "https://github.com/entbappy/Branching-tutorial/raw/master/articles.zip"

def download_and_extract():
    # Step 1: Download the ZIP file
    zip_path = "articles.zip"
    request.urlretrieve(url=data_url, filename=zip_path)

    # Step 2: Extract the ZIP file
    with zipfile.ZipFile(zip_path, "r") as zip_ref:
        zip_ref.extractall("articles")  # Extract contents to 'articles' folder

    # Step 3: Delete the ZIP file after extraction
    os.remove(zip_path)

# Run the function
download_and_extract()
