# import pip._vendor.requests
from pytubefix import YouTube

yt = YouTube('https://www.youtube.com/watch?v=rDQfbjYx8kA',use_oauth=False)
video = yt.streams.filter(progressive=False, file_extension='mp4').order_by('resolution').desc().first().download('/Users/bilal/video_download')
# response = pip._vendor.requests.get("https://yt.lemnoslife.com/videos?part=mostReplayed&id=Ks-_Mh1QhMc");
print(video)