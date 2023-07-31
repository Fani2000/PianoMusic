from pytube import YouTube, Search, Stream, Channel
import time
from os.path import join
from os import path
from subprocess import run

from Amapiano import AmapionoYoutube

def download(stream):
        parent_dir = join(path.curdir, "audios")
        stream.download(parent_dir)
        return parent_dir

def saveMp4ToMp3(stream):
    parent_dir = download(stream)
    filename = stream.default_filename
    mp4_filename = join(parent_dir, filename)
    mp3_filename = join(path.curdir, "mp3", f"{stream.title}.mp3", )

    run([
        'ffmpeg',
        '-i',
        mp4_filename.lower(),
        mp3_filename.lower()
    ])
    print("done")


with open('deep-house.txt', '+r') as f:
    djs = [d.split('\n')[0] for d in f.readlines()]


for dj in djs:
    query = Search(dj)
    for yt in query.results:
        time.sleep(1)
        print('DOWNLOADING...')
        stream = yt.streams.get_by_itag(22)
        saveMp4ToMp3(stream)
        print('DONE DOWNLOADING....')
        


# amapionoObj = AmapionoYoutube(
#     # listOfDjs=["Romeo Makota", "Dj Maphorisa", "StankyDj",
#     #            "MrJazzQ", "Kabza de small", "Mellow & Sleazy"]
#     # listOfDjs=["Soulful amapiano mix"]
#     listOfDjs=dj
# )
# amapionoObj.initialize()
