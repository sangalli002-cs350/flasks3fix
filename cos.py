import boto3

#PUT YOUR AWS CREDENTIALS IN THESE TWO LINES
aakid = ACCESS_ID
asak = ACCESS_KEY

s3_resource = boto3.resource('s3',
         aws_access_key_id=aakid,
         aws_secret_access_key= asak)

s3_client = boto3.resource('s3',
         aws_access_key_id=aakid,
         aws_secret_access_key= asak)


import uuid


def create_bucket_name(bucket_prefix):
    # The generated bucket name must be between 3 and 63 chars long
    return ''.join([bucket_prefix, str(uuid.uuid4())])



bucket_prefix='jrd'
BN = ''.join([bucket_prefix, str(uuid.uuid4())])
print ( "New Bucket about to be created:   " ,BN)
print(' ')




# create a new unique bucket 
s3_resource.create_bucket(Bucket=BN,
                          CreateBucketConfiguration={
                              'LocationConstraint': 'us-east-2'})





# Retrieve the list of existing buckets
response = s3_client.list_buckets()

# Output the bucket names
print('Existing buckets:')
for bucket in response['Buckets']:
    print(f'  {bucket["Name"]}')



#upload the file 
first_file_name='data.txt'
s3_resource.Object(BN, first_file_name).upload_file(
    Filename=first_file_name)
    

# download the file  
s3_resource.Object(BN, first_file_name).download_file(
    f'abc{first_file_name}')




for bucket_dict in s3_resource.meta.client.list_buckets().get('Buckets'):
    print(bucket_dict['Name'])




def delete_all_objects(bucket_name):
    res = []
    bucket=s3_resource.Bucket(bucket_name)
    for obj_version in bucket.object_versions.all():
        res.append({'Key': obj_version.object_key,
                    'VersionId': obj_version.id})
    print(res)
    bucket.delete_objects(Delete={'Objects': res})


# delete objects 
delete_all_objects(BN)

# delete bucket , however it must be empty first;  
s3_resource.Bucket(BN).delete()







print (" ")
print ("Finished")




