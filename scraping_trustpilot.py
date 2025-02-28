import requests
from bs4 import BeautifulSoup
import re

# Récup des 20 premières pages du site
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

# Récup des infos des entreprises
def parse_companies(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")

    companies = soup.find_all('div', class_='paper_paper__EGeEb paper_outline__bqVmn card_card__yyGgu card_noPadding__OOiac styles_wrapper__Jg8fe')
    # print(len(companies))
    for companie in companies:
        name = companie.find('p').text
        website = companie.find('p', class_='typography_body-m__k2UI7 typography_appearance-subtle__PYOVM styles_websiteUrlDisplayed__lSw1A').text
        rating = companie.find('span', class_='typography_body-m__k2UI7 typography_appearance-subtle__PYOVM styles_trustScore__iURkS').text
        nbr_rating = companie.find('p', class_='typography_body-m__k2UI7 typography_appearance-subtle__PYOVM styles_ratingText__A2dmB').text
        clean_nbr_rating = re.sub(r"\|", " - ", nbr_rating)
        address = companie.find('div', class_='styles_metadataRow__WKWNi').text
        if not address:
            address = "Pas d'adresse"
        tag = companie.find('span', class_='typography_body-s__IqDta typography_appearance-default__t8iAq').text
        
        # print(clean_nbr_rating)

        path = r"C:\Users\coque\OneDrive\Bureau\dev\DE_05_Scraping_Trustpilot\list_companies.txt"
        with open(path, "a") as f:
            f.write(f"{name}\n")
            f.write(f"{website}\n")
            f.write(f"{address}\n")
            f.write(f"{tag}\n")
            f.write(f"{rating}\n\n")

def parse_all_companies():
    pages = get_all_pages()
    for page in pages:
        parse_companies(url=page)
        print(f"scrapping en cours de {page}")

parse_all_companies()