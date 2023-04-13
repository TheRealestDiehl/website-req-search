from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

def test_python_search():
    browser = webdriver.Chrome()
    try:
        browser.get("https://www.amazon.com")