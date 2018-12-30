import json
import sys
import requests


WXT_ACCESS_TOKEN    = None #Replace None with your access token between quotes.
EMAIL_OLD           = None #Replace None with the email address to change
EMAIL_NEW           = None #Replace None with the email address to change to


#sets the header to be used for authentication and data format to be sent.
def setHeaders():
    accessToken_hdr = 'Bearer ' + ACCESS_TOKEN
    webex_teams_header = {'Authorization': accessToken_hdr, 'Content-Type': 'application/json; charset=utf-8'}
    return (webex_teams_header)


#check for the unique user id based on email address
def FindUserID(the_header,Old_Email):
    uri = 'https://api.ciscospark.com/v1'
    api_call= '/people?email='+Old_Email
    resp = requests.get(uri+api_call, headers=the_header)
    resp = resp.json()
    for item in resp["items"]:
            id= item['id']
    return(id)

def Change_Mail(the_header,UserID,New_Email):
    uri = 'https://api.ciscospark.com/v1'
    api_call= '/people/'+UserID
    body = {"toPersonEmail": "gifbot@webex.bot", "text": "Hello"}
    resp = requests.put(uri+api_call, json=body, headers=the_header)
    resp = resp.json()

    return(id)



if __name__ == '__main__':
    if WXT_ACCESS_TOKEN==None or EMAIL_OLD==None:
        sys.exit("Please check that variables WXT_ACCESS_TOKEN, EMAIL_OLD and EMAIL_NEW have values assigned.")
    header=setHeaders()
    #passing the old email address to find the user_id of the user
    user_id=FindUserID(header,EMAIL_OLD)
    Change_Mail(the_header,user_id,EMAIL_NEW)
    print(user_id)
