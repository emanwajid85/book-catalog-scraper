import requests
from bs4 import BeautifulSoup
import pandas as pd

all_books_data = []

for page_num in range(1, 51):
    url = f"https://books.toscrape.com/catalogue/page-{page_num}.html"
    
    try:
        response = requests.get(url, timeout=10)
    except requests.exceptions.RequestException as e:
        print(f"Page {page_num} failed, skipping. Error: {e}")
        continue
    
    soup = BeautifulSoup(response.text, "html.parser")
    books = soup.find_all("article", class_="product_pod")
    
    for book in books:
        title = book.h3.a["title"]
        price = book.find("p", class_="price_color").text
        rating = book.find("p", class_="star-rating")["class"][1]
        availability = book.find("p", class_="instock availability").text.strip()
        
        all_books_data.append({
            "Title": title,
            "Price": price,
            "Rating": rating,
            "Availability": availability
        })
    
    print(f"Page {page_num}/50 done")
    
df = pd.DataFrame(all_books_data)
print(f"Total books scraped: {len(df)}")
df["Price"] = df["Price"].str.replace(r"[^\d.]", "", regex=True).astype(float)

rating_map = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}
df["Rating"] = df["Rating"].map(rating_map)

df = df.drop_duplicates()

print(df.head())
print(df.info())
print("Average price:", df["Price"].mean())
print("Average rating:", df["Rating"].mean())

top10_expensive = df.sort_values("Price", ascending=False).head(10)
print(top10_expensive)

five_star_books = df[df["Rating"] == 5]
print(f"Number of 5-star books: {len(five_star_books)}")
df.to_csv("all_books_cleaned.csv", index=False)
top10_expensive.to_csv("top10_expensive_books.csv", index=False)
five_star_books.to_csv("five_star_books.csv", index=False)

print("All files saved!")