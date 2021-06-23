
#The Author Name is Shikamaru Nara
#To this code to work import pytube 
# Go to python interpreter 
# Search for pytube
# Install pytube
from pytube import Playlist

try:
 aList=Playlist("Enter your playlist link here")


 def download_all():
     print(f'Downloading in process: {aList.title}')
     for video in aList.videos:
         video.streams.first().download()
 download_all()
print("The playlist downloaded sucessfully")
except Exception as e:
    print(e)
