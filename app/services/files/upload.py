import json
import io
from io import BytesIO
from time import sleep

import requests
from PIL import Image
from tinify import tinify
from werkzeug.utils import secure_filename

from config import Config


def image_to_byte_array(image):
    # Encode your PIL Image as a JPEG without writing to disk
    buffer = io.BytesIO()
    try:
        image.save(buffer, format='JPEG', quality=100)
    except:
        image.save(buffer, format='PNG', quality=100)

    desiredObject = buffer.getbuffer()

    return desiredObject


def upload_tinity(image_key, image):
    tinify.key = Config.TINYPNG_API_KEY
    path = f"{Config.AWS_BUCKET}/{image_key}"

    try:
        fh = Image.open(BytesIO(image))
    except:
        fh = Image.open(image)
    image = image_to_byte_array(fh)

    source = tinify.from_buffer(image)
    original = source.store(
        service="s3",
        aws_access_key_id=Config.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=Config.AWS_SECRET_ACCESS_KEY,
        region="us-east-1",
        path=path.lower()
    )

    # ENVIA IMAGEM REDUZIDA
    resized_180 = source.resize(
        method="fit",
        width=180,
        height=180
    )
    resized_180.store(
        service="s3",
        aws_access_key_id=Config.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=Config.AWS_SECRET_ACCESS_KEY,
        region="us-east-1",
        path=path.replace('original', 'small').lower()
    )

    resized_450 = source.resize(
        method="fit",
        width=450,
        height=450
    )
    resized_450.store(
        service="s3",
        aws_access_key_id=Config.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=Config.AWS_SECRET_ACCESS_KEY,
        region="us-east-1",
        path=path.replace('original', 'medium').lower()
    )

    resized_850 = source.resize(
        method="fit",
        width=850,
        height=850
    )
    resized_850.store(
        service="s3",
        aws_access_key_id=Config.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=Config.AWS_SECRET_ACCESS_KEY,
        region="us-east-1",
        path=path.replace('original', 'large').lower()
    )

    return dict(image_key=image_key)


def upload_file3(image, aws_key, filename=0):
    """
    It takes an image, an AWS key, and an optional filename, and uploads the image to AWS S3, resizing
    it to four different sizes, and returns the image key

    :param image: The image file to be uploaded
    :param aws_key: The path to the image on S3
    :param filename: The name of the file you want to upload, defaults to 0 (optional)
    :return: The image_key is being returned.
    """
    if filename == 0:
        filename = secure_filename(image.filename)

    path = "{}/original/{}".format(aws_key, filename)

    api_endpoint = 'https://api.kraken.io/v1/upload'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.85 Safari/537.36'
    }
    files = {
        'file': image
    }
    params = {
        "auth": {
            "api_key": "cb65bbe68cd9b4b1f32f9a3f4fbfa10d",
            "api_secret": "c46556c41826746e381090974aac27c93e2a6d01"
        },
        "s3_store": {
            "key": Config.AWS_ACCESS_KEY_ID,
            "secret": Config.AWS_SECRET_ACCESS_KEY,
            "bucket": Config.AWS_BUCKET,
            "region": Config.AWS_BUCKET_LOCATION
        },
        "wait": True,
        "resize": [
            {
                "id": "original",
                "strategy": "none",
                "storage_path": path.lower()
            },
            {
                "id": "small",
                "strategy": "auto",
                "width": 180,
                "height": 180,
                "storage_path": path.replace('original', 'small').lower()
            },
            {
                "id": "medium",
                "strategy": "auto",
                "width": 450,
                "height": 450,
                "storage_path": path.replace('original', 'medium').lower()
            },
            {
                "id": "large",
                "strategy": "auto",
                "width": 850,
                "height": 850,
                "storage_path": path.replace('original', 'large').lower()
            }
        ]
    }
    try:
        r = requests.post(url=api_endpoint, headers=headers, files=files, data={
            'data': json.dumps(params)
        }, timeout=15)
        status_code = r.status_code
        attempts = 0
        r_json = None if status_code != 200 else r.json()
        if status_code != 200:
            while attempts < 3:
                attempts += 1
                if status_code == 500:
                    sleep(1)
                    r = requests.post(url=api_endpoint, headers=headers, files=files, data={
                        'data': json.dumps(params)
                    }, timeout=15)
                    status_code = r.status_code
                    if status_code == 200:
                        r_json = r.json()
                        break
            if attempts == 3 and status_code == 500:
                r_json = upload_tinity(path, image)
                
        r_json['image_key'] = path.lower()
    except:
        r_json = upload_tinity(path, image)
    return r_json
