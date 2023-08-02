from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException, StaleElementReferenceException
import os
from functions import accept_cookies, prepare_driver, extract_text, screenshot_comments, go_to_comments


def run(driver, comments_driver):
    # Get all <div> elements and look for items with data_testid="post-container"
    elements = driver.find_elements(By.TAG_NAME, "div")
    counter = 0
    for element in elements:
        try:
            data_testid = element.get_attribute("data-testid")
        except StaleElementReferenceException:
            print("--------- get_attribute() failed")

        # find post-container from data-testid's
        if "post-container" == data_testid:
            try:
                element.screenshot(f"screenshots/posts/post_{counter}.png")
                extract_text(element, "post", counter)
                comments_link = go_to_comments(element)
                if comments_link is None:
                    counter += 1
                    continue
                comments_driver.switch_to.window(comments_driver.current_window_handle)
                screenshot_comments(comments_driver, comments_link, counter)
                driver.switch_to.window(driver.current_window_handle)
                counter += 1
            except WebDriverException:
                print("------------ This element is not visible")


if __name__ == "__main__":
    # Delete existing screenshots
    screenshot_path = "screenshots"
    audio_path = "audio"
    sub_paths = ["posts", "comments"]
    for sub_path in sub_paths:
        dir_path = f"{screenshot_path}/{sub_path}"
        files = os.listdir(dir_path)
        for file in files:
            if "init" not in file:
                os.remove(f"{dir_path}/{file}")

    files = os.listdir(audio_path)
    for file in files:
        if "init" not in file:
            os.remove(f"{audio_path}/{file}")

    # Set chromedriver options
    driver = prepare_driver()
    comments_driver = prepare_driver()

    # Point driver to URL
    driver.get("https://www.reddit.com/r/wallstreetbets/hot/")

    # Accept cookies
    accept_cookies(driver)

    run(driver, comments_driver)
