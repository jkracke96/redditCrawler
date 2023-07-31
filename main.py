from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException, StaleElementReferenceException
import os
from functions import accept_cookies, prepare_driver, extract_text


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


# Delete existing screenshots
screenshot_path = "screenshots"
sub_paths = ["posts", "comments"]
for sub_path in sub_paths:
    dir_path = f"{screenshot_path}/{sub_path}"
    files = os.listdir(dir_path)
    for file in files:
        if "init" not in file:
            os.remove(f"{dir_path}/{file}")

# Set chromedriver options
driver = prepare_driver()
comments_driver = prepare_driver()

# Point driver to URL
driver.get("https://www.reddit.com/r/wallstreetbets/hot/")

# Accept cookies
accept_cookies(driver)


def func1(driver, comments_driver):
    # Get all <div> elements and look for items with data_testid="post-container"
    elements = driver.find_elements(By.TAG_NAME, "div")
    counter = 0
    for element in elements:
        try:
            data_testid = element.get_attribute("data-testid")
        except StaleElementReferenceException:
            print("--------- get_attribute() failed")
        if "post-container" == data_testid:
            try:
                element.screenshot(f"screenshots/posts/post_{counter}.png")
                extract_text(element, "post", counter)
                comments_link = go_to_comments(element)
                comments_driver.switch_to.window(comments_driver.current_window_handle)
                screenshot_comments(comments_driver, comments_link, counter)
                driver.switch_to.window(driver.current_window_handle)
                counter += 1
            except WebDriverException:
                print("------------ This element is not visible")


func1(driver, comments_driver)
