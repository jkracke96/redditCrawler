from selenium import webdriver
from selenium.webdriver.common.by import By


def accept_cookies(driver):
    elements = driver.find_elements(By.TAG_NAME, "button")
    for element in elements:
        if element.text == "Alle akzeptieren":
            element.click()
            return True


def prepare_driver():
    # Set chromedriver options
    options = webdriver.ChromeOptions()
    options.add_argument("headless")
    options.add_argument("--window-size=2560,1440")
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    return driver
