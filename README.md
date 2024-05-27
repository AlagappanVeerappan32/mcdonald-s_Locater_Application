# McDonald's Locator App

## Overview

The McDonald's Locator App is a backend service that helps users find the nearest McDonald's locations anywhere in the world. By feeding a dataset of all McDonald's locations into the system, users can easily search for the closest restaurant based on their current location. This backend service utilizes AWS cloud services to get the latitude and longitude of the user’s location and returns the nearest McDonald's locations.

## Features

- **Location-based Search:** Find the nearest McDonald's locations based on the user's address or coordinates.
- **AWS Integration:** Uses AWS Lambda, DynamoDB, API Gateway, and Amazon Location Service.
- **Geo Search:** Integrates with Algolia's Geo Search Database to store and search location data efficiently.

## Services Used

- **Python**: Main programming language.
- **AWS Lambda**: For running serverless functions.
- **DynamoDB**: To store all McDonald's locations.
- **API Gateway**: To handle API requests.
- **Amazon Location Service**: To convert addresses to coordinates.
- **Algolia**: For fast and efficient geo-search capabilities.

## Architecture

1. **DynamoDB**: Stores all McDonald's locations.
2. **AWS Lambda**: 
   - First Lambda function: Inserts locations into Algolia with geolocation data.
   - Second Lambda function: Retrieves nearby McDonald's locations based on the user's coordinates.
3. **API Gateway**: Interfaces with the Lambda functions.
4. **Amazon Location Service**: Converts addresses to latitude and longitude.
5. **Algolia**: Stores and searches location data.

## Steps to Set Up

1. **Create DynamoDB Table**:
   - Acts as the client-side database.
   - Store all McDonald's locations in this table.
2. **Enable DynamoDB Stream**:
   - For real-time data insertion into Algolia via Lambda.
3. **Set Up Lambda Functions**:
   - Use the Algolia API to create a client and an index.
   - Create a place index using Amazon Location Service.
   - Insert records with geolocation data into Algolia.
   - Assign necessary roles and permissions to the Lambda functions.
4. **Lambda Layer**:
   - Add dependencies for Algolia.
5. **Test Data Insertion**:
   - Ensure data is correctly inserted into DynamoDB and Algolia with latitude and longitude.
6. **Set Up Second Lambda Function**:
   - Retrieve user’s address and search in Algolia.
   - Use API Gateway to get user’s address.
   - Use Amazon Location Service to get coordinates.
   - Search in the Algolia database.
7. **Testing**:
   - Use Postman to test the API endpoints using addresses.
  
## Architecture 
Here's an overview of the system architecture:

![System Architecture](diagram.png)

## Testing

- **Postman**: Use Postman to send requests to the API and test the responses.
- **Check Data**: Verify that data is correctly inserted and retrieved from DynamoDB and Algolia.

## Future Enhancements

- Integrate a front-end interface to provide a complete web application experience.
- Add more detailed error handling and logging for better debugging.
- Implement caching for frequently searched locations to improve performance.

