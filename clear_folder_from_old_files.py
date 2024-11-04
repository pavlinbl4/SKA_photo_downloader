import os
import shutil
import sys
from datetime import datetime, timedelta

from loguru import logger

# Получаем путь к директории скрипта
script_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
log_file_path = os.path.join(script_dir, "deleted_from_downloads_files.log")

logger.add(log_file_path, format="{time} {level} {message}", level="INFO")


# Удаляем все обработчики
# logger.remove()


def delete_old_files(directory, extensions, minutes):
    cutoff_date = datetime.now() - timedelta(minutes=minutes)
    count = 0

    # Store the list of files once to avoid multiple calls
    all_files = os.listdir(directory)

    for ext in extensions:
        files = [os.path.join(directory, f) for f in all_files if f.endswith(ext)]
        for file in files:
            try:
                modified_date = datetime.fromtimestamp(os.path.getmtime(file))
                if modified_date < cutoff_date:
                    if os.path.isfile(file):
                        os.remove(file)
                        logger.info(f"Удален файл: {file}")
                        count += 1
            except Exception as e:
                logger.error(f"Error processing file {file}: {e}")
    logger.info(f"{count} files were deleted")


def delete_old_folder(directory, minutes):
    cutoff_date = datetime.now() - timedelta(minutes=minutes)
    items = os.listdir(directory)
    folders = [item for item in items if os.path.isdir(os.path.join(directory, item))]
    if len(folders) > 0:
        for folder in folders:
            path_to_dir = os.path.join(directory, folder)
            modified_date = datetime.fromtimestamp(os.path.getmtime(path_to_dir))
            if modified_date < cutoff_date:
                shutil.rmtree(path_to_dir)
                logger.info(f"Удален фолдер: {folder}")
    else:
        logger.info("Nothing to delete")


if __name__ == '__main__':
    delete_old_files('images', [
        'jpg',
        'jpeg',
        'JPEG',
        'JPG'
    ], 1)

    delete_old_folder('images', 1)
