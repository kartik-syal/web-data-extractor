# Web Data Extractor

Web crawler using Scrapy to extract URLs and titles from a website, and then use BeautifulSoup to scrape text data from those URLs.

## Setup Instructions

1. **Clone the Repository:**
   ```
   git clone https://github.com/kartik-syal/web-data-extractor.git
   cd your-repo/
   ```

2. **Install Dependencies:**
   ```
   pip install scrapy beautifulsoup4
   ```

3. **Run the Scrapy Spider:**
   ```
   scrapy runspider webcrawler/spiders/urls_spider.py
   ```

   This will generate `urls.csv` containing URLs and titles extracted from the website.

4. **Scrape Text Data using BeautifulSoup:**
   ```
   python scrape_data.py
   ```

   This will scrape text data from the URLs in `urls.csv` and store it in `scraped_data.csv`.

## Files and Directories

- `webcrawler/spiders/urls_spider.py`: Scrapy spider for crawling URLs and titles.
- `scrape_data.py`: Script to scrape text data from URLs using BeautifulSoup.
- `README.md`: This file containing setup instructions and project details.
- `.gitignore`: File specifying which files and directories to ignore in Git.

## Notes

- Adjust `allowed_domains` and `start_urls` in `urls_spider.py` for your target website.
- Customize `scrape_additional_data` function in `scrape_data.py` for specific data extraction needs.