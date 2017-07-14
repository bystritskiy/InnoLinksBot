import httplib2
import os
import sqlite3
from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage
from httplib2 import socks
import config

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None


# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/sheets.googleapis.com-python-quickstart.json
SCOPES = 'https://www.googleapis.com/auth/spreadsheets.readonly'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Google Sheets API Python Quickstart'


DATABASE = '/home/InnoLinksBot/mysite/database/test.db'


#app.config.from_object(__name__)




def create_database(path):
    if os.path.isfile(path):
        os.remove(path)
    conn = sqlite3.connect(path)
    cursor = conn.cursor()
    cursor.execute(config.create_db_command)
    print("Table created successfully...")
    conn.commit()
    cursor.close()
    conn.close()


def get_credentials():

    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'googleapis.com-python-quickstart.json')

    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else:
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials

def fill_database(path):

    credentials = get_credentials()

    #proxy_info = httplib2.ProxyInfo(proxy_type=socks.PROXY_TYPE_HTTP, proxy_host="proxy.server", proxy_port=3128)

    http = credentials.authorize(httplib2.Http())

    discoveryUrl = ('https://sheets.googleapis.com/$discovery/rest?' 'version=v4')
    #developerKey = 'AIzaSyDPpFPHSyVi3Evr0yPCxUkFRoVYSSCO9IA'

    service = discovery.build('sheets', 'v4', http = http, discoveryServiceUrl=discoveryUrl)

    spreadsheetId = '1DyqVpqeS5yBlMNJxVNhPxDn6oJBLwyd7sPrPhgR1xtA'
    rangeName = 'Лист1!A2:H'
    result = service.spreadsheets().values().get(spreadsheetId=spreadsheetId, range=rangeName).execute()

    #print(result)

    values = result.get('values', [])
    conn = sqlite3.connect(path)
    cursor = conn.cursor()

    id = 0
    for row in values:

        size = len(row)

        card_title = str(row[0].replace('\\n', " "))

        category = str(row[1].replace('\\n'," "))

        subcategory = str(row[2].replace('\\n', " "))

        if size==3:
            description = ''
            address = ''
            phone = ''
            schedule = ''
            links = ''
        elif size==4:
            description = str(row[3].replace('\\n', " "))
            address = ''
            phone = ''
            schedule = ''
            links = ''
        elif size==5:
            description = str(row[3].replace('\\n', " "))
            address = str(row[4].replace('\\n', " "))
            phone = ''
            schedule = ''
            links = ''
        elif size==6:
            description = str(row[3].replace('\\n', " "))
            address = str(row[4].replace('\\n', " "))
            phone = str(row[5].replace('\\n', " "))
            schedule = ''
            links = ''
        elif size==7:
            description = str(row[3].replace('\\n', " "))
            address = str(row[4].replace('\\n', " "))
            phone = str(row[5].replace('\\n', " "))
            schedule = str(row[6].replace('\\n', " "))
            links = ''
        elif size==8:
            description = str(row[3].replace('\\n', " "))
            address = str(row[4].replace('\\n', " "))
            phone = str(row[5].replace('\\n', " "))
            schedule = str(row[6].replace('\\n', " "))
            links = str(row[7].replace('\\n', " "))


        id += 1

        cursor.execute("INSERT INTO COMPANY (id,name,category,subcategory,description,address,phone,schedule,links) \
                                VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(id, card_title,category,
                                                                                                subcategory,description,address,phone,schedule,links ))
    conn.commit()
    cursor.close()
    conn.close()
    print("Information imported")





