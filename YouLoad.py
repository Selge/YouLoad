from pytube import Playlist

# Setting up the playlist/list of playlists you might want to download
playlists = [Playlist("https://www.youtube.com/playlist?list=whatever/put_here_any_playlist_link_you_want")]
# Setting up the list of target video formats
required_ext = ['mp4']


def load_me_plently(target_pl, ext):
    """ Loading all the videos from the target YouTube playlist """
    print(f'Downloading: {target_pl.title}')  # Writing a playlist name in console
    # iterating all the videos on the playlist:
    for video in target_pl.videos:
        print(f'Downloading: {video.title}')  # See what video is currently downloading
        # downloading:
        video.streams.filter(file_extension=f'{ext}').first().download(f"./{target_pl.title}")


if __name__ == '__main__':
    # calling the function/ target playlist and required video format are the arguments
    load_me_plently(playlists[0], required_ext[0])
