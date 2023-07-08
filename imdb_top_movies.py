# import requests
# from bs4 import BeautifulSoup
# url = "http://quotes.toscrape.com"
# response = requests.get(url)

# if response.status_code == 200:
#     html_content = response.text
# else:
#     print("Failed to fetch the web page:", response.status_code)
# soup = BeautifulSoup(html_content, "html.parser")

# # Extract quotes
# quote_divs = soup.find_all("div", class_="quote")

# for quote_div in quote_divs:
#     text = quote_div.find("span", class_="text").text
#     author = quote_div.find("small", class_="author").text
#     print(text)
#     print(f"- {author}")
#     print()

import requests
from bs4 import BeautifulSoup

def fetch_quotes():
    url = "http://quotes.toscrape.com"
    response = requests.get(url)

    if response.status_code == 200:
        html_content = response.text
    else:
        print("Failed to fetch the web page:", response.status_code)
        return []

    soup = BeautifulSoup(html_content, "html.parser")

    # Extract quotes
    quote_divs = soup.find_all("div", class_="quote")

    quotes = []
    for quote_div in quote_divs:
        text = quote_div.find("span", class_="text").text
        author = quote_div.find("small", class_="author").text
        quotes.append({"text": text, "author": author})

    return quotes
