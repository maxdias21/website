from pathlib import Path

from selenium.webdriver.chrome.service import Service
from selenium import webdriver

ROOT_PATH = Path(__file__).parent.parent.parent.parent
CHROMEDRIVER_NAME = 'chromedriver.exe'
CHROMEDRIVER_PATH = ROOT_PATH / 'utils/tests/selenium/chromedriver' / CHROMEDRIVER_NAME

def make_chrome_driver(*options):
    chrome_options = webdriver.ChromeOptions()

    if not options:
        for option in options:
            chrome_options.add_argument(option)

    chrome_service = Service(executable_path=str(CHROMEDRIVER_PATH))
    browser = webdriver.Chrome(service=chrome_service, options=chrome_options)

    return browser
