import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as chromeService
driver = webdriver.Chrome(service=chromeService(ChromeDriverManager().install()))
driver.get('https://digikala.com')