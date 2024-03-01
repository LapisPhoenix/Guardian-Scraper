# Guardian: Web Scraping and Article Extraction

The `Guardian` class is a Python utility for fetching HTML content from a given URL and extracting cleaned article text. It uses Selenium for web scraping and BeautifulSoup for parsing the HTML. Whether you're building a news aggregator, content analysis tool, or simply want to extract article text, this class can be a helpful addition to your project.

## Installation

1. Make sure you have Python 3.x installed.
2. Install the required packages using pip:

    ```bash
    pip install -r requirements.txt
    ```

3. Download the [geckodriver](https://github.com/mozilla/geckodriver/releases) (Firefox WebDriver) and add its location to your system PATH.

## Usage

```python
from guardian import Guardian

# Create an instance of the Guardian class
guardian = Guardian()

# Example usage: Get article content from a URL
article_url = "https://www.theguardian.com/technology/2024/feb/29/former-crypto-director-banned-from-leaving-australia-after-blockchain-global-collapsed-owing-58m"
article_text = guardian.get(article_url)

if article_text:
    print("Article content:")
    print(article_text)
else:
    print("Error fetching article content. Please check the URL or try again later.")
```

## Methods

### `get(url: str) -> str`

Retrieves the cleaned article text from a given URL.

- Args:
    - `url` (str): The URL of the article.

- Returns:
    - `str`: The cleaned article text.

## Error Handling

The `Guardian` class includes error handling for scenarios such as connection issues, missing article content, or invalid URLs. If an error occurs during fetching or parsing, appropriate error messages are returned.
