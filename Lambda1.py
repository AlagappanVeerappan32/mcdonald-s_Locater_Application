import json
from algoliasearch.search_client import SearchClient

# Initialize Algolia client
ALGOLIA_APP_ID = 'YourAlgoliaAppID'
ALGOLIA_API_KEY = 'YourAlgoliaAdminAPIKey'
ALGOLIA_INDEX_NAME = 'YourAlgoliaIndexName'
algolia_client = SearchClient.create(ALGOLIA_APP_ID, ALGOLIA_API_KEY)
index = algolia_client.init_index(ALGOLIA_INDEX_NAME)

def lambda_handler(event, context):
    # Check if the event is from DynamoDB Stream or direct invocation
    if 'Records' in event:
        # Handle DynamoDB Stream event
        for record in event['Records']:
            if record['eventName'] in ['INSERT', 'MODIFY']:
                new_image = record['dynamodb']['NewImage']
                item = {k: v[list(v.keys())[0]] for k, v in new_image.items()}
                index.save_object(item, {'objectID': item['id']})
            elif record['eventName'] == 'REMOVE':
                old_image = record['dynamodb']['OldImage']
                item_id = old_image['id']['S']
                index.delete_object(item_id)
    else:
        # Handle direct invocation
        item = event
        index.save_object(item, {'objectID': item['id']['S']})

    return {
        'statusCode': 200,
        'body': json.dumps('Successfully processed event.')
    }
