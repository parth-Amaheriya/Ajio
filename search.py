from curl_cffi import requests
import json
from lxml import html
from main import *
from pathlib import Path
from typing import Any

BASE_URL = "https://www.ajio.com"
OUTPUT_FILE = Path("cleaned_listing_products.json")



session = requests.Session(impersonate="chrome")  

cookies = {
    '_gcl_au': '1.1.1242066138.1776075611',
    'AB': 'B',
    '_gid': 'GA1.2.839209906.1776075612',
    '_fbp': 'fb.1.1776075615037.855111222913757446',
    'ajs_anonymous_id': '380be5ff-4ea2-4f58-b167-731f93838fa5',
    '_pin_unauth': 'dWlkPU5qaGpNVE5sTlRVdFlXSTJOQzAwTmprM0xXRTJNR010WkRjMk9ESTRZVGRpT0RZeA',
    '_fpuuid': 'SFQ0F_Cis7JjD1dbjnZwN',
    'deviceId': 'SFQ0F_Cis7JjD1dbjnZwN',
    'ifa': 'cc0a5cec-0156-4257-b29e-586a76400634',
    'os': '4',
    'vr': 'WEB-2.0.11',
    '_scid': 'SmNvXLZ_a-p9eDLdt-cDkS14K9FJCOOA',
    'V': '201',
    '_sctr': '1%7C1776018600000',
    'dtm_token': 'AQAKPidI4MB8tgE2FmbAAQBFtwABAQCcPd_cLwEBAJyLHop8',
    'dtm_consent': 'UNSPECIFIED',
    'cdigiMrkt': 'utm_source%3A%7Cutm_medium%3A%7Cdevice%3Ad%7Cexpires%3AWed%2C%2013%20May%202026%2011%3A23%3A34%20GMT%7C',
    'bm_sz': '6163796FDA9F670D1D3299CB51D755C7~YAAQDO+cttce8o2dAQAA5rFDjx9GC1TavKYmKmkhysF7ERKqTGs3vXfr4KDR4y5TJ48E8es24il0QvXkhjdmRaLV8NV3Od8xvXLilJ6O7yraXBmFGUlXhYsGXc34x9blL3FrLx/cii7rDSH9bhcYjrGVNEHMrehrtNvxe3wvX+lej726Ehc6EWuVLJbkaBazyhhPd4srbtb3b8eQPWJ5pPOXBaS2VqR3+lmzJcQMVy282R/SyvGpsfiOiLA06VSxgfWLYPIdRPSOKfegdL63irkxMhoo6fKIuZV/qrJAbigFq+Ab2t/G1PXpJ3L62y6cUxCrCjfOFrKAdQa6fc0ohCSDE4tG/1DJSL4/hmWZg4MQBSnsOsU=~4339760~3293761',
    'analytics_session_id': '1776225078182',
    'segment_user_id': 'null',
    'segment_device_id': '380be5ff-4ea2-4f58-b167-731f93838fa5',
    'recentlyViewed': '[{"id":"443396843_grey","store":0},{"id":"443395524_iceblue","store":0},{"id":"443397686_beigemulti","store":0}]',
    'bm_ss': 'ab8e18ef4e',
    'TS01d405db': '015d0fa226100ce187e4b98ed9c04c49f8c32894f43c04d93bf9fe5921ba9240c92dd4f8e2ea757a428c62e8dc07b79fd2c2b9f6c6',
    'ak_bmsc': '006D76C88A9B87A2F25C0665F8D4BB32~000000000000000000000000000000~YAAQjl86F3r6nYWdAQAAr8zWjx9M/OZ2O3K+/lvzUpRdgh+CBUwE/G8NM5u1qoe/P0PTHj0UzhTqIjWc/TtwPjzsl4Pl926yDCJV1m2xcmb5NMkui/3b3vU4lwxMjjvLXQq4FEgD9BN58N2cK2Q1Sxvw0pMyCnqxZR5f2y/jNAXq8hUmSdkz66tfB8SU0e6KNI9U2MHlZ2zLH44S5nD9aEbbsAMvqfmO1KpLxi9XPkJUiXUhl32gAEkV8WhnyYtk2zSImgEZ+hisofwakc1h7B8ltGCL7RqvGKPr/Opbu3/ug5XA2r240s/TBU5jL+uyoYal20ixHVPKxxGw0OhiZkyVRZg9gaR+bruicYpdQ0QyraZT4rNZsqHjMlcLdXdF4UhKzLBaJSH3Ug==',
    '_dc_gtm_UA-68002030-1': '1',
    'ImpressionCookie': '0',
    'bm_so': 'DB5DFFD3AD81ACBBB294C01CE185479481701A02533892C7440737C30A3562C4~YAAQjl86F95CnoWdAQAA+8fYjwd4w+0guIqAgYXCTRhbMw7voQuPrc60NAXyxGLEU41Zf+iqzZDyfal1jt2aNO6POsxrBPNzWP2QCwsbygirKiOz+g7MoIrK9LWiamza8QiNaZUvLnt85FJZLuEnbE4wXP6AxgonIsnmxKCdUfSifdCC19mML66cLytMg1GVBVgtJ38kytzE2yMNoGMkXU3N1sLB9FZaATcuyP9gOa+SLNc2r8rOKpu3e1eTT0n14Wx8KBryLWXiO6NdHGkRLypONYZ6SUR96Heq7XEllnTU1jEHe+yzspoeoa2PkXRuGeMFuUHXrfth1IJjoQoGU/kK0SKbLPUsqXT0VpF+ySjUhi9oyBZMeSUk6sQTuWkmbT7lG4yBywW/4mBhMIdvmqe1qdZFX0a7ItwjYU+HdgV9DnC89QwjVwwxBJTYh7j5Xaz99InSsx5PfVMaYFngRg==',
    '_abck': '6A06F762CCF36DE6D16BDFF9F87CC38F~0~YAAQjl86Fw9DnoWdAQAAbMnYjw9g7n/TEMM8iddxtLil5DD6rG8trJ96ASdq0sUhGJEDaFhbl9tTT5QOd2SsIApVVqkAA4YzqJOBXTNtXloZwSfBqdIkS0kD6J0zoq+kptTsiBPpbu3SmcRH3ErZcttduUTJNLYNlwKEVmvQsxIGJjOr2qzuV6Xh3DdMoN3FbtTsfgzknEv/WQribGxXjuUClXHGjJN/asFkyf9VITL3hxUUTteMyuhLbL7zwG/Wv7rqp/i7DWiua0tVKxoQMz5Qab5sU1BsjL08Q4slR31T7qNRjBXLyTJhU0wHnKxriNmgDBDl/FflHPlopKqlo8IIse/9DvkgwMGKZOhIZiXV8frNlStlI23w6OZtT2Uoi3qCoPYA5RfEoUNLPSyhMW9lyw1zr2Go5zSPCXsCBHdZ3FeJY3i1y1XbRNydN0yoFVkqi1ZDduy/eOTnSMQzC02CGlWjo5vdDkRVBMEBZWOvBD2oUN8ugpYxo9fF9WfeAtoCQa/wRlGTmp1a6Y9cTR/NAwBX4AURVch5Bp+LDfKtSW9SlXPKPdIkVCDuEH7rdp+Z5DZcj/xOriB2OcPvp0lkMA+whaEyRzb9497ofOF/U+8hUxTWw7Ei/xyiedDPS0cfCjaJFXNDJQk+I3VLPFWyhsxkvwlwXiZmGJSg43u78WtqGou/TYPsDYJ7Y6kc+WN2tyeo0Ox5Jodx3v8lBGyReGTtjxl05Egcn8NH8mfK6ECoo8oOD+HftGlsZAWMVKSCzspAtaRpAtEq68Rm2yiafTyPyHk0k32ZLsNpoy4=~-1~-1~1776235875~AAQAAAAF%2f%2f%2f%2f%2f79V6n1mcPivMtUYUXHlYlnJ6Qx5gd+56vFFFSs2gXYbrpZ5rSHHg1pW68HmoyCMGAz4YTIf009LQ4z0cWH6WAKkC5mtFre8%2fTdQe6RO4CffEwM1qfJGqzvNPAcShE4h6WYa6oTormvdj6RKB3CUopz+h3ccEiizUbxEVFh4gw3R5YgC8550QBhc8DMdvvFnoLWX%2fE+RvxNwpS8tDfhDqis%2f4oRlRd1Z73B3BkgWoX4md+I%3d~-1',
    'ajiosessionid': '8612EE1EE1F01BBB27C9BEF0AD81DAF7.a3694',
    'sessionStatus': 'true|undefined',
    'g_state': '{"i_l":0,"i_ll":1776234847674,"i_b":"OwihzjQV3IEaZ5ZDK0YIvOI7fkz2VbDeK9R6w8BR8a0","i_e":{"enable_itp_optimization":22},"i_et":1776138817430}',
    '_ga': 'GA1.2.671363337.1776075612',
    'FirstPage': 'Wed Apr 15 2026 12:04:08 GMT+0530 (India Standard Time)',
    '_derived_epik': 'dj0yJnU9dk9FSlhHSjBKNGIwM3ZjRUdPcnRPYnNnbWtGRC1NNjYmbj1BbERMcHdNbWJrbGV2WVVORkNFX0lnJm09MSZ0PUFBQUFBR25mTVY4JnJtPTEmcnQ9QUFBQUFHbmZNVjgmc3A9NQ',
    'bm_s': 'YAAQjl86F7BFnoWdAQAAc+DYjwWTWTIZD8jzMnZBXJuagWuD0uyQxMcpPsBaPUkWoBLNsCCgscLsRP5EksnWEQbsI9KRd1wgEaBIAaxEmo9y4LPsLgRL2EMQHG+vjZBBIHcSdziyuRxBySBkYGGrjUKz9fngMhuJZleqIGffgGOdxbkPSF5Hd9YVLU+QgFb3utDiacRAw9JeW5DZZze4eytpe0N5vEnUAa2/ap2AYXB1AGbXdZdZjer19nJ6CJErD53RfeAuEblzJE9VqRVwmsizHF6yWo8PttR19phE/wdiuhn4k6sMJdXrYFHScafXLMS2REcQ8DfVBfIddFT2riKeuDxLCvbKlNM4zptcGqxGGyse1SlZmetWUgFbM/R2ZTZXsg2fu8M5gaXV64rfEXDfnv2CadJ8YT3EFWbi80h/PqN4CVux9EF1aYiwvTNsJUXGQkD9Xs8e9R9JPsnT/+iSKCeQBfTqKWfr2RddeWUeGu2FNTGCsOhnQmOLkq+e86OxQqEvjaF0nmi9XJ1v5pCYu1u3PPBSdFxHjblep5UcS9HWcg3vcAqc2En6k3x+rn8sWAMrluKU610qQMv3+j2LeoqpWmE96HXbYytDPA3hVBL4fCgt2W2ivhVLVOnSnCM1Oai9tblXcwf5z6b67qly3rjlrX0EITf2XbdeKJ85EcA/1IQCVgQt6Hulsv9B6R1PoNXRfN0UrA0k4jh3JsmXcCD8JyR5yI6O3DBrhd1rrKub2so4UQFtyRn12GFJLyLY0GvQT2tvUZIV1+wgLI23yIydArKcDQAmhSfql6d4lAjb0AzW2WiB/k9IGtD1am/JsMg/L/x+WsCT/4qhhsofdkZQMeOU9y52hPCnuDGYHR1yxs2VZml70IGfHzE=',
    'bm_sv': 'DBE7F362FD28C1ED9528BAAF4C1A2C73~YAAQjl86F7FFnoWdAQAAc+DYjx8Sk2s4qMxUHTQPBlx81Mfud8sv0F6Ey0C5IvOLPhgnagAWmycZVsKMhdMBxTk5vVce3SgNOMFWadZjq9VBnQNnhSr3O3MCBfRkmR9No7uZyH9wUBTbCrhDQ9u/Y7hg+IwDUVam1QR/YaAYWQ4Wv33CiG5+zQGjen9SVKdrZddf3BpzaUP++CWHr9CxLEIIIxYGHc39O8rWWVmdMX82lKFUUS1Wreee+OzufvI=~1',
    '_scid_r': 'VuNvXLZ_a-p9eDLdt-cDkS14K9FJCOOAct8QPQ',
    'bm_lso': 'DB5DFFD3AD81ACBBB294C01CE185479481701A02533892C7440737C30A3562C4~YAAQjl86F95CnoWdAQAA+8fYjwd4w+0guIqAgYXCTRhbMw7voQuPrc60NAXyxGLEU41Zf+iqzZDyfal1jt2aNO6POsxrBPNzWP2QCwsbygirKiOz+g7MoIrK9LWiamza8QiNaZUvLnt85FJZLuEnbE4wXP6AxgonIsnmxKCdUfSifdCC19mML66cLytMg1GVBVgtJ38kytzE2yMNoGMkXU3N1sLB9FZaATcuyP9gOa+SLNc2r8rOKpu3e1eTT0n14Wx8KBryLWXiO6NdHGkRLypONYZ6SUR96Heq7XEllnTU1jEHe+yzspoeoa2PkXRuGeMFuUHXrfth1IJjoQoGU/kK0SKbLPUsqXT0VpF+ySjUhi9oyBZMeSUk6sQTuWkmbT7lG4yBywW/4mBhMIdvmqe1qdZFX0a7ItwjYU+HdgV9DnC89QwjVwwxBJTYh7j5Xaz99InSsx5PfVMaYFngRg==~1776234848716',
    'cto_bundle': 'qmBaLV9GUGdGQ2pGSFQ0U2gwV2FlUjhFa1RLM0IlMkJrTGlXTVJ0ek9qWVpvbG92cHV3MW5ueTZ4aDR2MFh1N0N0Z0wwb0tIamxNME1aRDdmcjVDOThKWWx2bm01aWlnT0F0Z25wNUJHR2JOVWwzaWxHSVNJdGVucVRhdnEzbXdQVkZtcWVvbndmcHdGOVNrMXRvQXQwZkZsNjRyUSUzRCUzRA',
    'analytics_session_id.last_access': '1776234863347',
    '_ga_X3MNHK0RVR': 'GS2.1.s1776234708$o9$g1$t1776234868$j60$l0$h0',
}

