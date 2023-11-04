import re
from bs4 import BeautifulSoup
import pandas as pd
import requests

HEADERS=({'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36","Accept-Language":'en-US, en;q=0.5'})

def generate_amazon_search(search_string):
    base_url = "https://www.amazon.in/s?k="
    
    search_string = re.sub(r'\s+', ' ', search_string)
    search_string = search_string.replace(" ", "+")
    
    url = base_url + search_string
    webpage = requests.get(url,headers=HEADERS)
    while webpage.status_code != 200:
         webpage = requests.get(url,headers=HEADERS)
    soup = BeautifulSoup(webpage.content,"html.parser")
    return soup

def generate_flipkart_search(search_string):
    base_url = "https://www.flipkart.com/search?q="
    
    search_string = re.sub(r'\s+', ' ', search_string)
    search_string = search_string.replace(" ", "%20")
    
    url = base_url + search_string
    webpage = requests.get(url,headers=HEADERS)
    while webpage.status_code != 200:
         webpage = requests.get(url,headers=HEADERS)
    soup = BeautifulSoup(webpage.content,"html.parser")
    return soup

