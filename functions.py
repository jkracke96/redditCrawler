from selenium.webdriver.common.by import By
import json
from selenium import webdriver
from selenium.common.exceptions import WebDriverException, StaleElementReferenceException


def screenshot_comments(comment_driver, link, post_counter):
    comment_driver.get(link)
    # Get all <div> elements and look for items with data_testid="post-container"
    comment_elements = comment_driver.find_elements(By.TAG_NAME, "shreddit-comment")
    comment_counter = 0
    for comment_element in comment_elements:
        try:
            thing_id = comment_element.get_attribute("thingid")
            parent_id = comment_element.get_attribute("parentid")
        except StaleElementReferenceException:
            print("--------- get_attribute() failed")
        if len(thing_id) == 10 and parent_id is None:
            try:
                comment_element.screenshot(f"screenshots/comments/post_{post_counter}_comment{comment_counter}.png", )
                extract_text(comment_element, "comment", post_counter, comment_counter)
                comment_counter += 1
            except WebDriverException:
                print("------------ This element is not visible")
        if comment_counter == 5:
            print(f"{comment_counter} comments were extracted")
            break


def go_to_comments(element):
    children = element.find_elements(By.TAG_NAME, "a")
    for child in children:
        comments_link = child.get_attribute("href")
        if "comments" in comments_link:
            return comments_link


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


