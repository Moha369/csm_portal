from jira.client import JIRA
import requests

jira = JIRA(options={'server': 'https://pixalate.atlassian.net'},
            basic_auth=('paulb@pixalate.com', 'iqKaAYoiFfbY8P3uVrA6AEBB'))

# loop through all my CS Tickets
all_my_projs = jira.search_issues(
    'project=CS and reporter=5c9a07a6a54a69118b3211d6', maxResults=6)

for paul in all_my_projs:
    print(paul)


comment = jira.comments('CS-3106')
a = int(0)
for i in comment:
    if int(i.id) > a:
        a = int(i.id)
print(jira.comment('CS-3106', a).body)
