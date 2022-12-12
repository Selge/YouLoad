# YouLoad #

Very simple (Perhaps this will become a more useful GUI application later) YouTube playlist downloader (using pytube library).


Pytube link:  **https://pytube.io/en/latest/index.html**

### How this stuff works: ###

Please note the list item format: that should look like [Playlist(your_link), Playlist(your_link_1)]

I didn't aim to put here all the existing formats that are possible to get from YouTube, you can experiment on your own.

The function itself looks like:
video.streams.filter(file_extension=f'{ext}').first().download(f"./{target_pl.title}")