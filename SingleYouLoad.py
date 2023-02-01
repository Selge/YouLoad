from pytube import YouTube
from pytube.cli import on_progress


required_ext = ['mp4']


def typewrite(num_1, num_2, text):
    ...


def on_complete():
    completed = "\nDownload completed!\n"
    size = 'File Size: ' + str(stream.filesize/1_000_000) + 'Mb\n'
    title = 'Title: ' + stream.title + '\n'
    desc = 'Description: ' + yt.description + '\n'
    author = 'Author: ' + yt.author + '\n'
    length = 'Video length: ' + str(yt.length) + 'Seconds\n'


url = input("Please enter the URL:  ")
yt = YouTube(url, on_progress_callback=on_progress, on_complete_callback=on_complete)
stream = yt.streams.filter(progressive=True, file_extension=required_ext[0]).get_highest_resolution()


if __name__ == '__main__':
    ...
