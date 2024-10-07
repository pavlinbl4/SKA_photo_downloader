
def save_album_name(album_name: str):
    with open('albums.txt', 'a', encoding='UTF8') as text_file:
        text_file.write(album_name + '\n')


def read_albums():
    try:
        with open('albums.txt', 'r', encoding='UTF8') as text_file:
            return text_file.readlines()
    except FileNotFoundError:
        with open('albums.txt', 'w', encoding='UTF8') as text_file:
            text_file.close()
        return []
