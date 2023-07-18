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
        self.streams = self.__streamsBasedOnDjs()
        if len(self.streams) > 0:
            # TODO: 1. Download the streams
            # TODO: 2. Convert the stream into mp3 
            # TODO: 3. 
            pass

    def __getStreams(self, streamSearchTerm):
        streams = []
        query = Search(streamSearchTerm)
        results_length = len(query.results)
        i = 0
        while i < results_length:
            try:
                stream = query.results[i].streams.get_by_itag(22)
                streams.append(stream)
            except Exception as error:
                print(error)
                print('Moving to the next i.')
            finally:
                i += 1

        return streams

    def __streamsBasedOnArtists(self):
        pass

    def __streamsBasedOnDjs(self):
        streams = id = []
        for i in range(len(self.listOfDjs)):
            dj = self.listOfDjs[i]
            dj_streams = self.__getStreams(dj)
            streams.extend(dj_streams)
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
