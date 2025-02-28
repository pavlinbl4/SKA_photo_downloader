from chrome_driver import ChromeDriver


def main():
    with ChromeDriver('https://www.ska.ru/media/album/') as driver:
        driver.driver_get()  # Открываем страницу
        title = driver.get_page_title()  # Получаем заголовок страницы
        print(f"Заголовок страницы: {title}")  # Выводим заголовок
        albums_links = driver.find_elements_locator("xpath", "//div[@class='card card-media ']")
        last_album_url = albums_links[0].find_element("tag name", 'a').get_attribute('href')
        print(last_album_url)

if __name__ == '__main__':
    main()
