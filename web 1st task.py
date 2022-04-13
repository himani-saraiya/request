from msilib.schema import Class
from urllib.request import Request
from bs4 import BeautifulSoup
# import json
# import os
import requests
url="https://www.rottentomatoes.com/top/bestofrt/top_100_animation_movies/"
page=requests.get(url)
# print(page)
soup=BeautifulSoup(page.txt,"html.parser")
def scrap_list():
    main_div=soup.find('div',Class_='lister')
    return main_div
print(scrap_list())