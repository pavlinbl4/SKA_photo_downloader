import os
import shutil
import sys
import time
from datetime import datetime, timedelta
from loguru import logger

# Получаем путь к директории скрипта
script_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
log_file_path = os.path.join(script_dir, "deleted_from_downloads_files.log")

logger.add(log_file_path, format="{time} {level} {message}", level="INFO")


def delete_old_files(directory, extensions, minutes):
    logger.info("Check old files in folder")
    """
    Удаляет файлы с указанными расширениями в заданной директории,
    если они были созданы или изменены раньше, чем указанное число дней от текущей даты.

    Args:
        directory (str): Путь к директории.
        extensions (list): Список расширений файлов для удаления (например, ['.tmp', '.log']).
        days (int): Количество дней, после которых файлы будут удалены.
    """
    cutoff_date = datetime.now() - timedelta(minutes=minutes)
    count = 0
    logger.info(os.listdir(directory))
    for ext in extensions:
        # files = [os.path.join(directory, f) for f in os.listdir(directory) if f.endswith(ext)]
        files = [os.path.join(directory, f) for f in os.listdir(directory) if os.path.isdir(f)]
        logger.info(files)
        for file in files:
            modified_date = datetime.fromtimestamp(os.path.getmtime(file))
            logger.info(f'{modified_date = }, {cutoff_date = }')
            if modified_date < cutoff_date:
                if os.path.isfile(file):
                    os.remove(file)
                    logger.info(f"Удален файл: {file}")
                    count += 1

        time.sleep(1)  # Задержка в 1 секунду для визуализации
    logger.info(f"{count} files were deleted")



def delete_old_folder(directory,  minutes):
    cutoff_date = datetime.now() - timedelta(minutes=minutes)
    items = os.listdir(directory)
    folders = [item for item in items if os.path.isdir(os.path.join(directory, item))]
    logger.info(folders)
    for dir in folders:
        path_to_dir = os.path.join(directory, dir)
        modified_date = datetime.fromtimestamp(os.path.getmtime(path_to_dir))
        logger.info(path_to_dir)
        if modified_date < cutoff_date:
            shutil.rmtree(path_to_dir)
            logger.info(f"Удален фолдер: {dir}")


if __name__ == '__main__':
    # delete_old_files('images', [
    #     'jpg',
    #     'jpeg',
    #     'JPEG',
    #     'JPG'
    # ], 1)
    delete_old_folder('images', 1)
