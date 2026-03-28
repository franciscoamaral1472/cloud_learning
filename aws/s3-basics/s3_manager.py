import boto3
from botocore.exceptions import ClientError
import os

s3 = boto3.client('s3')

def create_bucket(bucket_name, region='eu-west-1'):
    try:
        s3.create_bucket(
            Bucket=bucket_name,
            CreateBucketConfiguration={'LocationConstraint': region}
        )
        print(f"Bucket '{bucket_name}' created successfully.")
    except ClientError as e:
        print(f"Error creating bucket: {e}")

def upload_file(file_path, bucket_name, object_name=None):
    if object_name is None:
        object_name = os.path.basename(file_path)
    try:
        s3.upload_file(file_path, bucket_name, object_name)
        print(f"File '{file_path}' uploaded to '{bucket_name}/{object_name}'.")
    except ClientError as e:
        print(f"Error uploading file: {e}")

def list_files(bucket_name):
    try:
        response = s3.list_objects_v2(Bucket=bucket_name)
        if 'Contents' not in response:
            print("Bucket is empty.")
            return
        for obj in response['Contents']:
            print(f"  - {obj['Key']} ({obj['Size']} bytes)")
    except ClientError as e:
        print(f"Error listing files: {e}")

def download_file(bucket_name, object_name, download_path):
    try:
        s3.download_file(bucket_name, object_name, download_path)
        print(f"File '{object_name}' downloaded to '{download_path}'.")
    except ClientError as e:
        print(f"Error downloading file: {e}")

def delete_file(bucket_name, object_name):
    try:
        s3.delete_object(Bucket=bucket_name, Key=object_name)
        print(f"File '{object_name}' deleted from '{bucket_name}'.")
    except ClientError as e:
        print(f"Error deleting file: {e}")

if __name__ == "__main__":
    BUCKET = "my-learning-bucket-12345"

    create_bucket(BUCKET)
    upload_file("test.txt", BUCKET)
    list_files(BUCKET)
    download_file(BUCKET, "test.txt", "downloaded_test.txt")
    delete_file(BUCKET, "test.txt")