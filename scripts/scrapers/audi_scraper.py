import requests
from bs4 import BeautifulSoup
import re
from scripts.config import AUDI_HTML, AUDI_TEXT, AUDI_IMG

def scrape_deals(url=None):
        
    if url is None:
        return []
        
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Save raw HTML
        with open(AUDI_HTML, 'w', encoding='utf-8') as f:
            f.write(response.text)
        
        tab_panes = soup.find_all('div', class_='tab-pane')
        
        deals = []
        for pane in tab_panes:
            content = pane.get_text(strip=True, separator=' ')
            deals.append(content)
            
        return deals
        
    except Exception as e:
        print(f"Error scraping deals from {url}: {e}")
        return []

def scrape_images(url=None):
        
    if url is None:
        return []
        
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        images = []
        tab_panes = soup.find_all('div', class_='tab-pane')
    
        for tab_pane in tab_panes:
            for img_tag in tab_pane.find_all('img'):
                img_url = img_tag.get('src')
                if img_url:
                    images.append(img_url)
            
        return images
        
    except Exception as e:
        print(f"Error scraping images from {url}: {e}")
        return []

if __name__ == "__main__":
    url = "https://www.audiprinceton.com/updated-lease-specials.htm"
    deals = scrape_deals(url)
    images = scrape_images(url)

    with open(AUDI_TEXT, 'w', encoding='utf-8') as f:
        for deal in deals:
            f.write(deal + '\n')
    
    with open(AUDI_IMG, 'w', encoding='utf-8') as f:
        for image in images:
            f.write(image + '\n')