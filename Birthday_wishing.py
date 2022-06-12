# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client

def BirthDayWishing(destination:str,message:str):
    account_sid = 'AC253b5ca50b4f31e63b642fca0fc68a3d'
    auth_token = 'c4a254e5aaf9f7dfe4b785ca9f47b6d5'
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
            body=message,
            from_='+19783545798',
            to=destination
        )

    print(message.sid)

if __name__=="__main__":
    BirthDayWishing("to:number","Happy Birthday")
