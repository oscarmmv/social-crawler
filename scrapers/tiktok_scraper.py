from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from helium import *
import time
import platform
import json

class TikTokSpider:
    def scrape_tiktok_profile(self, url):
        # Determine the operating system
        system = platform.system()

        # Set the driver path based on the operating system
        if system == 'Linux':
            driver_path = 'chromium_drivers/chromedriver-linux-x64/chromedriver'
        elif system == 'Darwin':
            driver_path = 'chromium_drivers/chromedriver-mac-x64/chromedriver'
        elif system == 'Windows':
            driver_path = 'chromium_drivers/chromedriver-win-x64/chromedriver'
        else:
            raise Exception('Unsupported operating system')
        
        chrome_options = Options()
        chrome_options.add_argument("--incognito")  # Start browser in incognito mode
        chrome_options.add_argument("--headless")  # Run browser in headless mode
        
        driver = webdriver.Chrome(executable_path=driver_path, options=chrome_options)
        set_driver(driver)
        go_to(url)
        
        # Bypass security check if the #Path element exists
        if S('#Path').exists():
            click(S('#Path'))
            time.sleep(0.1)  # Wait for a moment after clicking the button
        
        name_elements = find_all(S('.css-1xo9k5n-H1ShareTitle'))
        username_elements = find_all(S('.css-10pb43i-H2ShareSubTitle'))
        follower_elements = find_all(S('div.css-mgke3u-DivNumber:nth-child(1) > strong:nth-child(1)'))
        following_elements = find_all(S('div.css-mgke3u-DivNumber:nth-child(2) > strong:nth-child(1)'))
        like_elements = find_all(S('.css-ntsum2-DivNumber > strong:nth-child(1)'))
        bio_elements = find_all(S('.css-4ac4gk-H2ShareDesc'))
        link_elements = find_all(S('.css-847r2g-SpanLink'))

        name = name_elements[0].web_element.text if name_elements else None
        username = username_elements[0].web_element.text if username_elements else None
        follower_count = follower_elements[0].web_element.text if follower_elements else None
        following_count = following_elements[0].web_element.text if following_elements else None
        like_count = like_elements[0].web_element.text if like_elements else None
        bio_desc = bio_elements[0].web_element.text if bio_elements else None
        link_desc = link_elements[0].web_element.text if link_elements else None

        data = {
            "Name": name,
            "Username": username,
            "Bio": bio_desc,
            "Link": link_desc,
            "Followers": follower_count,
            "Following": following_count,
            "Like_Count": like_count
        }

        return json.dumps(data, indent=4)

