from selenium import webdriver
from selenium.webdriver.common.by import By
import json


def accept_cookies(driver):
    elements = driver.find_elements(By.TAG_NAME, "button")
    for element in elements:
        if element.text == "Alle akzeptieren":
            element.click()
            return True


def prepare_driver():
    # Set chromedriver options
    options = webdriver.ChromeOptions()
    options.add_argument("headless")   # headless = do not show browser window
    options.add_argument("--window-size=2560,1440")
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    return driver


def extract_text(element, content_type, post_counter, comment_counter=None):
    # define html tag that contains the comment text
    if "post" in content_type:
        elements = element.find_elements(By.TAG_NAME, "h3")
    else:
        elements = element.find_elements(By.TAG_NAME, "p")

    for elem in elements:
        text = elem.text
        # if it is the first post, clear the existing json. Otherwise, load the existing content from json
        if "post" in content_type and post_counter == 0:
            data = dict()
        else:
            with open("screenshots/texts.json", "r") as f:
                data = json.load(f)

        # write post/comment text to dict
        if "post" in content_type:
            data[f"post_{post_counter}"] = text
        else:
            data[f"post_{post_counter}_comment_{comment_counter}"] = text

        with open("screenshots/texts.json", "w") as f:
            json.dump(data, f)


