import boto3
import uuid
import json
from environment import *

human_loop_name = str(uuid.uuid1())

textract = boto3.client('textract', aws_region)

response = textract.analyze_document(
  Document={'S3Object': {'Bucket': bucket_name, 'Name': document_name}},
  FeatureTypes=["TABLES", "FORMS"],
  HumanLoopConfig={
    'FlowDefinitionArn': flow_definition_arn,
    'HumanLoopName': human_loop_name,
    'DataAttributes': {'ContentClassifiers': ['FreeOfPersonallyIdentifiableInformation','FreeOfAdultContent']}
  }
)

print(json.dumps(response, indent=2, sort_keys=True))
