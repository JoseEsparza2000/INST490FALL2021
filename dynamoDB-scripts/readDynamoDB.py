import boto3
from boto3.dynamodb.conditions import Key
from boto3.dynamodb.conditions import Attr
import pprint

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('testdb')


query = table.scan(
    FilterExpression = Attr('pkey').gte(1)
)

# print(type(float(query['Items'][0]['latitude'])))
# pprint.pprint(query['Items'])