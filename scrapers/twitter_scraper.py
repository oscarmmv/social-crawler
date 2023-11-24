from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import platform
import json

def scrape_twitter_profile(url):
    system = platform.system()
    if system == 'Linux':
        driver_path = 'chromium_drivers/chromedriver-linux-x64/chromedriver'
    elif system == 'Darwin':
        driver_path = 'chromium_drivers/chromedriver-mac-x64/chromedriver'
    elif system == 'Windows':
        driver_path = 'chromium_drivers/chromedriver-win-x64/chromedriver'
    else:
        raise Exception('Unsupported operating system')
    
    options = Options()
    options.add_argument('--headless')  
    
    service = Service(driver_path)
    driver = webdriver.Chrome(service=service, options=options)

    driver.get(url)

    # Input your username and password here
    username = 'example123'
    password = '123456789'

    input_elements = driver.find_elements(By.TAG_NAME, "input")

    # Loop until the username field is found
    while True:
        try:
            input_elements = driver.find_elements(By.TAG_NAME, "input")
            username_field = input_elements[0]  # Assign the first input element to username_field
            print(username_field)
            username_field.send_keys(username)
            username_field.send_keys(Keys.RETURN)
            break  # If the element is found and no exception is thrown, break the loop
        except:
            continue

    # Loop until the password field is found
    while True:
        try:
            input_elements = driver.find_elements(By.TAG_NAME, "input")
            password_field = input_elements[1]  # Assign the second input element to password_field
            password_field.send_keys(password)
            password_field.send_keys(Keys.RETURN)
            break  # If the element is found and no exception is thrown, break the loop
        except:
            continue

    while True:
        try: 
            following_count_elements = driver.find_elements(By.CSS_SELECTOR, '.r-1mf7evn > a:nth-child(1) > span:nth-child(1) > span:nth-child(1)')
            follower_count_elements = driver.find_element(By.CSS_SELECTOR, 'div.r-13awgt0:nth-child(5) > div:nth-child(2) > a:nth-child(1) > span:nth-child(1) > span:nth-child(1)')
            location_desc_elements = driver.find_elements(By.CSS_SELECTOR, 'span.r-4qtqp9:nth-child(1) > span:nth-child(2) > span:nth-child(1)')
            account_age_elements = driver.find_elements(By.CSS_SELECTOR, 'span.r-4qtqp9:nth-child(2) > span:nth-child(2)')
            bio_desc_elements = driver.find_elements(By.CSS_SELECTOR, 'div.r-6gpygo:nth-child(3) > div:nth-child(1) > div:nth-child(1)')
            link_elements = driver.find_elements(By.CSS_SELECTOR, 'a.r-4qtqp9 > span:nth-child(2)')
            name_elements = driver.find_elements(By.CSS_SELECTOR, 'div.r-adyw6z:nth-child(1) > span:nth-child(1) > span:nth-child(1)')

            following_count = following_count_elements[0].text if following_count_elements else None
            follower_count = follower_count_elements.text if follower_count_elements else None
            location_desc = location_desc_elements[0].text if location_desc_elements else None
            account_age = account_age_elements[0].text if account_age_elements else None
            bio_desc = bio_desc_elements[0].text if bio_desc_elements else None
            link = link_elements[0].text if link_elements else None
            name = name_elements[0].text if name_elements else None

            break  
        except:
            time.sleep(1)  

    data = {
        "Name": name,
        "Bio": bio_desc,
        "Followers": follower_count,
        "Following": following_count,
        "Location": location_desc,
        "Account Age": account_age,
        "Link": link
    }

    return json.dumps(data, indent=4)


