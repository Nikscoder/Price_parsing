import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.x-kom.pl/szukaj?f32-dysk=141074-512-gb-ssd-pcie-wlutowany&f37-karta-graficzna=184622-apple-m1-7-rdzeni&f58-pamiec-ram=185607-16-gb-pamiec-zunifikowana&q=macbook%20air%20m1"

def get_date(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    return soup
def parse(soup):
    # Find the parent div with class 'sc-3g60u5-0 dNgqYV'
    parent_div = soup.find('div', {'class': 'sc-3g60u5-0 dNgqYV'})
    if parent_div:
        # Find the h3 element within the parent div
        title_element = parent_div.find('h3', {'class': 'sc-16zrtke-0 kGLNun sc-1yu46qn-9 feSnpB'})
        if title_element:
            title = title_element.get('title')
            print("Product Title:", title)
    return



soup = get_date(url)
parse(soup)
