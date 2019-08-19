import fbchat
import os
import json

import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint
from googleapiclient import discovery

from fbchat import Client
from fbchat.models import *
from fbchat import Message
from session import get_session

from lock import door_unlock

import datetime
import random

#Google Sheets API
#scope necessary for google sheets api
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

spreadsheet_id = "" #add spreadsheet id here. can be found in the sheets url

#directory for personal credentials
DIRNAME = os.path.dirname(__file__)
credentials = ServiceAccountCredentials.from_json_keyfile_name(
    os.path.join(DIRNAME, 'credentials.json'),
    scope
)

service = discovery.build('sheets', 'v4', credentials=credentials)
client = gspread.authorize(credentials)




#fbchat API
email = '' #email of facebook account that is sending the messages
password = '' #above's password
cookies = get_session()
fb_client = Client(email, password, session_cookies=cookies)
recip_id = 0 #change to the recipient's user id

#make sure fb is logged in
def fb_working():
    if not fb_client.isLoggedIn():
        fb_client.login(email,password)

#send message
def send_msg(name, opened):
    message = name + " has "
    if opened:
        message += "opened the door."
    else:
        message += "unsuccessfully tried to open the door."
    fb_client.send(Message(text=message), thread_id=recip_id)



while True:
    try:
        id_ = input("scan tag ") # request user to scan
        sheet = client.open("name of sheet").sheet1  # Open the spreadhseet, input the name of your spreadsheet


        sheet2 = service.spreadsheets()
        result = sheet2.values().get(spreadsheetId=spreadsheet_id,
                                    range="Allowed!A3:B").execute() #depending on data you might need to change the range.
        allowed = result.get('values')


        sheet3 = service.spreadsheets()
        rank_result = sheet3.values().get(spreadsheetId=spreadsheet_id,
                                    range="Ranking!B3:B").execute() #also might need to change range
        entries = rank_result.get('values')

        id_found = False

        for i in range(len(allowed)):
            if id_ == allowed[i][1]:
                id_found = True
                print("door opened @ ")
                time = datetime.datetime.now()
                print(time)

                name = allowed[i][0] 
                insertRow = [str(time),
                                name]
                sheet.insert_row(insertRow,4)
                

                value = int(entries[i][0]) + 1
                entries[i][0] = value
                body = {
                    'values':entries
                }
                sheet3.values().update(spreadsheetId=spreadsheet_id, range="Ranking!B3:B",
                                    valueInputOption = "USER_ENTERED", body = body).execute()

                fb_working()
                send_msg(name, id_found)

                door_unlock()
        if not id_found:
            fb_working()
            send_msg("Someone", id_found)
    except:
        print("error occured") #keeps the loop running





