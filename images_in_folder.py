import os
from loguru import logger

from exif_job import write_tags_to_image
from send_photo_tg import send_photo_as_file

# Получаем путь к директории скрипта


logger.add(sink='scr', format="{time} {level} {message}", level="INFO")
logger.remove()


def action_with_image_in_folder(directory, _album_name):
    # Store the list of files once to avoid multiple calls
    all_files = os.listdir(directory)
    logger.info(f"Files found: {all_files}")
    files = [os.path.join(directory, f) for f in all_files if f.endswith('JPG')]
    for file in files:
        logger.info(file)
        # write info to image iptc
        write_tags_to_image(file, _album_name)
        # send image as file via telegram
        send_photo_as_file(file)


if __name__ == '__main__':
    action_with_image_in_folder(
        './tests/test_images/', '_album_name')
