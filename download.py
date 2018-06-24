from __future__ import unicode_literals
import youtube_dl
import os

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'wav',
        'preferredquality': '200',
    }],
}
hyperlinkList = []
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    links = open("links.txt", "r")
    hyperlinkList = links.readlines()
    for link in hyperlinkList:
        os.chdir("songs")
        ydl.download([link])
        os.chdir("..")
