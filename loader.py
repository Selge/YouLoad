from pytube import Playlist
import random
import time
import pytube.request
from pytube import YouTube
from pytube.cli import on_progress


single_url = str(input("Please enter the single video URL:  ")).lower()
playlists = [Playlist(str(input("Please enter the playlist URL:  "))).lower()]
required_ext = ['mp4']
pytube.request.default_range_size = 500_000
yt = YouTube(single_url)
stream = yt.streams.filter(progressive=True, file_extension=required_ext[0]).get_highest_resolution()


class Clip:
    def __init__(self):
        self.video = single_url

    def load_me_single(self, video):
        video.stream.download(f"./{video.title}")


class Videolist:
    def __init__(self):
        self.target_pl = playlists
        self.required_ext = required_ext[0]

    def load_me_plently(self, target_pl, ext):
        for video in target_pl.videos:
            video.streams.filter(file_extension=f'{ext}').first().download(f"./{target_pl.title}")
