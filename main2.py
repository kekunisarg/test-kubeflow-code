import DateTime.DateTime as dt
import sys
import os
from google.cloud import storage


def main_func(username = None, level = None):
    print("Inside main method... Date & Time : "+str(dt()))
    if username is not None and level is not None:
        print("Uername = ", username)
        print("Level = ",level)
    else:
        print("User Details are not provided")

def upload_file_to_bucket(blob_name, file_path, bucket_name):
    try:
        os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'nth-plexus-320009-0bed73b5d7c8.json'
        storage_client = storage.Client()

        bucket = storage_client.get_bucket(bucket_name)
        blob = bucket.blob(blob_name)
        blob.upload_from_filename(file_path)
        return True
    except Exception as e:
        print(e)
        return False

if __name__ == '__main__':
    arg_list = sys.argv
    if len(arg_list) == 3:
        username = arg_list[1]
        level = arg_list[2]
        main_func(username, level)
    else:
        main_func()

    filepath = f'{os.getcwd()}/output/'
    print(filepath)
    print(os.path.join(filepath,'data.csv'))
    status = upload_file_to_bucket('input/data_new.csv',os.path.join(filepath,'data.csv'),'input_bucket_test_1')
    print(status)
