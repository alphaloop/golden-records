import requests
import json
from dataclasses import dataclass
from time import sleep, time

API_ROOT = 'https://api.archery-records.net/api/'
ENDPOINTS = ['archers', 'awards', 'awardslist', 'categories', 'classes', 'classifications', 'currenthandicaps', 'handicaps', 'rounds', 'scores', 'seasons', 'settings', 'types']

@dataclass
class RequestError(Exception):
    error: str    

class Client():

    def __init__(self, apiKey, pageSize=1000):
        self.apiKey = apiKey
        self.pageSize = pageSize
        self.lastRequest = time()-1

    def call_endpoint(self, endpoint, params={}):

        if endpoint not in ENDPOINTS:
            raise RequestError('%s is not a valid endpoint' % endpoint)

        results = []
        page = 1
        has_more_pages = True

        while(has_more_pages):
            
            response = self._request(endpoint, pageNumber=page, params=params)
            has_more_pages = json.loads(response.headers['Paging-Headers'])["nextPage"] == 'Yes'

            try:
                parsed = json.loads(response.text)
            except:
                raise RequestError('Error parsing response: ' + response.text)
            
            if parsed:
              results = results + parsed
            
            page = page + 1

        return results


    def _request(self, endpoint, pageNumber=1, params={}):
        
        headers = {
            'Accept': 'application/json',
            'Authorization': self.apiKey
        }
        
        parameters = {
            'pageNumber': pageNumber,
            'pageSize': self.pageSize
        }

        if params:
            parameters = parameters | params

        self._do_not_exceed_rate_limit()

        response = requests.get(API_ROOT + endpoint, params=parameters, headers=headers)

        if not response.ok:
            raise RequestError('%d %s' % (response.status_code, response.text))
        
        return response
    

    def _do_not_exceed_rate_limit(self):
        
        if time() - self.lastRequest <= 1:
            sleep(1)

        self.lastRequest = time()