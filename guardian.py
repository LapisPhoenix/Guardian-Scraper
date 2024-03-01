from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup
from selenium.common.exceptions import WebDriverException, TimeoutException


class Guardian:
    def __init__(self):
        self.max_retries = 3

    @staticmethod
    def _fetch_html(url: str) -> str:
        """
        Fetches the HTML content of a given URL using a headless Firefox browser.

        Args:
            url (str): The URL to fetch.

        Returns:
            str: The HTML content.
        """
        options = Options()
        options.add_argument("-headless")
        driver = webdriver.Firefox(options=options)

        try:
            driver.get(url)
            driver.implicitly_wait(1)
            html_content = driver.page_source
        except (WebDriverException, TimeoutException) as e:
            print(f"Error fetching HTML from {url}: {e}")
            html_content = ""

        driver.quit()

        return html_content

    def get(self, url: str) -> str:
        """
        Retrieves the article content from a given URL.

        Args:
            url (str): The URL of the article.

        Returns:
            str: The cleaned article text.
        """
        retries = 0
        while retries < self.max_retries:
            html = self._fetch_html(url)
            if html:
                break
            retries += 1

        if not html:
            return "Error fetching article content. Please check the URL or try again later."

        soup = BeautifulSoup(html, 'lxml')
        article_content = soup.select(".article-body-commercial-selector.article-body-viewer-selector.dcr-1g5o3j6")
        if not article_content:
            return "Article content not found. Please verify the URL or try another source."

        article_content = article_content[0]
        cleaned_article = BeautifulSoup(article_content.prettify(), 'lxml')

        # Extract text from <p> tags (actual article content)
        article_text = ""
        for paragraph_tag in cleaned_article.find_all('p', class_="dcr-4cudl2"):
            paragraph_text = ' '.join(paragraph_tag.stripped_strings)
            article_text += paragraph_text + "\n\n"

        return article_text
