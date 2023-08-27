from selenium.webdriver.common.by import By
import json
from selenium import webdriver
from selenium.common.exceptions import WebDriverException, StaleElementReferenceException
from gtts import gTTS


def screenshot_comments(comment_driver, link, post_counter):
    comment_driver.get(link)
    # Get all <div> elements and look for items with data_testid="post-container"
    comment_elements = comment_driver.find_elements(By.TAG_NAME, "shreddit-comment")
    comment_counter = 0
    for comment_element in comment_elements:
        # skip for first comment as it's a user statistic
        if comment_counter == 0:
            comment_counter += 1
            continue
        try:
            thing_id = comment_element.get_attribute("thingid")
            parent_id = comment_element.get_attribute("parentid")
        except StaleElementReferenceException:
            print("--------- get_attribute() failed")
        if len(thing_id) == 10 and parent_id is None:
            try:
                comment_element.screenshot(f"screenshots/comments/post_{post_counter}_comment_{comment_counter}.png", )
                extract_text(comment_element, "comment", post_counter, comment_counter)
                comment_counter += 1
            except WebDriverException:
                print("------------ This element is not visible")
        if comment_counter == 3:
            print(f"{comment_counter} comments were extracted")
            break


def go_to_comments(element):
    children = element.find_elements(By.TAG_NAME, "a")
    for child in children:
        comments_link = child.get_attribute("href")
        if comments_link is None:
            return None
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
    #options.add_argument("--window-size=1920,1080")
    options.add_argument("--window-size=3840,2160")
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    return driver


def text_to_speech(text, key):
    try:
        # Create a Google text to speech object
        tts = gTTS(text, lang="en-uk")
    except Exception as e:
        print(e)
        print(f"Text for {key} could not be converted to audio: {text}")
        tts = gTTS("haha")

    # Save the generated speech as an audio file
    tts.save(f"audio/{key}.mp3")


def extract_text(element, content_type, post_counter, comment_counter=None):
    # define html tag that contains the comment text
    if "post_top" in content_type:
        elements = element.find_elements(By.TAG_NAME, "div")
        for element in elements:
            if "post-title" in element.get_attribute("id"):
                elements = [element]
                break
    elif "post" in content_type:
        elements = element.find_elements(By.TAG_NAME, "h3")
    else:
        elements = element.find_elements(By.TAG_NAME, "p")

    for elem in elements:
        text = elem.text
        if text == "":
            continue
        # if it is the first post, clear the existing json. Otherwise, load the existing content from json
        if "post" in content_type and post_counter == 0:
            data = dict()
        else:
            with open("screenshots/texts.json", "r") as f:
                data = json.load(f)

        # write post/comment text to dict
        if "post" in content_type:
            key = f"post_{post_counter}"
            data[key] = text
        else:
            key = f"post_{post_counter}_comment_{comment_counter}"
            data[key] = text

        text_to_speech(text, key)

        with open("screenshots/texts.json", "w") as f:
            json.dump(data, f)
        break


