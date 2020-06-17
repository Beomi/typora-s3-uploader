import os.path
from sys import argv
import json
import boto3


CONFIGS = json.load(open('configs.json'))

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


def upload_file(filepath, filename=None, prefix=''):
    filename = filename or os.path.basename(filepath)
    s3.meta.client.upload_file(
        filepath, CONFIGS['BUCKET_NAME'], prefix + filename
    )


def upload_all(filepaths):
    for path in filepaths:
        upload_file(path)


if __name__ == "__main__":
    filepaths = get_filepaths(argv)
    upload_all(filepaths)
