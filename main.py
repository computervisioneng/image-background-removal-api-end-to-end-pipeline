import os
import random
import string
import urllib

import boto3
import rembg
import cv2
from fastapi import FastAPI

import awscredentials


client = boto3.client(
                        's3',
                        aws_access_key_id=awscredentials.access_key,
                        aws_secret_access_key=awscredentials.secret_key
                        )

bucket_name = None


app = FastAPI()


@app.post("/remove_bg")
async def remove_bg(img_url):

    name = ''.join([random.choice(string.ascii_uppercase + string.ascii_lowercase) for j in range(10)]) + '.png'

    urllib.request.urlretrieve(img_url, './{}'.format(name))

    img = cv2.imread('./{}'.format(name))

    output = rembg.remove(img)

    cv2.imwrite('./{}'.format(name), output)

    client.upload_file('./{}'.format(name), bucket_name, name)

    os.remove('./{}'.format(name))

    return {"rmv_img_url": 'https://{}.s3.amazonaws.com/{}'.format(bucket_name, name)}