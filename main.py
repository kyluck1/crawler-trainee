import requests
from bs4 import BeautifulSoup
import pandas as pd
import json
import time
import os

URL = "https://books.toscrape.com/"

HEADERS = {
    "User-Agent": "FernandoCrawlerBot/1.0"
}

RATING_MAP = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5
}


def fetch_page():
    response = requests.get(URL, headers=HEADERS)
    response.encoding = "utf-8"
    return response.text


def parse_books(html):
    soup = BeautifulSoup(html, "html.parser")

    books = []

    articles = soup.find_all("article", class_="product_pod")

    for article in articles:

        title = article.h3.a["title"]

        price = article.find("p", class_="price_color").text

        availability = article.find(
            "p",
            class_="instock availability"
        ).text.strip()

        rating_class = article.find(
            "p",
            class_="star-rating"
        )["class"][1]

        rating = RATING_MAP.get(rating_class, 0)

        books.append({
            "title": title,
            "price": price,
            "availability": availability,
            "rating": rating
        })

    return books


def save_json(data):
    with open("output/books.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


def save_csv(data):
    df = pd.DataFrame(data)
    df.to_csv("output/books.csv", index=False)


def main():

    os.makedirs("output", exist_ok=True)

    html = fetch_page()

    books = parse_books(html)

    save_json(books)

    save_csv(books)

    time.sleep(1)

    print("Scraping finalizado!")


if __name__ == "__main__":
    main()