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

    filename = ''.join([random.choice(string.ascii_uppercase + string.ascii_lowercase) for j in range(10)]) + '.png'

    urllib.request.urlretrieve(img_url, filename)

    img = cv2.imread(filename)

    output = rembg.remove(img)

    cv2.imwrite(filename, output)

    client.upload_file(filename, bucket_name, filename)

    os.remove(filename)

    return {"rmv_img_url": 'https://{}.s3.amazonaws.com/{}'.format(bucket_name, filename)}