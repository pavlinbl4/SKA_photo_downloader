import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from struct import error


class ChromeDriver:
    def __init__(self, url):
        self.user_data_dir = "/tmp/chrome-user-data"
        self.service = Service(ChromeDriverManager().install())
        self.url = url
        self.create_user_dir()  # Создаем директорию для пользовательских данных
        self.driver = webdriver.Chrome(service=self.service, options=self.setting_chrome_options())


    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.driver.quit()  # Закрываем браузер при выходе из контекста

    def create_user_dir(self):
        os.makedirs(self.user_data_dir, exist_ok=True)

    def setting_chrome_options(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument(f"--user-data-dir={self.user_data_dir}")
        return chrome_options  # Возвращаем объект Options

    def driver_get(self):
        return self.driver.get(self.url)  # Просто открываем URL, ничего не возвращаем

    def get_page_title(self):
        return self.driver.title  # Возвращаем заголовок страницы

    def find_elements_locator(self,locator,  element):
        try:
            return self.driver.find_elements(locator, element)
        except error:
            return error(error)

    def find_one_element_locator(self, locator,  element):
        try:
            return self.driver.find_element(locator, element)
        except error:
            return error(error)



