from Google import Create_Service
from googleapiclient.http import MediaFileUpload

CLIENT_SECRET_FILE = 'client_secrets.json'  #API File Add Here(client Secret File)
API_NAME = 'youtube'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/youtube.upload']

def uploadOnYoutube(description):  #Video Uploading Function
    service = Create_Service(CLIENT_SECRET_FILE,API_NAME,API_VERSION,SCOPES)

    request_body={
        'snippet':{
            'categoryId':25,  
            'title':'Todays Top Tech Headlines | Latest Tech News', #Title
            'description':description,   #Description
            'tags':['Tech News','News']   #Tags
        },
        'status':{
            'privacyStatus':'public',       #Add Privacy Status ["public","private","unlisted"]
            'selfDeclaredMadeForKids': False
        },
    'notifySubscribers': False
    }

    mediaFile = MediaFileUpload('.\output.mp4') #Selecting File(video) Which Is To Be Uploded

    response_upload = service.videos().insert(
        part='snippet,status',
        body=request_body,
        media_body=mediaFile
    ).execute()

if __name__ == "__main__":
    uploadOnYoutube('')