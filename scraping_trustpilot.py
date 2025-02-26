import requests
from bs4 import BeautifulSoup

def get_all_pages():
    urls = []
    page_number = 1

    for i in range(20):
        i = f"https://fr.trustpilot.com/categories/electronics_technology?claimed=true&page={page_number}&subcategories=internet_software"
        page_number += 1
        urls.append(i)
    # print(urls)
    return urls


# print(r.status_code)
get_all_pages()

def parse_companies():
    r = requests.get("https://fr.trustpilot.com/categories/electronics_technology?claimed=true&page=1&subcategories=internet_software")
    soup = BeautifulSoup(r.content, "html.parser")

    print(soup)

parse_companies()