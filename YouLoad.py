from pytube import Playlist

playlists = [Playlist("https://www.youtube.com/playlist?list=whatever/put_here_any_list_you_want")]
required_ext = ['mp4']


def load_me_plently(target_pl, ext):
    print(f'Downloading: {target_pl.title}')
    for video in target_pl.videos:
        print(f'Downloading: {video.title}')
        video.streams.filter(file_extension=f'{ext}').first().download(f"./{target_pl.title}")


if __name__ == '__main__':
    load_me_plently(playlists[0], required_ext[0])
