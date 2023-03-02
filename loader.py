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


def on_complete(a, b):
    completed = "\nDownload completed!\n"
    size = 'File Size: ' + str(stream.filesize/1_000_000) + 'Mb\n'
    title = 'Title: ' + stream.title + '\n'
    desc = 'Description: ' + yt.description + '\n'
    author = 'Author: ' + yt.author + '\n'
    length = 'Video length: ' + str(yt.length) + 'Seconds\n'

    txt_list = f'{completed}, {title}, {author}, {desc}, {length}, {size}'
    return txt_list


class Clip:
    def load_me_single(self):
        stream.download()


class Videolist:
    def load_me_plently(self, target_pl, ext):
        """ Loading all the videos from the target YouTube playlist """
        # iterating all the videos on the playlist:
        for video in target_pl.videos:
            # downloading:
            video.streams.filter(file_extension=f'{ext}').first().download(f"./{target_pl.title}")
