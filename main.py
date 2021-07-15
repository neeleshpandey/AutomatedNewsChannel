from newsapi import NewsApiClient
from MakeVideo import makeVideo
from UploadOnYoutube import uploadOnYoutube
from CleanUp import cleanUp

API_KEY = "" #Add NEWS API Here

DOWNLOAD_IMAGES = './images/' #Add path to download images
GEN_AUDIO = './audio/'  #Add path to save generated audio
INTRO_VIDEO = './intro.mp4' #Add path of intro video
OUTRO_VIDEO = ''    #Add path of outro video



#Step 1: Getting Top Headlines

print("Step 1: Getting Top Headlines")

try:
    newsapi = NewsApiClient(api_key= API_KEY)
    all_articles = newsapi.get_top_headlines(category = 'technology',
                                            country = 'us',
                                            language='en',
                                            )
except Exception as e:
    print("There is some problem with API")
    print("The ERROR is",e,sep="\n")

print("Step 1 Completed")




#Step 2: Making a Video

print("Step 2: Making a Video")

description = makeVideo(articles = all_articles['articles'],
                        imgpath = DOWNLOAD_IMAGES,
                        audpath = GEN_AUDIO,
                        intro = INTRO_VIDEO,
                        outro = OUTRO_VIDEO
                        )

print("Step 2 Completed")



#Step 3: Uploading Video on YouTube

print("Step 3: Uploading Video on YouTube")

uploadOnYoutube(description)

print("Step 3 Completed")



#Step 4: Clean Up

print("Step 4: Clean Up")

cleanUp(imgfolder = DOWNLOAD_IMAGES,
        audfolder = GEN_AUDIO
        )

print("Step 4 Completed")

print("MISSION ACCOMPLISHED")