headers = {
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'no-cache',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://www.ajio.com/',
    'sec-ch-ua': '"Google Chrome";v="147", "Not.A/Brand";v="8", "Chromium";v="147"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36',
}

import json
import re

def parse_json_from_script(tree):
    text = tree.xpath("//script[contains(text(), '__PRELOADED_STATE__')]/text()")
    
    data = {}
    
    if text:
        script_content = text[0].strip()
        
        script_content = script_content.replace("window.__PRELOADED_STATE__ =", "", 1).strip()
        
        if script_content.endswith(";"):
            script_content = script_content[:-1]
        
        try:
            data = json.loads(script_content)
                
        except Exception as e:
            print("JSON decode error:", e)
    else:
        print("JSON not found in script")
    
    return data


def clean_text(value: Any) -> str | None:
    if value is None:
        return None
    text = str(value).strip()
    if not text:
        return None
    return " ".join(text.split())


def as_int(value: Any) -> int | None:
    try:
        if value in (None, ""):
            return None
        return int(value)
    except (TypeError, ValueError):
        return None


def as_float(value: Any) -> float | None:
    try:
        if value in (None, ""):
            return None
        return float(value)
    except (TypeError, ValueError):
        return None


def normalize_url(value: Any) -> str | None:
    text = clean_text(value)
    if text is None:
        return None
    if text.startswith("http://") or text.startswith("https://"):
        return text
    if not text.startswith("/"):
        text = f"/{text}"
    return f"{BASE_URL}{text}"


