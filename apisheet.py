from googleapiclient.discovery import build
from google.oauth2 import service_account

# pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
# pip install --upgrade google-api-python-client


SERVICE_ACCOUNT_FILE = 'keys.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

# creates credentials with the scope
creds = None
creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1w1X00YL2uV_inK-l4VVbGXOXQpW1XoXlqkHFwDcJ-kc'

# creates service to access the google sheet api service
service = build('sheets', 'v4', credentials=creds)

# Call the Sheets API
sheet = service.spreadsheets()
result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                            range="Form Responses 1!A1:BN67").execute()
# only get the values                         
values = result.get('values', [])
#print(values)

if not values:
    print('No data found.')
else:
    count = 0
    for row in values:
        # Print columns B, which correspond to indices 1.
        print('%s' % (row[1]))
        count += 1
#print("Total Rows: " + str(count))

