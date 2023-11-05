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
    products = soup.find_all('div',attrs={'data-component-type':'s-search-result'})
    product_obj=[]
    for product in products :
        name = product.find("span",attrs={'class':'a-size-base-plus a-color-base a-text-normal'})
        if name is not None:
            name=name.string
        else:
            name=""
        price = product.find("span",attrs={'class':'a-price-whole'})
        if price is not None:
            price = price.string
            # price_text = price.get_text(strip=True)
            # Remove the rupee symbol (₹) and convert to an integer
            if price is not None:
                price = price.replace(',', '')  # Remove commas
                price = int(price)
            else:
                price=0
        else:
            price = 0
        image = product.find('div',attrs={'class':'a-section aok-relative s-image-square-aspect'})
        if image is not None:
            image = image.find('img').get('src')
        else:
            image = ""
        rating = product.find('div',attrs={'class':'a-row a-size-small'})
        if rating is not None:
            rating = rating.find('span')
            rating = rating.get('aria-label')
            pattern = r'(\d+\.\d+)'
            # Extract the numeric value from each string
            rating = re.search(pattern, rating).group(1)
        product_link = product.find("a",attrs={'class':'a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal'}).get('href')
        product_link = 'https://amazon.in/'+ product_link


        product_obj.append({'name':name,'price':price,'image':image,'rating':rating,'product_link':product_link,'website':'Amazon'})

    return product_obj



def generate_flipkart_search(search_string):
    base_url = "https://www.flipkart.com/search?q="
    
    search_string = re.sub(r'\s+', ' ', search_string)
    search_string = search_string.replace(" ", "%20")
    
    url = base_url + search_string
    webpage = requests.get(url,headers=HEADERS)
    while webpage.status_code != 200:
         webpage = requests.get(url,headers=HEADERS)
    soup = BeautifulSoup(webpage.content,"html.parser")
    products = soup.find_all('div',attrs={'class':'_4ddWXP'})

    product_obj=[]
    for product in products :
        name = product.find("a",attrs={'class':'s1Q9rs'}).string
        price = product.find("div",attrs={'class':'_30jeq3'})
        if price is not None:
            price_text = price.get_text(strip=True)
            # Remove the rupee symbol (₹) and convert to an integer
            price_text = price_text.replace('₹', '').replace(',', '')  # Remove commas
            price = int(price_text)
        else:
            price = 0
        link = "www.flipkart.com"+product.find("a",attrs={'class':'s1Q9rs'}).get('href')

        image = product.find('div', attrs={'class': 'CXW8mj'})
        if image is not None:
            image = image.find('img').get('src')
        else:
            image = ""

        
        rating = product.find('div',attrs={'class':'_3LWZlK'})

        if rating is not None:
            rating = rating.get_text(strip=True)
        else:
            rating = "4"
        product_obj.append({'name':name,'product_link':link,'price':price,'image':image,'rating':rating,'product_link':link,'website':'Flipkart'})

    return product_obj


def sorter(product_list):
    max_price = max(float(product['price']) for product in product_list)
    max_rating = max(float(product['rating']) for product in product_list)

    sorted_list = sorted(product_list, key=lambda x: (0.7 * (float(x['price']) / max_price) + 0.3 * (float(x['rating']) / max_rating)), reverse=True)
    
    return sorted_list

