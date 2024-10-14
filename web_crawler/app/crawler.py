import requests
from bs4 import BeautifulSoup

def crawl(url, depth):
    crawled_links = []

    def scrape(url, depth):
        if depth == 0:
            return
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            for link in soup.find_all('a', href=True):
                link_url = link['href']
                if link_url.startswith('http'):
                    crawled_links.append(link_url)
                    scrape(link_url, depth - 1)
        except Exception as e:
            print(f"Error crawling {url}: {e}")

    scrape(url, depth)
    return crawled_links
