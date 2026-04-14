import requests

headers = {
    'sec-ch-ua-platform': '"Windows"',
    'Referer': 'https://www.ajio.com/b/andamen',
    'sec-ch-ua': '"Chromium";v="146", "Not-A.Brand";v="24", "Google Chrome";v="146"',
    'sec-ch-ua-mobile': '?0',
    'ai': 'www.ajio.com',
    'clientIP': '45.114.65.131, 10.156.239.4, 182.156.239.12, 104.91.59.54, 23.64.59.239, 23.208.140.229',
    'vr': 'WEB-1.15.0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36',
    'Accept': 'application/json',
    'os': '4',
    'ua': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36',
}

params = {
    'fields': 'SITE',
    'currentPage': '12',
    'pageSize': '45',
    'format': 'json',
    'query': ':relevance',
    'gridColumns': '3',
    'advfilter': 'true',
    'platform': 'Desktop',
    'showAdsOnNextPage': 'false',
    'is_ads_enable_plp': 'true',
    'displayRatings': 'true',
    'store': 'ajio',
    'segmentIds': '',
    'enableRushDelivery': 'true',
    'vertexEnabled': 'false',
    'visitorId': '671363337.1776075612',
    'userEncryptedId': '695b93783355c5227c148a8285458b67e4b52cf427edbbbb1c8c15ef02a370b5',
    'previousSource': 'Saas',
    'plaAdsProvider': 'OSMOS',
    'plaAdsEliminationDisabled': 'false',
    'plpBannerAdsEnabled': 'false',
    'state': '',
    'city': '',
    'zone': '',
    'userRestriction': '',
    'userState': 'NON_LOGGED_IN',
}

response = requests.get('https://www.ajio.com/api/category/andamen', params=params, headers=headers)


def parser_product_links(category_links):
    for category in category_links:
        print(f"Processing category: {category['category_name']}")
        response = requests.get(category['product_api_url'], params=params, headers=headers)
        if response.status_code == 200:
            data = response.json()
            product_links = [product['product_url'] for product in data.get('products', [])]
            print(f"Extracted {len(product_links)} product links for category: {category['category_name']}")
            insert_product_links(category['sub_id'], product_links)
        else:
            print(f"Failed to fetch products for category: {category['category_name']}. Status code: {response.status_code}")