# Golden Records API Client

A simple Python API client for accessing data in Golden Records via its API.

https://api.archery-records.net/help

The client handles authentication, results paging and rate limiting, and optional parameters.

The client only handles `GET` requests to avoid the risk of inadvertently updating data.

## Usage

Create client with API key:
```
from goldenrecords.client import Client
API_KEY='your-api-key'
client = Client(API_KEY)
```

## Examples

Get all types of archery (call `GET /api/types`):
```
types = client.call_endpoint('types')
```

Get all scores for an archer with a given UID (call `GET /api/scores?id=<archer id>`):
```
scores = client.call_endpoint('scores', {'id': '<archer id>'})
```