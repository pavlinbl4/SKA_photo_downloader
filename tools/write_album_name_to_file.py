
def save_album_name(album_name: str, script_dir: str):
    with open(f'{script_dir}/albums.txt', 'a', encoding='UTF8') as text_file:
        text_file.write(album_name + '\n')


def read_albums(script_dir):
    try:
        with open(f'{script_dir}/albums.txt', 'r', encoding='UTF8') as text_file:
            return text_file.readlines()
    except FileNotFoundError:
        with open(f'{script_dir}/albums.txt', 'w', encoding='UTF8') as text_file:
            text_file.close()
        return []
