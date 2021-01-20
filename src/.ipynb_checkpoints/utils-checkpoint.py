from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import re

def get_links(url):
    req = Request(url)
    html_page = urlopen(req)

    soup = BeautifulSoup(html_page, "lxml")

    links = []
    for link in soup.findAll('a'):
        try:          
            classes = link.get("class")
            if 'btn-primary' in classes:
                if ".cxg" in link.get("href"):
                    links.append(link.get("href"))
                else:
                    links.append("https://www.covid19cellatlas.org" + link.get("href"))
        except:
            continue