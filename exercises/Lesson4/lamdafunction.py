import json

def lambda_handler(event, context):

    number=float(event)
    
    return {
        'statusCode': 200,
        'body' : json.dumps(f'Your number plus one is: {number+1}')
        }
