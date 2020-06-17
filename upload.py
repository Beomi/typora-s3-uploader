import os.path
from sys import argv
from uuid import uuid4
import json
import boto3


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIGS = json.load(open(os.path.join(BASE_DIR, 'configs.json')))

s3 = boto3.resource(
    's3',
    aws_access_key_id=CONFIGS['ACCESS_KEY'],
    aws_secret_access_key=CONFIGS['SECRET_KEY'],
    region_name=CONFIGS['REGION_NAME'],
)


def get_filepaths(args):
    filepaths = []
    args.pop(0)  # Remove `upload.py` filename
    for i in args:
        filepaths.append(i)
        if i == None:
            break
    return filepaths


def upload_file(
        filepath,
        filename=None,
        s3_prefix='',
        cdn_prefix='',
        use_random_hash=False):
    if use_random_hash:
        s3_prefix += uuid4().hex[:6]

    filename = filename or os.path.basename(filepath)
    s3.meta.client.upload_file(
        filepath, CONFIGS['BUCKET_NAME'], s3_prefix + filename
    )
    if cdn_prefix:
        uploaded_url = cdn_prefix + s3_prefix + filename
    else:
        uploaded_url = (
            f'https://s3-{CONFIGS["REGION_NAME"]}.amazonaws.com/{CONFIGS["BUCKET_NAME"]}/{s3_prefix}/{filename}'
        )
    return uploaded_url


def upload_all(filepaths):
    for path in filepaths:
        print(upload_file(
            path,
            s3_prefix=CONFIGS.get('S3_PREFIX'),
            cdn_prefix=CONFIGS.get('CDN_PREFIX'),
            use_random_hash=CONFIGS.get('USE_RANDOM_HASH'),
        ))


if __name__ == "__main__":
    filepaths = get_filepaths(argv)
    upload_all(filepaths)
