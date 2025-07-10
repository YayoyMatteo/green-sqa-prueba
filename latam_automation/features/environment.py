from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def before_all(context):
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")  # No headless, visible
    context.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

def after_all(context):
    context.driver.quit()
