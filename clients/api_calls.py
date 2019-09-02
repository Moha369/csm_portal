import requests
import json


def jira_data():
    url = 'https://pixalate.atlassian.net/rest/api/2/search?jql=project=CS'
    r = requests.get(url, auth=(
        'paulb@pixalate.com', 'ZgQI2j1wrMOle9z1iWVK9747'))
    data = r.json()
    print(json.dumps(data, indent=2))
    return data


def pendo_data():
    # url = 'https://app.pendo.io/api/v1/aggregation'
    url = 'https://app.pendo.io/api/v1/visitor/gwm'
    headers = {
        'x-pendo-integration-key': "ea51020f-cb13-470e-5e55-ff27d25528e7",
        'content-type': "application/json"
    }

    r = requests.get(url, headers=headers)
    data = r.json()
    first_visit = data['metadata']['auto']['firstvisit']
    print(first_visit)
    return first_visit
