# YouLoad #

Very simple (perhaps this will become a more useful GUI application later) YouTube playlist downloader (using pytube library).


**Pytube link:**  ***https://pytube.io/en/latest/index.html***


### How this stuff works: ###

- First you may set up the list of the YouTube playlists links. 
The downloader uses each link as a ***pytube.Playlist*** class object, so I put it to the list like
**[Playlist(your_link_here), Playlist(your_link_here_1), Playlist(your_link_here_2) etc.]** , but you may find a better way to.  

- Then we're setting a list of target video formats.
I didn't aim to put here all the existing formats that are possible to get from YouTube, you can experiment on your own.

- After that we're calling the **Main** function and using playlist and format list objects as arguments.
- Program considers each YouTube playlist as a list of video objects. It iterates all the videos and downloads it one by one.
Computer outputs to the console Name of a currently downloading playlist and a name of a currently downloading video.
- The download command itself looks like:
**video.streams.filter(file_extension=f'{ext}').first().download(f"./{target_pl.title}")** where **ext** is replaced by your 
target video file extension (mp4, 3gp, whatever YouTube has) and **./{target_pl.title}** - automatically created directory 
(it will have the same name as a playlist which files are stored there) for saving video files from the currently downloading playlist.