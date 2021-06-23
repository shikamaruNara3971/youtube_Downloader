
#The Author Name is Shikamaru Nara
#To this code to work import pytube 
# Go to python interpreter 
# Search for pytube
# Install pytube
from pytube import YouTube
youtube_video_url = 'Enter your Video link here'

try:
    yt_obj = YouTube(youtube_video_url)

    filters = yt_obj.streams.filter(progressive=True, file_extension='mp4')
    print(filters)
    # download the highest quality video
    filters.get_highest_resolution().download(output_path='Specify the path here', filename='Your_Video.mp4')
    print('Video Downloaded Successfully')
except Exception as e:
    print(e)
