# _*_coding :utf-8 _*_
# @Time :2022/10/23 20:53
# @File : 002_爬取网易音乐
# @Project : python-crawl

import requests


url = 'https://music.163.com/#/search/m/?s=%E5%91%A8%E6%9D%B0&type=1'
headers = {
    "Host": "music.163.com",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0",
    "Referer": "https://music.163.com/",
    "DNT": "1",
    "Connection": "keep-alive",
    "Cookie": "NMTID=00OX6LmGACNKHrnaE_ooO48oGIFZDkAAAF__xQvpw; JSESSIONID-WYYY=brqNgNxtbhzzIwbyWFWKQK3pEOuU0sdlPcfPeihNcEpRQUG8R2YsC4%2FMz6PyoZlMkzytbXCt44T8Z9iPn0jdcoQOWPwYY8t%5Cte99PO7z04Ig2FtalNSZkcBh8EyGUxwW5UqGEHA9cvwYXq%2FVzDDmlqMbCVBOrK3xQCXh%2FfjzdJM%5CxviC%3A1666530207942; _iuqxldmzr_=32; _ntes_nnid=c1f85b1b44f1fa6c8865f8e6da2cd3e6,1649334307782; _ntes_nuid=c1f85b1b44f1fa6c8865f8e6da2cd3e6; WEVNSM=1.0.0; WNMCID=pswqyf.1649334310427.01.0; WM_NI=FChtWI4ipFXbwWHk87UfgUajrsnKi6jfucdSloaglTlAnQl3B4SCB4gyCeZKUOJ0IiGU1XRQ3b068u5Ewe81AGiJoJ%2Far6M5gfg7y8piD76CjIz22nGroGRFgNh%2FtfrCTmo%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6ee8adb7de99bbd92dc3f9cbc8fa7c45a978a9aadc146928f978bbc7ff8eda2baed2af0fea7c3b92a869da895d643f8b7c0a7db6ab589888cbb3d97baa9b6e462b2ada2acec3eaababb84e759b0b1af88ef60b09fa2b2ef3982ec9da4c140a5a78d86d941979186d1cc63858bffb9d15bf1be00d7bb7ff79bb986bb3b8399a7abee42edbfbed7d03fa5baa9d8fc34b4b78cd8b549aa97b6d3b16685aea1a8d14ea592a8d0f76eb29d9c8eee37e2a3; WM_TID=7NA%2BmRFLMq5EFRAFBVKFYRQMjsu82nZi; ntes_kaola_ad=1; _ga_C6TGHFPQ1H=GS1.1.1650713400.2.0.1650713400.0; _ga=GA1.1.1850846699.1650632237; Qs_lvt_382223=1650632246; Qs_pv_382223=516945592105492860; _clck=1kkir74|1|f0v|0; __snaker__id=okp0mOsmUWaODeS7; YD00000558929251%3AWM_NI=HWawVUyPOYBiJYnudnIxQerwnqRr2JzBM%2FpRFDhE7H3cPVuGApa4LnsCj9bh91%2FPfKVpc9KiSb0z%2BGQoL3Cp3y3jo7KeZ4nxbLjdcICneFR9059dA1X7QqbKnzgJ8urjYmY%3D; YD00000558929251%3AWM_NIKE=9ca17ae2e6ffcda170e2e6ee8bee4ab8b3b68ddc6f8eef8fa2d14a868f8b86d869829a8491e85aa8bff8acf52af0fea7c3b92a8c89af98d55fbb9081bac1638a87a296e7668ba89f86f17daeaf9e93b142ba9e83d0f35a869ca8a6b644f1bda0b7f84d83b0afd5cf66b19da6dae164fbefe1b1e54196b0addaca6391be009baa4d93b184d4c27cf1a7fd8bee3d89bb96d5ed74a294a685e24381b2aba7d133f4ebf785c43b9ce99f92e141aea6a9abbb7fb2b6978edc37e2a3; YD00000558929251%3AWM_TID=r6DZZh4ujTFEERFAUAKRJBBK9bAdO5au; gdxidpyhxdE=70lm9KRkEkEarntwWQxdiqESLIBUn6ArrTXAAJHhQvy4BGbEhKDtNbetKH%5CoCCP%2BwrjCY9rbxR4c6RvEjTHUkoncWe1nBRhTdZ7bE994byNsmBVIy%2B5BfmmT7iI7OEevsdTNmvdLBCe%2FRYXDxQRsgf1eL4gaJ0CMoZTaU2ZWdTilvMox%3A1666516121598; _9755xjdesxxd_=32; MUSIC_U=04e36d991bd94f676c3157d7afebbb6bf89e5726f86124c6e2f0e03a78adc35e519e07624a9f0053cbe959b7709d2cd0cf8ac103cb2c022ad7c6b7f4865bf4fdf9228a3743b2486cd4dbf082a8813684; playerid=88713648; __csrf=03f9c49af4ce95d10c697e8e53ebf7b9",
    "Upgrade-Insecure-Requests": "1",

}

response = requests.get(url).text

print(response)

































