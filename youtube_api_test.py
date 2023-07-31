from pytube import YouTube, Search, Stream, Channel

from Amapiano import AmapionoYoutube

with open('deep-house.txt', '+r') as f:
    dj = [d.split('\n')[0] for d in f.readlines()]



amapionoObj = AmapionoYoutube(
    # listOfDjs=["Romeo Makota", "Dj Maphorisa", "StankyDj",
    #            "MrJazzQ", "Kabza de small", "Mellow & Sleazy"]
    # listOfDjs=["Soulful amapiano mix"]
    listOfDjs=dj
)
amapionoObj.initialize()
