# from os.path import join
# from os import path
# from subprocess import run
from pytube import YouTube, Search, Stream, Channel

from Amapiano import AmapionoYoutube


def main():
    # yt = YouTube('http://youtube.com/watch?v=2lAe1cqCOXo')
    # query = Search('Mellow & Sleazy | Boiler Room')
    # query = Search("Mellow & Sleazy X DJ Maphorisa - Imali Ikhona")
    # query = Search("Romeo Makota")
    # print(query)
    # yt = query.results[0]
    # print(query.results)
    # print(yt.title)
    # print(yt.description)
    # print(yt.thumbnail_url)
    # streams = yt.streams.get_by_itag(22)
    # print(streams)
    # print(query.results)
    # stream = query.results[0].streams.get_by_itag(22)
    # print(stream)
    # if stream != None:
    #     saveMp4ToMp3(stream, 0)
    # for i in range(len(query.results)):
    #     stream = query.results[i].streams.get_by_itag(22)
    #     print(stream)
    #     if stream != None:
    #         saveMp4ToMp3(stream, i)

    # streams.download()
    pass


amapionoObj = AmapionoYoutube(
    listOfDjs=["Romeo Makota", "Dj Maphorisa", "StankyDj",
               "MrJazzQ", "Kabza de small", "Mellow & Sleazy"]
)
amapionoObj.initialize()


# yt = YouTube(
#     'https://www.youtube.com/watch?v=kMd2LDIeeVQ',
#     use_oauth=False,
#     allow_oauth_cache=True
# )
# # yt.bypass_age_gate()
# print(yt.streams)


main()
