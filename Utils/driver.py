from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import os

def get_driver():

    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    path = os.path.join(base_dir, "ChromeDriver", "chromedriver.exe")

    service = Service(path)
    driver = webdriver.Chrome(service=service)

    driver.maximize_window()
    return driver