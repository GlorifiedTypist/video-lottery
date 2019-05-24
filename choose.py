#!/usr/bin/python
import random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions

def connectChrome():
    options = ChromeOptions()
    options.add_argument("--headless")
    chromeDriverPath = "/usr/local/bin/chromedriver"
    driver = webdriver.Chrome(chromeDriverPath, chrome_options=options)
    print("Chrome Headless Browser Invoked - Friday Video Lottery v0.1b")
    return driver

def main():
    driver = connectChrome()
    driver.get("https://www.youtube.com/channel/UCvqbFHwN-nwalWPjPUKpvTA/videos?view=0&sort=dd&shelf_id=1")
    results = driver.find_elements_by_id('video-title')

    length = len(results) 
    winner = random.randint(0, length)

    for i in range(length): 

        if i == winner:
            print("Today's winner is lucky number %d, %s - %s") % (winner, results[i].text, results[i].get_attribute('href'))

    driver.quit()

main()