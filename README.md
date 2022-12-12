# YouLoad #

Very simple (perhaps this will become a more useful GUI application later) YouTube playlist downloader (using pytube library).


**Pytube link:**  ***https://pytube.io/en/latest/index.html***


### How this stuff works: ###

- First you may set up the list of the YouTube playlist links. 
The downloader uses each link as a pytube.Playlist class object: **Playlist(your_link_here)**

- Then we're setting a list of 
I didn't aim to put here all the existing formats that are possible to get from YouTube, you can experiment on your own.

- 

- The function itself looks like:
**video.streams.filter(file_extension=f'{ext}').first().download(f"./{target_pl.title}")** Where