def first_image_url(images: Any) -> str | None:
    if not isinstance(images, list):
        return None
    for image in images:
        if isinstance(image, dict):
            url = normalize_url(image.get("url"))
            if url:
                return url
    return None


def flatten_tags(tags: Any) -> list[str]:
    if not isinstance(tags, list):
        return []

    flattened = []
    for tag in tags:
        if isinstance(tag, dict):
            title = clean_text(tag.get("title"))
            if title:
                flattened.append(title)
        else:
            title = clean_text(tag)
            if title:
                flattened.append(title)
    return flattened


def get_price_block(entity: dict[str, Any], key: str) -> dict[str, Any]:
    block = entity.get(key)
    return block if isinstance(block, dict) else {}


def clean_listing_product(entity: dict[str, Any], position: int) -> dict[str, Any]:
    color_data = entity.get("fnlColorVariantData") if isinstance(entity.get("fnlColorVariantData"), dict) else {}
    price_data = get_price_block(entity, "price")
    was_price_data = get_price_block(entity, "wasPriceData")
    offer_price_data = get_price_block(entity, "offerPrice")

    return {
        "position": position,
        "product_id": clean_text(entity.get("code")),
        "product_name": clean_text(entity.get("name")),
        "brand_name": clean_text(color_data.get("brandName") or entity.get("brandTypeName")),
        "catalog_name": clean_text(entity.get("catalogName")),
        "product_url": normalize_url(entity.get("url")),
        "image_url": first_image_url(entity.get("images")) or normalize_url(color_data.get("outfitPictureURL")),
        "color_group": clean_text(color_data.get("colorGroup")),
        "coupon_status": clean_text(entity.get("couponStatus")),
        "discount_percent": clean_text(entity.get("discountPercent")),
        "price": as_int(price_data.get("value") or entity.get("price")),
        "original_price": as_int(was_price_data.get("value") or entity.get("wasPrice")),
        "offer_price": as_int(offer_price_data.get("value") or offer_price_data.get("price") or entity.get("offerPrice")),
        "average_rating": as_float(entity.get("averageRating")),
        "rating_count": clean_text(entity.get("ratingCount")),
        "segment_name": clean_text(entity.get("segmentName")),
        "segment_name_text": clean_text(entity.get("segmentNameText")),
        "vertical_name": clean_text(entity.get("verticalName")),
        "vertical_name_text": clean_text(entity.get("verticalNameText")),
        "brick_name": clean_text(entity.get("brickName")),
        "brick_name_text": clean_text(entity.get("brickNameText")),
        "seller_id": clean_text(entity.get("sellerId")),
        "seller_sku": clean_text(entity.get("sellerSku")),
        "planning_category": clean_text((entity.get("fnlProductData") or {}).get("planningCategory") if isinstance(entity.get("fnlProductData"), dict) else None),
        "tags": flatten_tags(entity.get("tags")),
    }


