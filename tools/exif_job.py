# pip install PyExifTool

import exiftool


def write_tags_to_image(file, _album_name):
    caption = (f'Хоккейный матч между командами'
               f'{_album_name}'
               f"     "
               f'ХК СКА')
    edited_tags = {"XMP:Title": 'ХОККЕЙ',
                   "IPTC:ObjectName": 'ХОККЕЙ',
                   'XMP:Rating': "3",
                   'XMP:Description': caption,
                   'IPTC:Caption-Abstract': caption,
                   'XMP:Credit': 'ХК СКА',
                   'IPTC:Credit': 'ХК СКА'}

    with exiftool.ExifToolHelper() as et:
        et.set_tags(
            [file],
            tags=edited_tags,
            params=["-P", "-overwrite_original", "-codedcharacterset=utf8"]
        )


def read_image_metadate(path_to_image_file):
    with exiftool.ExifToolHelper() as et:
        return et.get_metadata(path_to_image_file)[0]


