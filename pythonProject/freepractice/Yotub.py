#Youtube视频下载器
import pytube
from pytube import YouTube

link = input("Enter a youtube video's URL")  # 例如 https://youtu.be/dQw4w9WgXcQ

yt = pytube.YouTube(link)
yt.streams.first().download()

print("downloaded", link)