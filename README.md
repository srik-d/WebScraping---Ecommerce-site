# E-Commerce Scraping Project

This project is designed to scrape product information from the e-commerce site at [webscraper.io]mainly to get information about all the laptops present (https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops) using Python. The script fetches, parses, and extracts data such as product name, price, description, and ratings, then saves this data into a CSV file.

## Features

- **HTTP Requests**: Utilizes the `requests` library to fetch HTML content from the specified URL.
- **HTML Parsing**: Leverages `BeautifulSoup` with the `lxml` parser for efficient HTML parsing.
- **Data Extraction**: Extracts product details including name, price, description, and ratings.
- **CSV Output**: Saves the extracted data into a CSV file with a timestamped filename.

## Requirements

- Python 3.7+
- `requests`
- `beautifulsoup4`
- `lxml`

## Installation

1. Clone the repository or download the script file.
2. Navigate to the project directory.
3. Install the required Python packages:
   ```sh
   pip install -r requirements.txt
   ```

## Usage

Execute the script to start scraping the e-commerce site and saving the data to a CSV file(data_(date)):

```sh
python scraper.py
```

## Files

- **scraper.py**: The main script for scraping and saving data.
- **requirements.txt**: Lists the required Python packages.

---

