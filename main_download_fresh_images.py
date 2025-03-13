import os
from pathlib import Path
from struct import error

from loguru import logger
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from compare_with_saved_data import CompareWithSavedData
from tools.clear_folder_from_old_files import delete_old_folder
from tools.crome_options import setting_chrome_options
from tools.exif_job import write_tags_to_image
from tools.image_downloader import downloader
from tools.send_message_to_telegram import send_telegram_message
from tools.write_album_name_to_file import save_album_name

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=setting_chrome_options())

script_dir = os.path.dirname(os.path.abspath(__file__))
log_file_path = os.path.join(script_dir, "ska_downloader_log.log")
logger.add(log_file_path, format="{time} {level} {message}", level="INFO", retention="1 day", rotation="1 day")


def albums_links(url: str):
    try:
        driver.get(url)
        return driver.find_elements(By.XPATH, "//div[@class='card card-media ']")
    except error:
        logger.error(error)


def last_album(all_albums):
    try:
        return all_albums[0].find_element(By.TAG_NAME, 'a').get_attribute('href')
    except error:
        logger.error(error)


def all_images(last_album_url):
    try:
        driver.get(last_album_url)
        album_name = driver.find_element(By.XPATH, '(//div[@class="container"])[3]').text
    except error:
        logger.error(error)

    all_elements = driver.find_elements(By.XPATH, "//img[@class='item-img']")
    return [x.get_attribute('src') for x in all_elements], album_name


if __name__ == '__main__':
    # получаю список всех альбомов
    _all_albums = albums_links('https://www.ska.ru/media/album/')

    # получаю ссылку на самый свежий альбом
    _last_album_url = last_album(_all_albums)
    logger.info(f'{_last_album_url = }')

    # получаю название альбома
    _album_name = all_images(_last_album_url)[1]
    logger.info(_album_name)

    with open(f'{script_dir}/albums.txt', 'w', encoding='UTF8') as text_file:
        text_file.write('')

    # проверяю не скачан ли альбом ранее


    if CompareWithSavedData(script_dir, 'albums.txt', _album_name).compare():
    # old_albums = read_albums(script_dir)
    # logger.info(old_albums = read_albums())

    # if _album_name + '\n' not in old_albums:

        # нужно получить ссылки на все снимки в альбоме
        images_links_list = all_images(_last_album_url)[0]
        logger.info(f'{len(images_links_list) = }')

        Path(f'{script_dir}/images/{_album_name}').mkdir(parents=True, exist_ok=True)
        path_to_download = Path(f'{script_dir}/images/{_album_name}')
        logger.info(path_to_download)

        save_album_name(_album_name, script_dir)
        send_telegram_message(_album_name)

        # игровые снимки начинаются примерно с 40 кадра, берем срез в 20 снимков
        for image_link in images_links_list:
            # for image_link in images_links_list:
            print(image_link)
            downloader(image_link, _album_name)

        write_tags_to_image(path_to_download, _album_name)

        # upload fresh images

        # delete downloaded files after upload

    else:
        print("NO NEW ALBUMS")

    # delete_old_files(path_to_download, 'jpg', 1)

    delete_old_folder(f'{script_dir}/images', 1)
