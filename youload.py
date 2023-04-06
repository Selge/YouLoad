from pytube import Playlist
import random
import time
import pytube.request
from pytube import YouTube


# for the moment we use only this filetype, to be upgraded later
required_ext = ['mp4']
pytube.request.default_range_size = 500_000


class Single:
    def reprint(self):
        print("SINGLE")


class Multi:
    def reprint(self):
        print("MULTI")
