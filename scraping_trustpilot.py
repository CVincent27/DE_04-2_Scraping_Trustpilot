import requests
from bs4 import BeautifulSoup

def get_all_pages():
    urls = []
    page_number = 1

    for i in range(20):
        i = f"https://fr.trustpilot.com/categories/electronics_technology?claimed=true&page={page_number}&subcategories=internet_software"
        page_number += 1
        urls.append(i)
    print(urls)


# print(r.status_code)
get_all_pages()