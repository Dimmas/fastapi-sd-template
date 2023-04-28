import io
from datetime import datetime, timezone
import uuid
import boto3
from config import AWSConfig


#Upload data to s3
def write_to_s3(image, fname, region_name='ru-1'):
    s3 = boto3.client('s3', region_name, endpoint_url=AWSConfig.host_name, aws_access_key_id=AWSConfig.aws_access_key_id, aws_secret_access_key=AWSConfig.aws_secret_access_key)
    s3.upload_fileobj(image, AWSConfig.bucket_name, fname)
    return f'{AWSConfig.host_name}/{AWSConfig.bucket_name}/{fname}'


def save_image(img):
    in_mem_file = io.BytesIO()
    img.save(in_mem_file, format='png')
    in_mem_file.seek(0)
    dt = datetime.now()
    file_name = str(uuid.uuid4())+'-'+str(int(dt.replace(tzinfo=timezone.utc).timestamp()))
    img_url = write_to_s3(in_mem_file, f'gallery/{file_name}.jpeg')
    return img_url, file_name
