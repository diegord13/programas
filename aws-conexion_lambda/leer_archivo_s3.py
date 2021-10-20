import boto3
def lambda_handler(event,context):
    s3 = boto3.client('s3')
    if event:
        print("Event : ", event)
        file_obj = event['Records'][0]
        filename = str(file_obj['s3']['object']['key'])
        print("Filename: ", filename)
        fileObj = s3.get_object(Bucket = "aws-lambda-trigger", key=filename)
        print("File_obj", fileObj)
        file_content = fileObj["Body"].read().decode("utf-8")
        print(file_content)

    return 'mensaje'