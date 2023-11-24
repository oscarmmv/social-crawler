import platform
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import json

def scrape_facebook(url):
    system = platform.system()
    if system == 'Linux':
        driver_path = 'chromium_drivers/chromedriver-linux-x64/chromedriver'
    elif system == 'Darwin':
        driver_path = 'chromium_drivers/chromedriver-mac-x64/chromedriver'
    elif system == 'Windows':
        driver_path = 'chromium_drivers/chromedriver-win-x64/chromedriver'
    else:
        raise Exception('Unsupported operating system')
    
    chrome_options = Options()
    chrome_options.add_argument('--headless')  

    service = Service(driver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)

    driver.get(url)

    while True:
        try:
            button = driver.find_element(By.CSS_SELECTOR, '.x92rtbv > div:nth-child(1)')
            button.click()
            break
        except:
            continue
    while True:
        try:
            name_elements = driver.find_element(By.CSS_SELECTOR, 'h1.x1heor9g')
            like_count_elements = driver.find_elements(By.CSS_SELECTOR, 'div.x1cy8zhl:nth-child(2) > span:nth-child(1) > a:nth-child(1)')
            follower_count_elements = driver.find_elements(By.CSS_SELECTOR, 'a.xt0psk2:nth-child(2)')
            bio_desc_elements = driver.find_elements(By.CSS_SELECTOR, '.xieb3on > div:nth-child(1)')
            page_desc_elements = driver.find_elements(By.CSS_SELECTOR, '.xieb3on > div:nth-child(2) > div:nth-child(1) > ul:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > span:nth-child(1) > div:nth-child(1) > span:nth-child(1)')
            email_desc_elements = driver.find_elements(By.CSS_SELECTOR, 'div.x1nhvcw1:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > span:nth-child(1)')

            links_elements = [
                driver.find_elements(By.CSS_SELECTOR, 'div.x1nhvcw1:nth-child(3) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > span:nth-child(1) > a:nth-child(1)'),
                driver.find_elements(By.CSS_SELECTOR, 'div.x1nhvcw1:nth-child(4) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > span:nth-child(1) > a:nth-child(1)'),
                driver.find_elements(By.CSS_SELECTOR, 'div.x1ja2u2z:nth-child(5) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > span:nth-child(1) > a:nth-child(1)'),
                driver.find_elements(By.CSS_SELECTOR, 'div.x9f619:nth-child(6)'),
                driver.find_elements(By.CSS_SELECTOR, 'div.x9f619:nth-child(6) > div:nth-child(2) > div:nth-child(1) > a:nth-child(1) > div:nth-child(1) > div:nth-child(1) > span:nth-child(1)')
            ]

            name = name_elements.text if name_elements else None
            like_count = like_count_elements[0].text if like_count_elements else None
            follower_count = follower_count_elements[0].text if follower_count_elements else None
            bio_desc = bio_desc_elements[0].text if bio_desc_elements else None
            page_desc = page_desc_elements[0].text if page_desc_elements else None
            email_desc = email_desc_elements[0].text if email_desc_elements else None
            link_texts = [element[0].get_attribute("href") if element and element[0].get_attribute("href") else element[0].text if element and element[0].text else None for element in links_elements]
            link_texts = list(set(link_texts)) # Remove duplicates from link_texts

            break
        except:
            continue

    data = {
        "Name": name,
        "Status": page_desc,
        "Bio": bio_desc,
        "Followers": follower_count,
        "Likes": like_count,
        "Email": email_desc,
        "Links": {f"link{i+1}": link_text for i, link_text in enumerate(link_texts) if link_text is not None}
    }

    driver.quit()

    return json.dumps(data, indent=4)


