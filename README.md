# S3 Uploader for Typora, CLI ver.

Python/boto3 based S3 image(file) uploader.

Compatiable with [Typora](http://typora.io/).

## How to install

1. Clone this Repository.

```bash
git clone https://github.com/Beomi/typora-s3-uploader
```

2. Install with `install.sh` file.

> You need python3.7+ to use this package.

```bash
cd typora-s3-uploader
chmod +x *.sh
./install.sh
```

3. Copy `configs_example.json` to `configs.json`

```bash
cp configs_example.json configs.json
```

4. Edit `configs.json` with your keys.

```json
{
  "ACCESS_KEY": "AKIAYABCDWL6FVUJABCD",
  "SECRET_KEY": "00000000/abCdeFgsLqf4Zed15qU4j27y0000000",
  "BUCKET_NAME": "my-bucket",
  "REGION_NAME": "ap-northeast-2",
  "CDN_PREFIX": "https://mybucketcdn.cloudfront.net",
  "S3_PREFIX": "img/",
  "USE_RANDOM_HASH": true
}
```

- ACCESS_KEY: AWS Programmable ACCESS_KEY
- SECRET_KEY: AWS Programmable SECRET_KEY
- BUCKET_NAME: S3 Bucket name
- REGION_NAME: S3 Bucket Region name
- (Optional) CDN_PREFIX: Remove if you do not need.
- (Optional) S3_PREFIX: Add Key prefix when uploads your file.
- (Optional) USE_RANDOM_HASH: Add Random(UUID4) strings to the end of your filename.

5. Add script path information to Typora app.

Add upload.sh file path to Typora like the screenshot below.

![Add upload.sh file path to Typora](https://user-images.githubusercontent.com/11323660/84979524-94d72980-b16a-11ea-8e2b-e1e196f8e852.png)


Example path:

```
/Users/beomi/coding/typora-s3-uploader/upload.sh
```
