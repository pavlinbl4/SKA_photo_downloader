from pathlib import Path

from selenium.webdriver.chrome.options import Options


def download_folder(path_to_download_folder=f'{Path.home()}/Downloads'):
    preferences = {
        "download.default_directory": path_to_download_folder
    }
    return preferences


def setting_chrome_options():
    preferences = download_folder()
    chrome_options = Options()
    chrome_options.add_experimental_option("prefs", preferences)
    # chrome_options.add_argument("webdriver.chrome.driver=chromedriver")
    # chrome_options.add_experimental_option('detach', True)
    chrome_options.add_argument("--headless")  # фоновый режим
    chrome_options.add_argument("--ignore-certificate-errors")  # игнорирует ошибки сертификата SSL
    # chrome_options.add_argument("--disable-cache")  # отключает кэширование в браузере
    # chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--window-size=1280,800")
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")  # невидимость автоматизации
    chrome_options.add_argument(
        "user-agent=Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0")
    return chrome_options



