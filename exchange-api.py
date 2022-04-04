import json
import boto3
from boto3.dynamodb.conditions import Key

def lambda_handler(event, context):
    # TODO implement
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('bitstamp-live')
    
    channel = event["params"]["querystring"]["channel"]
    init = int(event["params"]["querystring"]["from"])
    to = int(event["params"]["querystring"]["to"])
    
    query_result = table.query(IndexName = 'channel-nmicrotimestamp-index', 
    KeyConditionExpression=Key('channel').eq(channel) & Key('nmicrotimestamp').between(init , to))
    
    e = event
    return {
        'statusCode': 200,
        'headers': {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*'},
        'body': query_result
    }