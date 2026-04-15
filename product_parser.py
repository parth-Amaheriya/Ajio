
from curl_cffi import requests
import json
import time
import random




params = {
    'fields': 'SITE',
    'pageSize': "60",
    'format': 'json',
    'platform': 'Desktop',
    'displayRatings': 'true',
    'store': 'ajio',
    'visitorId': '671363337.1776075612',
    'userEncryptedId': '695b93783355c5227c148a8285458b67e4b52cf427edbbbb1c8c15ef02a370b5',
    'previousSource': 'Saas',
    'userState': 'NON_LOGGED_IN',
}

visitor_data = [
    {
        'visitorId': '671363337.1776075612',
        'userEncryptedId': '695b93783355c5227c148a8285458b67e4b52cf427edbbbb1c8c15ef02a370b5'
    },
    {
        'visitorId': '1888385107.1776242932',
        'userEncryptedId': '388e47a4f72da5467948606652c2fbe0eb02b45e53eb967e891b707b27527c4e',
    }
]

headers={
        'sec-ch-ua-platform': '"Windows"',
        'accept-language': 'en-US,en;q=0.9',
        'sec-ch-ua': '"Google Chrome";v="138", "Not.A/Brand";v="8", "Chromium";v="138"',
        'ai': 'www.ajio.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36',
        'Accept': 'application/json',
        'os': '4',
        'ua': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36',
    }


def get_session():
    session = requests.Session(impersonate="chrome")  
    session.get('https://www.ajio.com/', headers=headers, timeout=20)
    return session,headers

def parser_product_links(api_url):
    print(f"Processing API URL: {api_url}")
    page_count=1
    total_products_count=None
    product_links=[]
    session,headers = get_session()
    try:
        while True:
            params_temp={**params, 'currentPage':page_count}
            # time.sleep(random.uniform(2,4))
            response = session.get(api_url, impersonate="chrome", params=params_temp, headers=headers,timeout=20)
            print(page_count,response)

            if response.status_code != 200:
                print(f"Failed to fetch products for API URL: {api_url}. Status code: {response.status_code}")
                break

            data = response.json()
            product_links.extend(parse_product_link(data))
            if page_count==1:
                total_products_count = extract_page_info(data)

            if page_count%99==0:
                print("Refreshing session to avoid potential blocking wait 60 seconds...")
                time.sleep(100)
                session,headers = get_session()

            page_count+=1
    except Exception as e:
        print(f"Error fetching products for API URL: {api_url}. Error: {e}") 
        return product_links, total_products_count   

    return product_links, total_products_count
def extract_page_info(data_json):
    try:
        page_data=data_json.get('pagination', {})
        total_product_count=page_data.get('totalResults', 'N/A')
        return total_product_count
    except Exception as e:
        print(f"Error extracting page info: {e}")
        return None

# products
def parse_product_link(data_json):
    links=[]
    try:
        products=data_json.get('products', [])

        for pro in products:
            product_url=pro.get('url')
            links.append(product_url)
        return links
    
    except Exception as e:
        print(f"Error decoding JSON: {e}")
        return links        
        