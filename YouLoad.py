from pytube import Playlist

playlists = [Playlist("https://www.youtube.com/playlist?list=PLPrskxx43-yngz6Cz7x_tWas4hpzsrE3P")]
required_ext = ['mp4']


def load_me_plently(target_pl, ext):
    print(f'Downloading: {target_pl.title}')
    for video in target_pl.videos:
        print(f'Downloading: {video.title}')
        vids = video.streams.filter(file_extension=f'{ext}')
        vids.first().download(f"./{target_pl.title}")


if __name__ == '__main__':
    load_me_plently(playlists[0], required_ext[0])
