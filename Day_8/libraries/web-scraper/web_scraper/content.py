class ContentScraper:
    def __init__(self, url: str):
        self.url = url
        self.soup = None
        from bs4 import BeautifulSoup
        self.bs4 = BeautifulSoup
        self.html = None

    def fetch_content(self):
        import requests
        response: object = requests.get(self.url)
        if response.status_code == 200:
            self.html = response.text
        else:
            raise Exception(f"Failed to fetch content from {self.url}")

    def parse_content(self):
        soup: self.bs4 = self.bs4(self.html, 'html.parser')
        self.soup = soup
    
    def get_formated_html(self):
        return self.soup.prettify()
    
    def get_clean_text(self):
        data = self.soup.text
        data = '\n'.join(filter(lambda x: x!= '', data.split('\n')))
        return data