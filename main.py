from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

from crome_options import setting_chrome_options
from image_downloader import downloader
from write_album_name_to_file import save_album_name, read_albums

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=setting_chrome_options())


def albums_links(url: str):
    driver.get(url)
    return driver.find_elements(By.XPATH, "//div[@class='card card-media ']")


def last_album(all_albums):
    return all_albums[0].find_element(By.TAG_NAME, 'a').get_attribute('href')


def all_images(last_album_url):
    driver.get(last_album_url)
    album_name = driver.find_element(By.XPATH, '(//div[@class="container"])[3]').text
    all_elements = driver.find_elements(By.XPATH, "//img[@class='item-img']")
    return [x.get_attribute('src') for x in all_elements], album_name


if __name__ == '__main__':
    # получаю список всех альбомов
    _all_albums = albums_links('https://www.ska.ru/media/album/')

    # получаю ссылку на самый свежий альбом
    _last_album_url = last_album(_all_albums)

    # нужно получить ссылки на све снимки в альбоме
    images_links_list = all_images(_last_album_url)[0]
    # получаю название альбома
    _album_name = all_images(_last_album_url)[1]

    # проверяю не скачан ли альбом ранее
    old_albums = read_albums()
    print(old_albums)

    if _album_name + '\n' not in old_albums:

        save_album_name(_album_name)

        # игровые снимки начинаются примерно с 40 кадра, берем срез в 20 снимков
        for image_link in images_links_list[40: 60]:
            print(image_link)
            # downloader(image_link)
    else:
        print("NO NEW ALBUMS")
