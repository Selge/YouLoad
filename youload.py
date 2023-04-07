import pytube.request
from pytube import YouTube


# for the moment we use only this filetype, to be upgraded later
required_ext = ['mp4']
pytube.request.default_range_size = 500_000


class Single:
    def __init__(self):
        self.video = ''
        self.yt = YouTube(self.video)
        self.required_ext = required_ext[0]
        self.stream = self.yt.streams.filter(progressive=True,
                                             file_extension=self.required_ext[0]).get_highest_resolution()

    def load_me_single(self, video, *args):
        video.stream.download(f"./{video.title}")


class Multi:
    def __init__(self):
        self.target_pl = ''
        self.required_ext = required_ext[0]

    def load_me_plenty(self, target_pl, *args):
        for video in target_pl.videos:
            video.streams.filter(progressive=True,
                                 file_extension=self.required_ext[0]).get_highest_resolution().download(f"./{target_pl.title}")
