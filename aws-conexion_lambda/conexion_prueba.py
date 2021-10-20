import json
import boto3

#os.environ['AWS_DEFAULT_REGION]'= 'us-west-2

s3 = boto3.resource('s3')

def lambda_handler(event,context):
    #trae datos del objeto o archivo puesto en s3

    for record in event['Records']:
        bucket = record['s3']['bucket']['name']
        archivo = record['s3']['object']['key']

        print("BUCKET: "+str(bucket))
        print("ARCHIVO: "+str(archivo))

    return{
        'statuscode:200'
    }