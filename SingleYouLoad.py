import random
import time
import pytube.request
from pytube import YouTube
from pytube.cli import on_progress


pytube.request.default_range_size = 500_000
required_ext = ['mp4']


def typewrite(num_1, num_2, text):
    for character in text:
        r = random.uniform(num_1, num_2)
        time.sleep(r)
        print(character, end='', flush=True)


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


url = input("Please enter the URL:  ")
try:
    yt = YouTube(url, on_progress_callback=on_progress, on_complete_callback=on_complete)
    stream = yt.streams.filter(progressive=True, file_extension=required_ext[0]).get_highest_resolution()
    typewrite(.05, .1, 'Download is starting...\n')
    stream.download()
except:
    print("Ooops, something went wrong. Please, doublecheck the link or the application code!")
#
# if __name__ == '__main__':
#     ...
