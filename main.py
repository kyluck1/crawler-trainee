import requests
from bs4 import BeautifulSoup
import pandas as pd
import json
import time
import os

os.makedirs("output", exist_ok=True)

URL = "https://books.toscrape.com/"

headers = {
    "User-Agent": "FernandoCrawlerBot/1.0"
}

response = requests.get(URL, headers=headers)
response.encoding = "utf-8"

soup = BeautifulSoup(response.text, "html.parser")

books = []

rating_map = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5
}

articles = soup.find_all("article", class_="product_pod")

for article in articles:

    title = article.h3.a["title"]

    price = article.find("p", class_="price_color").text

    availability = article.find("p", class_="instock availability").text.strip()

    rating_class = article.find("p", class_="star-rating")["class"][1]

    rating = rating_map.get(rating_class, 0)

    books.append({
        "title": title,
        "price": price,
        "availability": availability,
        "rating": rating
    })

time.sleep(1)

# salvar JSON
with open("output/books.json", "w", encoding="utf-8") as f:
    json.dump(books, f, indent=4, ensure_ascii=False)

# salvar CSV
df = pd.DataFrame(books)
df.to_csv("output/books.csv", index=False)

print("Scraping finalizado!")