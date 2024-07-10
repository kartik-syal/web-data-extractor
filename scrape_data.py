import csv
import requests
from bs4 import BeautifulSoup

input_csv = 'urls.csv'
output_csv = 'scraped_data.csv'

def scrape_all_text(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad status codes
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Extract all text within the <body> tag
        body = soup.find('body')
        return body.get_text(separator=' ', strip=True) if body else 'N/A'
    except requests.RequestException as e:
        return f"Error: {e}"

with open(input_csv, newline='') as infile, open(output_csv, mode='w', newline='') as outfile:
    reader = csv.DictReader(infile)
    fieldnames = reader.fieldnames + ['data']
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    writer.writeheader()

    for row in reader:
        row['data'] = scrape_all_text(row['url'])
        writer.writerow(row)
