# pip install PyExifTool

import exiftool
from icecream import ic


def write_tags_to_image(file, _album_name):
    caption = (f'Хоккейный матч между командами                 '
               f'{_album_name}'
               f'                                    '
               f'ХК СКА')
    edited_tags = {"XMP:Title": 'ХОККЕЙ',
                   "IPTC:ObjectName": 'ХОККЕЙ',
                   'XMP:Rating': "3",
                   'XMP:Description':  caption,
                   'XMP:Label': 'Red',
                   'XMP:Creator': 'ХК СКА'}
    with exiftool.ExifToolHelper() as et:
        et.set_tags(
            [file],
            tags=edited_tags,
            params=["-P", "-overwrite_original"]
        )


def read_image_metadate(path_to_image_file):
    with exiftool.ExifToolHelper() as et:
        return et.get_metadata(path_to_image_file)[0]


if __name__ == '__main__':
    tags = {
        "IPTC:ObjectName": "title",

        'XMP:Subject': "keywords/exiftool",

        'XMP:Creator': 'Eugene Pavlenko/exiftool',
        'XMP:Rights': 'Pavlenko Evgeniy',
        'XMP:Credit': 'Pavlenko Evgeniy',
        'IPTC:By-line': 'Pavlenko Evgeniy',
        'IPTC:Credit': '',
        'IPTC:CopyrightNotice': 'Pavlenko Evgeniy',

        'Photoshop:SlicesGroupName': ''
    }

    edited_tags = {"XMP:Title": 'ХОККЕЙ',
                   "IPTC:ObjectName": 'ХОККЕЙ',
                   'XMP:Rating': "3",
                   'XMP:Description': "Матч по хоккею",
                   'XMP:Label': 'Red',
                   'XMP:Creator': 'ХК СКА'}

    test_ol_image = './tests/test_images/20010402_pavl_18_up.jpeg'

    write_tags_to_image(test_ol_image, edited_tags)
    ic(read_image_metadate(test_ol_image))
