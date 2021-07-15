import urllib.request
from gtts import gTTS
from mutagen.mp3 import MP3
from moviepy.editor import *
from PIL import Image

def getContextImages(article,c,imgpath):
    '''Converts News API Image URL to a Image(.png)'''
    urllib.request.urlretrieve(article['urlToImage'],imgpath+str(c)+".png") #URL to Image Conversion
    image = Image.open(imgpath+str(c)+".png")
    new_image = image.resize((1920, 1080))  #Resizing the Image
    new_image.save(imgpath+str(c)+".png")

def generateAudio(article,c,audpath):
    '''Converts Text NEWS to audio(mp3)'''
    con = str(c+1)+article['title']+article["description"]  #Getting Content that needs to be converted to audio
    tts = gTTS(con,lang="en")   #Converting to audio
    tts.save(audpath+str(c)+'.mp3') #Saving the audio
    audio = MP3(audpath+str(c)+".mp3")    
    return int(audio.info.length)   #returning duration of audio

def generateVideo(duration,c,imgpath,audpath):
    '''generating video using images and audio'''
    clip = ImageSequenceClip([imgpath+str(c)+'.png'], durations=[duration]) 
    audioclip = AudioFileClip(audpath+str(c)+".mp3")
    videoclip = clip.set_audio(audioclip)
    return videoclip

def makeVideo(articles,imgpath,audpath,intro,outro):
    '''This Function Generates a Output Video'''
    if not os.path.exists(imgpath): #Making Directories to save files
        os.makedirs(imgpath)
    if not os.path.exists(audpath):
            os.makedirs(audpath)

    c = 0
    description = ''
    clips = []
    if intro != '': #Adding intro video
        clips.append(VideoFileClip(intro))
    for article in articles:
        try:
            if c > 10:  #Number of Headlines(Change it according to your need)
                break

            getContextImages(article,c,imgpath)

            duration = generateAudio(article,c,audpath)
            
            clips.append(generateVideo(duration,c,imgpath,audpath))

            desc = [['Source : ',article['source']['name']],
                    ['Author : ',article['author']],
                    ['Url : ',article['url']]]
            for des in desc:
                if des[1] is not None:
                    description += des[0]+des[1]+'\n'
            description += '\n'
            
            c += 1

            print("Clip",c,": Successfully Created")

        except Exception as e:
            print("Skipped one, there is a Problem")
            print("The Error Is",e,sep="\n")
    

    if outro != '': #Adding outro video
        clips.append(VideoFileClip(outro))
    outputVideo = concatenate_videoclips(clips,method='compose')
    outputVideo.to_videofile("output.mp4",threads=8, remove_temp=True)

    return description

if __name__ == "__main__":
    description = makeVideo(articles = '',
                            imgpath = '',
                            audpath = '',
                            intro = '',
                            outro = ''
                            )
