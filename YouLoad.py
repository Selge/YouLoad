from pytube import Playlist
import random
import time
import pytube.request
from pytube import YouTube
from pytube.cli import on_progress

1
2
3
4


# Setting up the playlist/list of playlists you might want to download
single_url = str(input("Please enter the single video URL:  ")).lower()
playlists = [Playlist(str(input("Please enter the playlist URL:  "))).lower()]
# url = input("https://www.youtube.com/playlist?list=whatever/put_here_any_video_link_you_want")
# playlists = [Playlist("https://www.youtube.com/playlist?list=whatever/put_here_any_playlist_link_you_want")]
# Setting up the list of target video formats
required_ext = ['mp4']


def on_complete(a, b):
    completed = "\nDownload completed!\n"
    size = 'File Size: ' + str(stream.filesize/1_000_000) + 'Mb\n'
    title = 'Title: ' + stream.title + '\n'
    desc = 'Description: ' + yt.description + '\n'
    author = 'Author: ' + yt.author + '\n'
    length = 'Video length: ' + str(yt.length) + 'Seconds\n'

    txt_list = [completed, title, author, desc, length, size]
    for item in txt_list:
        typewrite(.05, .1, item)
        print('-' * 60)

pytube.request.default_range_size = 500_000
yt = YouTube(single_url, on_progress_callback=on_progress, on_complete_callback=on_complete)
stream = yt.streams.filter(progressive=True, file_extension=required_ext[0]).get_highest_resolution()


def typewrite(num_1, num_2, text):
    for character in text:
        r = random.uniform(num_1, num_2)
        time.sleep(r)
        print(character, end='', flush=True)


def load_me_single():
    typewrite(.05, .1, 'Download is starting...\n')
    stream.download()


def load_me_plently(target_pl, ext):
    """ Loading all the videos from the target YouTube playlist """
    print(f'Downloading: {target_pl.title}')  # Writing a playlist name in console
    # iterating all the videos on the playlist:
    for video in target_pl.videos:
        print(f'Downloading: {video.title}')  # See what video is currently downloading
        # downloading:
        video.streams.filter(file_extension=f'{ext}').first().download(f"./{target_pl.title}")


# if __name__ == '__main__':
#     # calling the function/ target playlist and required video format are the arguments
#     load_me_plently(playlists[0], required_ext[0])
