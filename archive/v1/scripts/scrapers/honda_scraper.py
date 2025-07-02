from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urllib.parse import urlparse, urlunparse
from scripts.config import HONDA_TEXT, HONDA_IMG
import time

def scrape_deals(url=None):
    if url is None:
        return []
    
    # Set up WebDriver
    driver = webdriver.Chrome()  # Replace with `webdriver.Firefox()` if using Firefox

    try:
        # Load the webpage
        driver.get(url)

        # Wait for the dynamic content to load (adjust the timeout and element as needed)
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "promo"))
        )

        while True:
            try:
                # Wait for the "Load More" button to be clickable
                load_more_button = WebDriverWait(driver, 5).until(
                    EC.element_to_be_clickable((By.CLASS_NAME, "load-more"))
                )
                load_more_button.click()  # Click the button
                time.sleep(2)  # Small delay to let new content load
            except Exception:
                # Exit loop if "Load More" button is no longer present or clickable
                break

        # Extract dynamically loaded data (example)
        promo_elements = driver.find_elements(By.CLASS_NAME, "promo")
        
        deals = []
        for promo in promo_elements:
            # Find all button tags within each promo section
            try:
                button = promo.find_element(By.TAG_NAME, "button")
                
                # Scroll the button into view
                driver.execute_script("arguments[0].scrollIntoView();", button)
                time.sleep(1)  # Optional: wait for a moment
                
                # Use JavaScript to click the button
                driver.execute_script("arguments[0].click();", button)
                time.sleep(2)  # Allow time for the data to appear
                
                modal = driver.find_element(By.CLASS_NAME, "modal-content")
                time.sleep(1)
                modal_text = modal.text.replace("\n", " ")
                deals.append(modal_text)

                try:
                    close_button = WebDriverWait(driver, 5).until(
                        EC.element_to_be_clickable((By.CLASS_NAME, "ddc-icon-close"))
                    )
                    close_button.click()  # Close the additional data view
                    time.sleep(1)  # Allow time for the UI to reset
                except Exception as close_error:
                    print(f"Error closing popup: {close_error}")
            except Exception as e:
                print(e)
        
        return deals

    finally:
        driver.quit()  # Close the browser

def scrape_images(url=None):
    if url is None:
        return []
    
    # Set up WebDriver
    driver = webdriver.Chrome()  # Replace with `webdriver.Firefox()` if using Firefox

    try:
        # Load the webpage
        driver.get(url)

        # Wait for the dynamic content to load (adjust the timeout and element as needed)
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "promo"))
        )

        while True:
            try:
                # Wait for the "Load More" button to be clickable
                load_more_button = WebDriverWait(driver, 5).until(
                    EC.element_to_be_clickable((By.CLASS_NAME, "load-more"))
                )
                load_more_button.click()  # Click the button
                time.sleep(2)  # Small delay to let new content load
            except Exception:
                # Exit loop if "Load More" button is no longer present or clickable
                break

        # Extract dynamically loaded data (example)
        promo_elements = driver.find_elements(By.CLASS_NAME, "promo")
        
        images = []
        for promo in promo_elements:
            # Find all img tags within each promo section
            img_tags = promo.find_elements(By.TAG_NAME, "img")
            for img_tag in img_tags:
                # Extract the src attribute from each img tag
                img_url = img_tag.get_attribute("src")
                cleaned_img_url = clean_image_url(img_url)
                images.append(cleaned_img_url)
        
        return images

    finally:
        driver.quit()  # Close the browser

def clean_image_url(raw_url):
    # Ensure the URL starts with "https://"
    if raw_url.startswith("//"):
        raw_url = "https:" + raw_url

    # Parse the URL and remove query parameters
    parsed_url = urlparse(raw_url)
    clean_url = urlunparse(parsed_url._replace(query=""))

    return clean_url

if __name__ == "__main__":
    url = "https://www.princetonhonda.com/promotions/new/index.htm"
    deals = scrape_deals(url)
    images = scrape_images(url)
    
    with open(HONDA_TEXT, 'w', encoding='utf-8') as f:
        for deal in deals:
            f.write(deal + '\n')

    with open(HONDA_IMG, 'w', encoding='utf-8') as f:
        for image in images:
            f.write(image + '\n')