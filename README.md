# social-crawler

## Installation 

```bash
# clone the repo
$ git clone https://github.com/oscarmmv/social-crawler.git

# change the working directory to social crawler
$ cd social-crawler
```
## Requirement

  - Project requires Google Chrome to be installed. (You can change to your perfered OS, please read [WebDriver Documentation](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&ved=2ahUKEwiK9Mr24duCAxWZCjQIHS3JDhgQFnoECBMQAQ&url=https%3A%2F%2Fwww.selenium.dev%2Fdocumentation%2Fwebdriver%2F&usg=AOvVaw1pVic_aa2kpShm2UAQOKH0&opi=89978449))
  - Supported Operating Systems:
    - WinX64
    - MacX64
    - LinuxX64
  * if you are using an unsupported OS, download the appropraite chromium drivers from https://chromedriver.chromium.org and set the driver path
```pyhton
  driver_path = "path-to-drivers/chromedriver-<your-operating-system>/chromedriver"
```

## Facebook Crawler
Import
```python
  # Install the required dependencies

```
```python
  # Import the scrape_facebook function into your Python script
  from facebook_scraper import scrape_facebook
```
Usage
```python
  data = scrape_facebook(url)
```
---
Return Type
The function returns a JSON object with the following structure:
```pyhton
data = {
  "Name": "user_name",
  "Status": "user_status",
  "Bio": "user_bio",
  "Followers": followers_count,
  "Likes": likes_count,
  "Email": "user_email",
  "Links": ["link_1", "link_2", ...]
}
```

## Instagram Crawler
Import
```python
  # Install the required dependencies

```
```python
  # Import the scrape_instagram_user function into your Python script
  from instagram_scraper import scrape_instagram_user
```
Usage
```python
  data = scrape_instagram_user(url)
```
---
Return Type
The function returns a JSON object with the following structure:
```pyhton
data = {
  "Name": "user_name",
  "Followers": followers_count,
  "Following": following_count,
  "Posts": post_count
}
```

## TikTok Crawler
##### Import
```python
  # Install the required dependencies

```
```python
  # Import the scrape_tiktok_profile function into your Python script
  from tiktok_scraper import scrape_tiktok_profile
```
Usage
```python
  data = scrape_tiktok_profile(url)
```
---
Return Type
The function returns a JSON object with the following structure:
```pyhton
data = {
  "Name": "name",
  "Username": "user_name",
  "Bio": "user_bio",
  "Link": link,
  "Followers": follower_count,
  "Following": following_count,
  "Like_Count": like_count
}
```

## Twitter Crawler
Import
```python
  # Install the required dependencies

```
```python
  # Import the scrape_twitter_profile function into your Python script
  from twitter_scraper import scrape_twitter_profile
```
Usage
```python
  data = scrape_twitter_profile(url)
```
---
Return Type
The function returns a JSON object with the following structure:
```pyhton
data = {
  "Name": "name",
  "Bio": "user_bio",
  "Followers": follower_count,
  "Following": following_count,
  "Account Age": account_age,
  "Link": link,
}
```







