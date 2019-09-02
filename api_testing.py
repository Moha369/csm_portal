import requests
import json
import dateutil.parser

jira_url = 'https://pixalate.atlassian.net/rest/api/2/search?jql=project=CS'

jira_r = requests.get(jira_url, auth=(
    'paulb@pixalate.com', 'ZgQI2j1wrMOle9z1iWVK9747'))

data = jira_r.json()
print(json.dumps(data, indent=2))

for ticket in data['issues']:
    ticket_number = ticket['key']
    summary = ticket['fields']['summary']
    # assignee = ticket['fields']['assignee']['name']
    status = ticket['fields']['status']['name']
    updated = dateutil.parser.parse(ticket['fields']['updated'])
    ticket_url = 'https://pixalate.atlassian.net/browse/' + \
        ticket['key']
    client = ticket['fields']['customfield_10907'][0]['value']

    if status != 'Closed':

        ticket_dict = {
            'ticket_number': ticket_number,
            'summary': summary,
            # 'assignee': assignee,
            'status': status,
            'updated': updated,
            'url': ticket_url,
            'client_id': client
        }

        print(ticket_number, summary, status,
              updated.strftime('%m/%d/%Y'), ticket_url, client)


# Pendo -

def pendo_visitor_info(self):
    pendo_url = "https://app.pendo.io/api/v1/visitor/awgm/history"

    params = {
        "starttime": '1564654385000'
    }
    headers = {
        'x-pendo-integration-key': "ea51020f-cb13-470e-5e55-ff27d25528e7",
        'content-type': "application/x-www-form-urlencoded"
    }

    # get current day in epoch
    current_day = time.time()
    current_day_format = datetime.datetime.fromtimestamp(current_day)
    readable_current_day = current_day_format.strftime(
        '%d-%m-%Y - %H:%M:%S')
    print(readable_current_day)

    response = requests.get(pendo_url, headers=headers, params=params)
    data = response.json()
