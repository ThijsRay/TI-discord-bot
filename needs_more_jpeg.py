from PIL import Image
import requests
from io import BytesIO


async def url_to_img(url):
    response = requests.get(url)
    return Image.open(BytesIO(response.content))


async def compress_img(img, filename, times):
    img = img.convert("RGB")
    ratio = math.pow(2 , times)
    if times is not None:
        img.resize((img.size[0]*ratio,img.size[1]*ratio), Image.ANTIALIAS)
    img.save(filename, 'JPEG', quality=1)
