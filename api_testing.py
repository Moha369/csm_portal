import requests
import json
import dateutil.parser

url = 'https://pixalate.atlassian.net/rest/api/2/search?jql=project=CS'

r = requests.get(url, auth=('paulb@pixalate.com', 'iqKaAYoiFfbY8P3uVrA6AEBB'))

data = r.json()

client_name = 'Fox TV'
client_ID = 'tv'

for ticket in data['issues']:
    ticket_number = ticket['key']
    summary = ticket['fields']['summary']
    assignee = ticket['fields']['assignee']['name']
    status = ticket['fields']['status']['name']
    updated = dateutil.parser.parse(ticket['fields']['updated'])
    ticket_url = 'https://pixalate.atlassian.net/browse/' + ticket['key']

    client = ticket['fields']['customfield_10907'][0]['value']

    if status != 'Closed' and client_name in client and client_ID.upper() in client:
        print(
            ticket_number, summary, assignee, status,
            updated.strftime('%m/%d/%Y'), ticket_url, client
        )
