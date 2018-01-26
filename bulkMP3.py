from __future__ import unicode_literals
import youtube_dl


ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}
hyperlinkList = []
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    links = open("links.txt", "r")
    hyperlinkList = links.readlines()
    for link in hyperlinkList:
        ydl.download([link])
