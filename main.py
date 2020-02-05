"""main.py"""
import website_alive.make_request


URL = ("https://github.com/katerinoc")

"""Analyze if site have access"""
if website_alive.make_request.make_request(URL) is True:
    print('Сайт доступен')
else:
    print('Сайт недоступен')
