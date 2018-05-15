# /usr/bin/env python
from __future__ import print_function
from apiclient.discovery import build
from oauth2client import file, client, tools
from httplib2 import Http
# Download the twilio-python library from twilio.com/docs/libraries/python
from twilio.rest import Client

# USER: This stuff below is for authorising Google Sheets to send data to the app. It will save the credentials to your computer (locally!) once.
SCOPES = 'https://www.googleapis.com/auth/spreadsheets.readonly'
store = file.Storage('credentials.json')
creds = store.get()
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
    creds = tools.run_flow(flow, store)
service = build('sheets', 'v4', http=creds.authorize(Http()))
# USER: Put the google sheet id below
SPREADSHEET_ID = 'google sheet id here'
# USER: Put all the numbers in A:
# USER: Put the message to get sent out in cell B1
RANGE_NAME = 'TextList!A:B'
result = service.spreadsheets().values().get(spreadsheetId=SPREADSHEET_ID,
                                             range=RANGE_NAME).execut
# USER: Put the Twilio Auth stuff in here
# Find these values at https://twilio.com/user/account
account_sid = ""
auth_token = ""

client = Client(account_sid, auth_token)

# USER: If not using Google sheets interface, place correctly formatted numbers in here.
numbers = []

values = result.get('values', [])
if not values:
    print('No data found.')
else:
    for row in values:
        if row == []:
            continue
        if len(row) == 2:
            message = row[1]
        else:
            number = row[0]
            number = number.replace(" ", "")
            number = "+44" + number[1:]
            numbers.append(number)

# USER: Uncomment below for manual assignment of a message to send
# message = "example message here"

for number in numbers:
    client.api.account.messages.create(
        to=number,
        from_="+447480488859",
        body=message)

print("---\nmessaged", len(numbers), "numbers\n---" )
