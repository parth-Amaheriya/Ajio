from curl_cffi import requests
import json
from lxml import html
import re
from db import *

# from product_parser import parser_product_links

home_url="https://www.ajio.com"
api_url="https://www.ajio.com/api/category/"

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
    'cdigiMrkt': 'utm_source%3A%7Cutm_medium%3A%7Cdevice%3Ad%7Cexpires%3AWed%2C%2013%20May%202026%2010%3A20%3A16%20GMT%7C',
    '_scid': 'SmNvXLZ_a-p9eDLdt-cDkS14K9FJCOOA',
    'V': '201',
    '_sctr': '1%7C1776018600000',
    'dtm_token': 'AQAKPidI4MB8tgE2FmbAAQBFtwABAQCcPd_cLwEBAJyLHop8',
    'dtm_consent': 'UNSPECIFIED',
    'ADRUM_BT': 'R:73|i:4841|g:7a17f061-7a0a-4cff-87a3-a3398df476d92431504|e:796|n:customer1_be12de70-87be-45ee-86d9-ba878ff9a400',
    'TS01d405db': '015d0fa226063593ffbcdc33dd1a879c0c953acff1f4781b223f9655c2024dd6d78b5421706e7a49255842fbd3556593609f06fe1e',
    'bm_ss': 'ab8e18ef4e',
    'bm_so': '864B07C3295CC55428854EEC4C4EE0E6CE2E1D528C9E81AAA59DC8A6B42A25F0~YAAQBO+ctgCKf2+dAQAAAk9Riwd/LelPZSpE9jPiAhjN76XTp5iDcCInkdG7IX4GanJnfHAy2azg3TcCd1y6PjC23byiP+y9VN9Wo6xAYzUJIvjTDi3Eh+FABFhOyhJVgznF1UFluDH4vpAWpz0P3tkPQ0z9duNFUMUk2QN1WQ8vCokhLA9SzOMnK+CtWrGLnWITYXLcgSmSWW2FshNqA7AAW0ldTGehKCxYjHocWmQ/qywLqIkwry5ChMs5TyJ/w9p1f5dXvlW7yOqJ1ac7tFhEC369KDYDFOHNxRMSmBia5uRzDG/toLKYaHeUkGWb0nZr3zN/7A+VBjoEM5+SE2uZ59+vLOD2v8hsp1wVhmnVGeZKQxzIg8VxhB8Fc+WLpeXkAtmdeLFvzBGHY/aDSMLH59gOh1YCN/+q4hFIioaBtulg6In79u9nvUPrzn2VG/e0fvqDMm7LynDliqKCXQ==',
    'bm_sz': 'BCE5CE3F407D464DA0D43FAECE6E99F6~YAAQBO+ctgGKf2+dAQAAAk9Rix88GukpN5+OuPwrqeDq4j7WLvXDAlUK2qKJBOcmzuDvVgHG0hnC+2h8COIV/KsRDgWzizlWSDe27QJ3SDUKufZyebymG6uLRPlhJhPR5Mu4swcbwmki2dT021RzHnZPwBYFolDIljeEzlRfQYGGyPglvLsyMNzh703kXYmq1PAkIxAnJDkxuIu5csFeydePMKQitZxZQuP7CPuvI+34bEAm/2c0+qivtxsO/aqB9sl9Od2mCmU4YrPiT9KX6BOXYJNout/4ZPFPJjZQgrABEGqAGYKJwFCwcQibpEiZ3htm4R3VJL0qqNRNdk7r7LGLV80GUlffSTZLOZAJJyHqv0IjRFY=~3224627~4342081',
    'ak_bmsc': '7F241EE39B3701362D18C72B3FA4F220~000000000000000000000000000000~YAAQBO+ctl6Kf2+dAQAAQlNRix//DDKfHueLZHjchWlFaJPH8d3g7K0Om9YTu8JEhTKV48OXiGyDlWAZfXK6dJTo72a5MVaFMy4xpka3LKujRwG9phxP9mqStzAe0XzlOvWLWZZGlzgSEurg7ebnXXgk5ouHsXJ9zZzklbzReEfluCYJFyRvOiuGG+eFYJirJVimOPAK37W1C5cpxoQQLENc+VW5wz0PzZJfB28MhwGy7wLtGikDuCKvvZacs0HTIlmuuJYXycHu3mprjGyeRmmWuFcGi3HEM7L3ZO8nO5vsJLMzECWYNG5NjeYLDcTCtCd5uLWAOaTOzhEKAGnl0cJW3gijpY2mh5hjSrFP9+fy5GHllgZv+x9YOrmr+T3m',
    '_abck': '6A06F762CCF36DE6D16BDFF9F87CC38F~0~YAAQBO+ctnWKf2+dAQAAZlRRiw+DkHtDeJq5qDHZZydGLo34MAXGR5qgzoyM6St6mVWcfxB8dfncdXcnK3F8p8DvIXZbrPr7fjlV8ZuBD5JMXxp04fSzZkks46s8z6WYIwvdFase5hf1tnwHCnFvRd7M/dH1Ss9OQatkvXw3LwUJMUtYnxhas6AXbKWPWS4I9jrOEwUc82lqMEucdl9M/6wIj7BL3JcYBdRMpYNt+yqe04/FGJf8MIuxqmWHtGdVy2YQQAuvZ+il7IoZRwmmLX6IpHzos+bUgrj+t0k3+u+uiu3sbf2MQ0LoeYKrcsFmkj6gs0Cd5MTnOpaz/zpR/mXGOS8usZR9UVuPNXW5rZEOievXDOZqifGGQhUt8YkrSFnnS9SG2AXi65bvKYMqhKabKAm8FOGzFwIwAv3LuJPsz7ZK3AW5pi5FDDLj/3bXAFo8fQBc/DiCRzOmTwvY8yRezeGcWwavCXzKjprv3tcexlu1SjIsbUmGCAXtuyWlcgKNn3SD3CvQeWZ2V3Xmn4X05mNDbwGXfQrkXeWsO18gjW1cuiqlyE57hyjNW3GjJlyu9sCrUBmdybbQ8Bn8bwgB2JGUqOj/SPDz2dys4rSC97LLXlYaYWZ+H4XuNCGJZltg7misGdd/ZV0pQaf1op2VnPQTRxGJpH1Uc9GsIZ1oVGmrvDF5U8S+PH/MX2jJUsg=~-1~-1~1776162456~AAQAAAAF%2f%2f%2f%2f%2f+r8fgDT+iLaDPLfiV7QXMb+6ePYWM0nhKmKpefmNc9TFchWQZqwa1ZHfElBe3OcQ5GeVRsEbqaggJYPEIXFWgzOI5MIMpTbYveLQtKX0ydGOZJLBuTJ5008N5qGCexg9I34tME%3d~-1',
    'sessionStatus': 'true|undefined',
    'segment_user_id': 'null',
    'segment_device_id': '380be5ff-4ea2-4f58-b167-731f93838fa5',
    'analytics_session_id': '1776158857747',
    '_derived_epik': 'dj0yJnU9endhN1BicnUtLUVET18wTUpnc2x5dHo1RVl0WWhSTjMmbj1aSUtBWXVJZW9vTlJEOTRVaGRkTFVRJm09MSZ0PUFBQUFBR25lQ0lvJnJtPTEmcnQ9QUFBQUFHbmVDSW8mc3A9Mg',
    'g_state': '{"i_l":0,"i_ll":1776158858641,"i_b":"u8eL3103fmNAkln4cYcTjK8aFGOPCVO6sPTWQE2BSJ4","i_e":{"enable_itp_optimization":22},"i_et":1776138817430}',
    '_dc_gtm_UA-68002030-1': '1',
    'ImpressionCookie': '0',
    'FirstPage': 'Tue Apr 14 2026 14:57:39 GMT+0530 (India Standard Time)',
    '_ga': 'GA1.1.671363337.1776075612',
    'bm_lso': '864B07C3295CC55428854EEC4C4EE0E6CE2E1D528C9E81AAA59DC8A6B42A25F0~YAAQBO+ctgCKf2+dAQAAAk9Riwd/LelPZSpE9jPiAhjN76XTp5iDcCInkdG7IX4GanJnfHAy2azg3TcCd1y6PjC23byiP+y9VN9Wo6xAYzUJIvjTDi3Eh+FABFhOyhJVgznF1UFluDH4vpAWpz0P3tkPQ0z9duNFUMUk2QN1WQ8vCokhLA9SzOMnK+CtWrGLnWITYXLcgSmSWW2FshNqA7AAW0ldTGehKCxYjHocWmQ/qywLqIkwry5ChMs5TyJ/w9p1f5dXvlW7yOqJ1ac7tFhEC369KDYDFOHNxRMSmBia5uRzDG/toLKYaHeUkGWb0nZr3zN/7A+VBjoEM5+SE2uZ59+vLOD2v8hsp1wVhmnVGeZKQxzIg8VxhB8Fc+WLpeXkAtmdeLFvzBGHY/aDSMLH59gOh1YCN/+q4hFIioaBtulg6In79u9nvUPrzn2VG/e0fvqDMm7LynDliqKCXQ==~1776158859297',
    '_scid_r': 'WONvXLZ_a-p9eDLdt-cDkS14K9FJCOOAct8Q8w',
    'cto_bundle': 'qvxU2V9GUGdGQ2pGSFQ0U2gwV2FlUjhFa1RKdWxDUzhraG9XeTZZdjV4cXVZUFdFcDhCd3RoV2l6YjNsTlJnbG1hS2J2dHdGcmlmVkYxQXk4SmNuSDA1SzBqVjdjMlpLME1KRFlSTmNVeXF3S2NJekFWNCUyQlRFaUpPQmx6T0ZQbTZjSlRyME02UXN1R0FTYmMlMkZwWGphMmxLVENRJTNEJTNE',
    'bm_s': 'YAAQBO+ctj+Mf2+dAQAAzmZRiwV5jVOBzGkq6p5C5kVwsWrEUy5/SgsymAVtrgGol2A3QegS3xREJkPThB8Ab6yhO8+fS2kmHQckRfa8ejDwW9/rjBU/pqGtogCOo1qRxWmF5GQMymXNVcZD+4qvPBmFeC33ScJ0WUvPJqkqv4kK6tuUcgZ4cF10Cz0LJxxFyoJV/6ys6pjJ4qFpnBIus0NHi1h8BsExIjb1boq0ZZGEF4+n9cG5kXux7KmSwG8pSKovc5TESQW5WAnkc5sh26wWPyLRDyOQWR4roAZnHu9t8PVDHKhMtkrintypRcXA1fIU6PQiI2DkSNctzCuVcPpwdmTLAqfQT5ueCjOelZFWSxe8Y1iP+zke1JaiLRtfmQf54EWP5F4k8IPL0uQ0dfvjXPnX6HdPKtXZDQodbOXs81IwywZRvpHJPYz/T+v9Z1Z9U1ZNh6GNtpVu3XMBAbxjpvrP9NCDYQyD+PUhmcIzpNIm0pD2PrbmzYItwD1gs5nf/V2G29idIUIstg1FC4iTLWR9k2yBnUzKrl5X4LT1PSsRHwR8bU5pEP28w7XuoLiasXboJmaG4bQu7RPM87jBaX8vBWJ1xqTUvvxfKEga3lO46ky9tUzpbi2id3NoGMMWcA5p+yhuUlKQ1bq+Sg0rpVxJ8OGjzhYSkXvphWcPxcRipO1MZ/NTjdxaoe7+oXK91kW89/P0DNMd5nLTnhSUg4rfsburj79sgjg7KrZZSd+I7zFa2dagTWP/4Ep4zs/aQwMKyDzuV5elWdOSiDeMATDoI/zza5yzrZvR9CGGGiSH5iCewasfZXE2Nv9dt+PkpUHV2Fw02ePKPAubAQOk9h9V0Gy+v5dq7/QgxXk+6w==',
    'ajiosessionid': 'DE3121E93EDBA30CA9825933B8A687AE.a3684',
    'bm_sv': '03F0BAC707FD240AA93A32996A04C88B~YAAQDO+ctqdFVVedAQAAq3NRix8OhX6j7rAEWCAGpPYAN0QqUaOR5QKFH4vc4NeROrcB0Bz4+JZfM7AEwbL4GR32BjfXjasVAG+tQIf4stTNjh5ylLleeP9xYTBKBjYeCpZpwNojOldXy5GXbj2N9zROFAw+tioBkljqP0ZgCOcRMcRP4biFYQeRpnoTh8wIffYDn+8LIh8MpjUMZvwrAdE3VgudUdg2MRYRot+7VLuChCRZVKUHh6iKvG+paw==~1',
    '_ga_X3MNHK0RVR': 'GS2.1.s1776158859$o5$g0$t1776158883$j36$l0$h0',
    'analytics_session_id.last_access': '1776158883040',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'if-none-match': 'W/"b79b5-7TcrwuM8B4CPBGD7gxnqr3zrvYI"',
    'priority': 'u=0, i',
    'referer': 'https://www.ajio.com/sw.js?jioCdnUrl=https%3A%2F%2Fassets-jiocdn.ajio.com',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'same-origin',
    'sec-fetch-site': 'same-origin',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36',
    # 'cookie': '_gcl_au=1.1.1242066138.1776075611; AB=B; _gid=GA1.2.839209906.1776075612; _fbp=fb.1.1776075615037.855111222913757446; ajs_anonymous_id=380be5ff-4ea2-4f58-b167-731f93838fa5; _pin_unauth=dWlkPU5qaGpNVE5sTlRVdFlXSTJOQzAwTmprM0xXRTJNR010WkRjMk9ESTRZVGRpT0RZeA; _fpuuid=SFQ0F_Cis7JjD1dbjnZwN; deviceId=SFQ0F_Cis7JjD1dbjnZwN; ifa=cc0a5cec-0156-4257-b29e-586a76400634; os=4; vr=WEB-2.0.11; cdigiMrkt=utm_source%3A%7Cutm_medium%3A%7Cdevice%3Ad%7Cexpires%3AWed%2C%2013%20May%202026%2010%3A20%3A16%20GMT%7C; _scid=SmNvXLZ_a-p9eDLdt-cDkS14K9FJCOOA; V=201; _sctr=1%7C1776018600000; dtm_token=AQAKPidI4MB8tgE2FmbAAQBFtwABAQCcPd_cLwEBAJyLHop8; dtm_consent=UNSPECIFIED; ADRUM_BT=R:73|i:4841|g:7a17f061-7a0a-4cff-87a3-a3398df476d92431504|e:796|n:customer1_be12de70-87be-45ee-86d9-ba878ff9a400; TS01d405db=015d0fa226063593ffbcdc33dd1a879c0c953acff1f4781b223f9655c2024dd6d78b5421706e7a49255842fbd3556593609f06fe1e; bm_ss=ab8e18ef4e; bm_so=864B07C3295CC55428854EEC4C4EE0E6CE2E1D528C9E81AAA59DC8A6B42A25F0~YAAQBO+ctgCKf2+dAQAAAk9Riwd/LelPZSpE9jPiAhjN76XTp5iDcCInkdG7IX4GanJnfHAy2azg3TcCd1y6PjC23byiP+y9VN9Wo6xAYzUJIvjTDi3Eh+FABFhOyhJVgznF1UFluDH4vpAWpz0P3tkPQ0z9duNFUMUk2QN1WQ8vCokhLA9SzOMnK+CtWrGLnWITYXLcgSmSWW2FshNqA7AAW0ldTGehKCxYjHocWmQ/qywLqIkwry5ChMs5TyJ/w9p1f5dXvlW7yOqJ1ac7tFhEC369KDYDFOHNxRMSmBia5uRzDG/toLKYaHeUkGWb0nZr3zN/7A+VBjoEM5+SE2uZ59+vLOD2v8hsp1wVhmnVGeZKQxzIg8VxhB8Fc+WLpeXkAtmdeLFvzBGHY/aDSMLH59gOh1YCN/+q4hFIioaBtulg6In79u9nvUPrzn2VG/e0fvqDMm7LynDliqKCXQ==; bm_sz=BCE5CE3F407D464DA0D43FAECE6E99F6~YAAQBO+ctgGKf2+dAQAAAk9Rix88GukpN5+OuPwrqeDq4j7WLvXDAlUK2qKJBOcmzuDvVgHG0hnC+2h8COIV/KsRDgWzizlWSDe27QJ3SDUKufZyebymG6uLRPlhJhPR5Mu4swcbwmki2dT021RzHnZPwBYFolDIljeEzlRfQYGGyPglvLsyMNzh703kXYmq1PAkIxAnJDkxuIu5csFeydePMKQitZxZQuP7CPuvI+34bEAm/2c0+qivtxsO/aqB9sl9Od2mCmU4YrPiT9KX6BOXYJNout/4ZPFPJjZQgrABEGqAGYKJwFCwcQibpEiZ3htm4R3VJL0qqNRNdk7r7LGLV80GUlffSTZLOZAJJyHqv0IjRFY=~3224627~4342081; ak_bmsc=7F241EE39B3701362D18C72B3FA4F220~000000000000000000000000000000~YAAQBO+ctl6Kf2+dAQAAQlNRix//DDKfHueLZHjchWlFaJPH8d3g7K0Om9YTu8JEhTKV48OXiGyDlWAZfXK6dJTo72a5MVaFMy4xpka3LKujRwG9phxP9mqStzAe0XzlOvWLWZZGlzgSEurg7ebnXXgk5ouHsXJ9zZzklbzReEfluCYJFyRvOiuGG+eFYJirJVimOPAK37W1C5cpxoQQLENc+VW5wz0PzZJfB28MhwGy7wLtGikDuCKvvZacs0HTIlmuuJYXycHu3mprjGyeRmmWuFcGi3HEM7L3ZO8nO5vsJLMzECWYNG5NjeYLDcTCtCd5uLWAOaTOzhEKAGnl0cJW3gijpY2mh5hjSrFP9+fy5GHllgZv+x9YOrmr+T3m; _abck=6A06F762CCF36DE6D16BDFF9F87CC38F~0~YAAQBO+ctnWKf2+dAQAAZlRRiw+DkHtDeJq5qDHZZydGLo34MAXGR5qgzoyM6St6mVWcfxB8dfncdXcnK3F8p8DvIXZbrPr7fjlV8ZuBD5JMXxp04fSzZkks46s8z6WYIwvdFase5hf1tnwHCnFvRd7M/dH1Ss9OQatkvXw3LwUJMUtYnxhas6AXbKWPWS4I9jrOEwUc82lqMEucdl9M/6wIj7BL3JcYBdRMpYNt+yqe04/FGJf8MIuxqmWHtGdVy2YQQAuvZ+il7IoZRwmmLX6IpHzos+bUgrj+t0k3+u+uiu3sbf2MQ0LoeYKrcsFmkj6gs0Cd5MTnOpaz/zpR/mXGOS8usZR9UVuPNXW5rZEOievXDOZqifGGQhUt8YkrSFnnS9SG2AXi65bvKYMqhKabKAm8FOGzFwIwAv3LuJPsz7ZK3AW5pi5FDDLj/3bXAFo8fQBc/DiCRzOmTwvY8yRezeGcWwavCXzKjprv3tcexlu1SjIsbUmGCAXtuyWlcgKNn3SD3CvQeWZ2V3Xmn4X05mNDbwGXfQrkXeWsO18gjW1cuiqlyE57hyjNW3GjJlyu9sCrUBmdybbQ8Bn8bwgB2JGUqOj/SPDz2dys4rSC97LLXlYaYWZ+H4XuNCGJZltg7misGdd/ZV0pQaf1op2VnPQTRxGJpH1Uc9GsIZ1oVGmrvDF5U8S+PH/MX2jJUsg=~-1~-1~1776162456~AAQAAAAF%2f%2f%2f%2f%2f+r8fgDT+iLaDPLfiV7QXMb+6ePYWM0nhKmKpefmNc9TFchWQZqwa1ZHfElBe3OcQ5GeVRsEbqaggJYPEIXFWgzOI5MIMpTbYveLQtKX0ydGOZJLBuTJ5008N5qGCexg9I34tME%3d~-1; sessionStatus=true|undefined; segment_user_id=null; segment_device_id=380be5ff-4ea2-4f58-b167-731f93838fa5; analytics_session_id=1776158857747; _derived_epik=dj0yJnU9endhN1BicnUtLUVET18wTUpnc2x5dHo1RVl0WWhSTjMmbj1aSUtBWXVJZW9vTlJEOTRVaGRkTFVRJm09MSZ0PUFBQUFBR25lQ0lvJnJtPTEmcnQ9QUFBQUFHbmVDSW8mc3A9Mg; g_state={"i_l":0,"i_ll":1776158858641,"i_b":"u8eL3103fmNAkln4cYcTjK8aFGOPCVO6sPTWQE2BSJ4","i_e":{"enable_itp_optimization":22},"i_et":1776138817430}; _dc_gtm_UA-68002030-1=1; ImpressionCookie=0; FirstPage=Tue Apr 14 2026 14:57:39 GMT+0530 (India Standard Time); _ga=GA1.1.671363337.1776075612; bm_lso=864B07C3295CC55428854EEC4C4EE0E6CE2E1D528C9E81AAA59DC8A6B42A25F0~YAAQBO+ctgCKf2+dAQAAAk9Riwd/LelPZSpE9jPiAhjN76XTp5iDcCInkdG7IX4GanJnfHAy2azg3TcCd1y6PjC23byiP+y9VN9Wo6xAYzUJIvjTDi3Eh+FABFhOyhJVgznF1UFluDH4vpAWpz0P3tkPQ0z9duNFUMUk2QN1WQ8vCokhLA9SzOMnK+CtWrGLnWITYXLcgSmSWW2FshNqA7AAW0ldTGehKCxYjHocWmQ/qywLqIkwry5ChMs5TyJ/w9p1f5dXvlW7yOqJ1ac7tFhEC369KDYDFOHNxRMSmBia5uRzDG/toLKYaHeUkGWb0nZr3zN/7A+VBjoEM5+SE2uZ59+vLOD2v8hsp1wVhmnVGeZKQxzIg8VxhB8Fc+WLpeXkAtmdeLFvzBGHY/aDSMLH59gOh1YCN/+q4hFIioaBtulg6In79u9nvUPrzn2VG/e0fvqDMm7LynDliqKCXQ==~1776158859297; _scid_r=WONvXLZ_a-p9eDLdt-cDkS14K9FJCOOAct8Q8w; cto_bundle=qvxU2V9GUGdGQ2pGSFQ0U2gwV2FlUjhFa1RKdWxDUzhraG9XeTZZdjV4cXVZUFdFcDhCd3RoV2l6YjNsTlJnbG1hS2J2dHdGcmlmVkYxQXk4SmNuSDA1SzBqVjdjMlpLME1KRFlSTmNVeXF3S2NJekFWNCUyQlRFaUpPQmx6T0ZQbTZjSlRyME02UXN1R0FTYmMlMkZwWGphMmxLVENRJTNEJTNE; bm_s=YAAQBO+ctj+Mf2+dAQAAzmZRiwV5jVOBzGkq6p5C5kVwsWrEUy5/SgsymAVtrgGol2A3QegS3xREJkPThB8Ab6yhO8+fS2kmHQckRfa8ejDwW9/rjBU/pqGtogCOo1qRxWmF5GQMymXNVcZD+4qvPBmFeC33ScJ0WUvPJqkqv4kK6tuUcgZ4cF10Cz0LJxxFyoJV/6ys6pjJ4qFpnBIus0NHi1h8BsExIjb1boq0ZZGEF4+n9cG5kXux7KmSwG8pSKovc5TESQW5WAnkc5sh26wWPyLRDyOQWR4roAZnHu9t8PVDHKhMtkrintypRcXA1fIU6PQiI2DkSNctzCuVcPpwdmTLAqfQT5ueCjOelZFWSxe8Y1iP+zke1JaiLRtfmQf54EWP5F4k8IPL0uQ0dfvjXPnX6HdPKtXZDQodbOXs81IwywZRvpHJPYz/T+v9Z1Z9U1ZNh6GNtpVu3XMBAbxjpvrP9NCDYQyD+PUhmcIzpNIm0pD2PrbmzYItwD1gs5nf/V2G29idIUIstg1FC4iTLWR9k2yBnUzKrl5X4LT1PSsRHwR8bU5pEP28w7XuoLiasXboJmaG4bQu7RPM87jBaX8vBWJ1xqTUvvxfKEga3lO46ky9tUzpbi2id3NoGMMWcA5p+yhuUlKQ1bq+Sg0rpVxJ8OGjzhYSkXvphWcPxcRipO1MZ/NTjdxaoe7+oXK91kW89/P0DNMd5nLTnhSUg4rfsburj79sgjg7KrZZSd+I7zFa2dagTWP/4Ep4zs/aQwMKyDzuV5elWdOSiDeMATDoI/zza5yzrZvR9CGGGiSH5iCewasfZXE2Nv9dt+PkpUHV2Fw02ePKPAubAQOk9h9V0Gy+v5dq7/QgxXk+6w==; ajiosessionid=DE3121E93EDBA30CA9825933B8A687AE.a3684; bm_sv=03F0BAC707FD240AA93A32996A04C88B~YAAQDO+ctqdFVVedAQAAq3NRix8OhX6j7rAEWCAGpPYAN0QqUaOR5QKFH4vc4NeROrcB0Bz4+JZfM7AEwbL4GR32BjfXjasVAG+tQIf4stTNjh5ylLleeP9xYTBKBjYeCpZpwNojOldXy5GXbj2N9zROFAw+tioBkljqP0ZgCOcRMcRP4biFYQeRpnoTh8wIffYDn+8LIh8MpjUMZvwrAdE3VgudUdg2MRYRot+7VLuChCRZVKUHh6iKvG+paw==~1; _ga_X3MNHK0RVR=GS2.1.s1776158859$o5$g0$t1776158883$j36$l0$h0; analytics_session_id.last_access=1776158883040',
}
def parse_json_from_script(tree):
    text=tree.xpath("//script[contains(text(), '__PRELOADED_STATE__')]/text()")
    match=re.search(r'window\.__PRELOADED_STATE__\s*=\s*(\{[\s\S]*\})\s*;?', text[0] if text else "")
    data={}
    if match:
        json_str=match.group(1)
        json_str=re.sub(r',\s*}', '}', json_str)

        data=json.loads(json_str)\
        
        with open("ajio.json","w",encoding="utf-8") as f:
            json.dump(data,f,indent=4)
        
    else:
        print("JSON not found in script")
    return data    
