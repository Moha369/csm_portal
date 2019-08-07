import requests
import json
import dateutil.parser


jira_url = 'https://pixalate.atlassian.net/rest/api/2/search?jql=project=CS'

jira_r = requests.get(jira_url, auth=(
    'paulb@pixalate.com', 'iqKaAYoiFfbY8P3uVrA6AEBB'))

data = jira_r.json()

# client_name = 'Fox TV'
# client_ID = 'tv'

for ticket in data['issues']:
    ticket_number = ticket['key']
    summary = ticket['fields']['summary']
    assignee = ticket['fields']['assignee']['name']
    status = ticket['fields']['status']['name']
    updated = dateutil.parser.parse(ticket['fields']['updated'])
    ticket_url = 'https://pixalate.atlassian.net/browse/' + \
        ticket['key']
    client = ticket['fields']['customfield_10907'][0]['value']

    if status != 'Closed':

        ticket_dict = {
            'ticket_number': ticket_number,
            'summary': summary,
            'assignee': assignee,
            'status': status,
            'updated': updated,
            'url': ticket_url,
            'client_id': client
        }

        print(ticket_dict)
