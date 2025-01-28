from io import BytesIO
import requests
import urllib3
from PIL import Image
from tools.file_name_from_link import extract_file_name


# pip install requests Pillow


def downloader(image_url: str, _album_name: str):
    try:
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

        response = requests.get(image_url, stream=True, verify=False)

        # Step 2: Open the image using Pillow
        image = Image.open(BytesIO(response.content))

        # Step 3: Convert to RGB (JPEG does not support transparency)
        rgb_image = image.convert('RGB')

        # Step 4: Save the image as JPEG
        rgb_image.save(f"./images/{_album_name}/{extract_file_name(image_url)}.JPG", 'JPEG')

    except Exception as ex:
        print(f'{ex = }, {f"./images/{_album_name}/{extract_file_name(image_url)}.JPG"}')
