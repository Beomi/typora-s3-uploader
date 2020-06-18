import os.path
from sys import argv
from uuid import uuid4
from pathlib import Path
import json
import boto3


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIGS = json.load(open(os.path.join(BASE_DIR, 'configs.json')))

s3 = boto3.client(
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

    filename = filename or os.path.basename(filepath)

    if use_random_hash:
        ext = filename.split('.')[-1]
        f_head = '.'.join(filename.split('.')[:-1])
        filename = '.'.join([f_head, uuid4().hex[:6], ext])

    upload_path = f'{s3_prefix}{filename}'
    filepath = Path(filepath)
    s3.put_object(
        Body=open(filepath, 'rb'),
        Bucket=CONFIGS['BUCKET_NAME'],
        Key=upload_path,
    )
    if cdn_prefix:
        uploaded_url = f'{cdn_prefix}/{s3_prefix}{filename}'
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
