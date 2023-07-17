"""
author: Fani Keorapetse
date: 12 July 2023
"""

from os.path import join
from os import path
from subprocess import run

from pytube import YouTube, Search, Stream, Channel


class AmapionoYoutube:
    """
    Custom Youtube Class to allow one to search for mix or song and then store them in their appropriate directories once they are done downloading.
    It will also allow the user to interact with the youtube api and site to snatch the latest music and mixes for Amapiano.
    """

    def __init__(self, listOfArtists=[], listOfDjs=[], listOfChannels=[]):
        self.listOfArtists = listOfArtists
        self.listOfDjs = listOfDjs
        self.listOfChannels = listOfChannels

    def initialize(self):
        self.__streamsBasedOnDjs()

    def __getStreams(self, streamSearchTerm):
        streams = []
        query = Search(streamSearchTerm)
        for i in range(len(query.results)):
            id = query.results[i].video_id
            youtube_url = f""
            # stream = query.results[i].streams.get_by_itag(22)
            # # print(stream)
            # yt = YouTube(stream.url, allow_oauth_cache=True,use_oauth=True)
            # print(yt.age_restricted)
            # # print(stream)
            # is_age_restricted = yt.age_restricted

            # if is_age_restricted != True:
            #     streams.append(yt)
            #     print(yt)

        return streams

    def __streamsBasedOnArtists(self):
        pass

    def __streamsBasedOnDjs(self):
        streams = id = []
        for i in range(len(self.listOfDjs)):
            dj = self.listOfDjs[i]
            dj_streams = self.__getStreams(dj)
            streams.extend(dj_streams)
        print(streams)
        return streams

    def __streamsBasedOnChannels(self):
        pass

    def __download(self, stream):
        parent_dir = join(path.curdir, "audios")
        stream.download(parent_dir)
        return parent_dir

    def __saveMp4ToMp3(self, stream):
        parent_dir = self.download(stream)
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
