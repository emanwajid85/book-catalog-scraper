# Book Catalog Scraper

Scraped and cleaned a full 1000-book catalog from a live website using Python, BeautifulSoup, and pandas.

## What this project does
- Scrapes all 50 pages of a book catalog (title, price, rating, availability)
- Handles network errors gracefully without crashing
- Cleans and converts price/rating data into usable numeric formats
- Removes duplicates
- Generates filtered summary reports (top 10 most expensive books, all 5-star rated books)

## Tools used
Python, requests, BeautifulSoup, pandas

## Files
- `project2_scraper.py` — full scraping + cleaning script
- `all_books_cleaned.csv` — full cleaned dataset
- `top10_expensive_books.csv` — filtered summary
- `five_star_books.csv` — filtered summary
