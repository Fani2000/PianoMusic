from os.path import join
from os import path
from subprocess import run
from pytube import YouTube, Search, Stream, Channel

def main():
    # yt = YouTube('http://youtube.com/watch?v=2lAe1cqCOXo')
    query = Search('Romeo Makota')
    # print(query)
    # yt = query.results[0]
    # print(query.results)
    # print(yt.title)
    # print(yt.description)
    # print(yt.thumbnail_url)
    # streams = yt.streams.get_by_itag(22)
    # print(streams)
    for i in range(len(query.results)):
        stream = query.results[i].streams.get_by_itag(22)
        print(stream)
        saveMp4ToMp3(stream, i)

    # streams.download()

def saveMp4ToMp3(stream, i): 
    parent_dir = join(path.curdir,"audios")
    stream.download(parent_dir)
    filename = stream.default_filename
    run([
        'ffmpeg',
        '-i',
        join(parent_dir, filename),
        join(parent_dir, i, '.mp3')
    ])
    print("done")

main()
    
    
