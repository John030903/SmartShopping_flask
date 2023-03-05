import requests
import json
from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options
from numpy import random
from bs4 import BeautifulSoup
from .fill_items import tiki_filter, lazada_filter, shopee_filter
import pandas as pd

TIKI_API = "https://tiki.vn/api/v2/products?limit=48&include=advertisement&aggregations=2&trackity_id=a818abb0-b29b-a7e7-c95b-bfa1603a6b24&q={}&sort=top_seller"
LAZADA_API = "https://www.lazada.vn/catalog/?_keyori=ss&ajax=true&from=input&isFirstRequest=true&page=1&q={}&spm=a2o4n.store_product.search.go.3f1b1380SEs25s"
# LAZADA_SEARCH = "https://www.lazada.vn/tag/hoa--gia/?q={}&_keyori=ss&from=input&spm=a2o4n.store_product.search.go.32271380DlWemj&catalog_redirect_tag=true"
SHOPEE_SEARCH = "https://shopee.vn/search?keyword={}&page=0&sortBy=sales"

def use_api(url):
    """
    It takes a URL as an argument, makes a request to that URL, and returns the response as a JSON
    object
    
    :param url: The URL of the API you want to use
    :return: A dictionary
    """
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.70',}
    response = requests.get(url, headers=headers)
    data = json.loads(response.content)
    return data

def use_browser(search_key):
    """
    It opens a headless Chrome browser, navigates to the Shopee search page, waits for the page to load,
    then returns the scripts on the page
    
    :param search_key: the keyword you want to search for
    :return: A list of all the scripts in the page.
    """
    chrome_options = Options()  
    chrome_options.add_argument("--headless")  
    driver = webdriver.Chrome(options=chrome_options)
    driver.set_page_load_timeout(30)
    driver.get(SHOPEE_SEARCH.format(search_key))
    sleep(random.randint(5,10))
    soup = BeautifulSoup(driver.page_source)
    scripts = soup.find_all("script", type="application/ld+json")
    # with open("File.html", "w", encoding="utf-8") as f:
    #     f.write(driver.page_source)
    return scripts

def load_data(search_key):
    tiki_items = use_api(TIKI_API.format(search_key))["data"]
    items = tiki_filter(tiki_items)
    try:
        lazada_items = use_api(LAZADA_API.format(search_key))["mods"]["listItems"]
        items = pd.concat([items,lazada_filter(lazada_items)], ignore_index=True)
    except:
        pass
    try:
        shopee_items = use_browser(search_key)
        items = pd.concat([items,shopee_filter(shopee_items)], ignore_index=True)
    except:
        pass
    return items
