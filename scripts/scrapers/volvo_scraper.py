import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urlunparse
from scripts.config import VOLVO_HTML, VOLVO_TEXT, VOLVO_IMG

def scrape_deals(url=None):
        
    if url is None:
        return []
        
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Save raw HTML
        with open(VOLVO_HTML, 'w', encoding='utf-8') as f:
            f.write(response.text)
        
        velocity = soup.find('div', id='velocity')
        
        models = ['XC40', 'XC60', 'XC90', 'V60', 'S60']
        model_ids = []
        for model in models:
            model_ids.extend([
                f'intro{model}',
                f'offer{model}', 
                f'disclosure{model}'
            ])
        
        model_groups = {}
        for model_id in model_ids:
            div = velocity.find('div', id=model_id)
            if div:
                model = next((m for m in models if m in model_id), None)
                if model not in model_groups:
                    model_groups[model] = []
                model_groups[model].append(div)
        
        deals = []
        for model_divs in model_groups.values():
            combined_text = ' '.join(
                ' '.join(div.get_text(strip=True, separator=' ').split())
                for div in model_divs
            )
            if combined_text:
                deals.append(combined_text)
            
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
        velocity_div = soup.find('div', id='velocity')  # Find the div with id='velocity'
    
        if velocity_div:
            # Find all <img> tags under the div
            for img_tag in velocity_div.find_all('img'):
                img_url = img_tag.get('src')
                if img_url:
                    cleaned_img_url = clean_image_url(img_url)
                    images.append(cleaned_img_url)
        else:
            print("No div with id 'velocity' found.")
        
        return images
    
    except Exception as e:
        print(f"Error scraping images from {url}: {e}")
        return []

def clean_image_url(raw_url):
    # Ensure the URL starts with "https://"
    if raw_url.startswith("//"):
        raw_url = "https:" + raw_url

    # Parse the URL and remove query parameters
    parsed_url = urlparse(raw_url)
    clean_url = urlunparse(parsed_url._replace(query=""))

    return clean_url

if __name__ == "__main__":
    url = "https://www.volvocarsprinceton.com/research/volvo-deals.htm"
    deals = scrape_deals(url)
    images = scrape_images(url)
    
    with open(VOLVO_TEXT, 'w', encoding='utf-8') as f:
        for deal in deals:
            f.write(deal + '\n')

    with open(VOLVO_IMG, 'w', encoding='utf-8') as f:
        for image in images:
            f.write(image + '\n')