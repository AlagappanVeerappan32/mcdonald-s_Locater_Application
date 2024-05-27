import json
import boto3
from algoliasearch.search_client import SearchClient

ALGOLIA_APP_ID = 'YourAlgoliaAppID'
ALGOLIA_API_KEY = 'YourAlgoliaAdminAPIKey'
ALGOLIA_INDEX_NAME = 'YourAlgoliaIndexName'
algolia_client = SearchClient.create(ALGOLIA_APP_ID, ALGOLIA_API_KEY)
index = algolia_client.init_index(ALGOLIA_INDEX_NAME)

client = boto3.client('location')

def lambda_handler(event, context):
    # TODO implement
    location=json.loads(event['body'])['location']
    print("location : {}".format(location))
    
    response = client.search_place_index_for_text(IndexName='YOUR_INDEX', 
    MaxResults=1, 
    Text=location
    )
    
    longi,lat = response["Results"][0]['Place']['Geometry']['Point']
    
    results = index.search('', {
    'aroundLatLng': '{}, {}'.format(lat,longi),
    'aroundRadius' : 100000 })
    return results
