from PIL import Image
import requests
from io import BytesIO


async def url_to_img(url):
    response = requests.get(url)
    return Image.open(BytesIO(response.content))


async def compress_img(img, filename):
    img.save(filename, 'JPEG', quality=1)