def extract_listing_products(payload: dict[str, Any]) -> list[dict[str, Any]]:
    grid = payload.get("grid") if isinstance(payload.get("grid"), dict) else {}
    results = grid.get("results", [])
    entities = grid.get("entities", {}) if isinstance(grid.get("entities"), dict) else {}

    cleaned_products = []
    for position, product_id in enumerate(results, start=1):
        entity = entities.get(product_id)
        if not isinstance(entity, dict) or not entity:
            continue
        cleaned_products.append(clean_listing_product(entity, position))
    return cleaned_products


def search_products(query):
    url=f'https://www.ajio.com/api/home/search/{query}'
    response = session.get(url, cookies=cookies, headers=headers)
    print(response)
    data=response.json()
    responseSource=data.get("responseSource", "")
    suggestion=data.get("suggestions",[])

    text=suggestion[0]['value'] if suggestion else ""
    if not text:
        print("No suggestions found for the query.")
        return {"Error": "No suggestions found for the query."}
    
    print("*"*50)    
    print(f"Searching suggestion for: {text}")
    print("*"*50)
    response = session.get(f'https://www.ajio.com/search/?text={text}&responseSource={responseSource}', cookies=cookies, headers=headers)
    print(response)


    tree=html.fromstring(response.text)
    json_data=parse_json_from_script(tree)
    
    cleaned_products = extract_listing_products(json_data)

    return {"First Suggestion": text, "products": cleaned_products}
    