def extract_category_links(data):
    final_output = {}
    json_data = data.get("navigation", {})

    def get_links(nodes, current_path):
        links = {}
        for node in nodes:
            name = node.get("name")
            url = node.get("url")
            pageType = node.get("pageType")
            children = node.get("childDetails") or []

            if not name:
                continue

            full_path = f"{current_path} > {name}" if current_path else name

            if '/c/' in url and url.strip():
                links[full_path] = {"category_url": home_url + url, "api_url": api_url+url.split('/c/')[-1]}

            # Decide next prefix
            child_prefix = full_path if url and url.strip() else current_path

            if isinstance(children, list) and children:
                links.update(get_links(children, child_prefix))

        return links
    top_categories = json_data.get("data", {}).get("childDetails", [])

    for cat_node in top_categories:
        cat_name = cat_node.get("name")
        cat_children = cat_node.get("childDetails") or []

        links = get_links(cat_children, cat_name)

        final_output.update(links)

    return final_output


    
def main(url):
    create_schema()
    if not has_categories():
       
        response=requests.get(url, impersonate="chrome",cookies=cookies, headers=headers)
        print(response.status_code)
        tree=html.fromstring(response.text)
        json_data=parse_json_from_script(tree)
        category_links=extract_category_links(json_data)
        category_links.update({
        "Other": {
            "category_url": "https://www.ajio.com/s/83",
            "api_url": "https://www.ajio.com/api/category/83"
            }
        })

        with open("ans.json", "w", encoding="utf-8") as f:
            json.dump(category_links, f, indent=4, ensure_ascii=False)

        count=insert_category_link(category_links)

        print(f"Category links extracted and saved to ans.json. Inserted {count} links.")
    else:
        print("Category links already exist. Skipping extraction.")


    # parser_product_links(category_links)

if __name__=="__main__":
    main(home_url)