import requests
from bs4 import BeautifulSoup

import get_page


# setting the url
board = input("Choose board: ")
page = input("Choose page: ")

if page == "1":
    URL = "https://boards.4chan.org/"+board+"/"
else:
    URL = "https://boards.4chan.org/"+board+"/"+page
print("Url has been set to: "+URL)

#getting html file
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")


get_page.get_page(soup)
