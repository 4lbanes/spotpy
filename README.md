YouTube Video Playlist Manager
This project is a YouTube video playlist manager that allows users to search for videos by name, download them, and play them with interactive keyboard controls. The program also generates a summary of the watched videos at the end.

Features
Video Search: Allows users to search for YouTube videos by typing the name.
Video Download: Downloads videos in MP4 format with the best available resolution.
Video Playback: Plays downloaded videos with keyboard controls for pausing, skipping, adjusting volume, and more.
Summary Creation: Generates a summary of watched videos and saves it to a summary.txt file.
Technologies Used
Python: Main programming language.
Pytube: Library for downloading YouTube videos.
OpenCV: Library for video manipulation and display.
FFPyPlayer: Library for synchronized video and audio playback.
Google API Client: Library for integration with the YouTube API.
Prerequisites
Python 3.x
The following Python libraries installed:
pytube
opencv-python
ffpyplayer
google-api-python-client
You can install them using pip:

bash
Copiar código
pip install pytube opencv-python ffpyplayer google-api-python-client
How to Use
Clone the repository or download the files.

Obtain a YouTube API key and insert it into the YOUTUBE_API_KEY variable in the code.

Run the Python script:

bash
Copiar código
python main.py
Enter the names of the videos you want to add to the playlist. Type 'done' to finish the list.

Control video playback using the following keys:

q: Stop the video and exit.
w: Increase volume.
s: Decrease volume.
d: Skip forward 5 seconds.
a: Rewind 5 seconds.
m: Mute/unmute the sound.
p: Pause/unpause the video.
0: Return to the beginning of the video.
n: Skip to the next video in the playlist.
b: Go back to the previous video in the playlist.
Video Summary: At the end, a summary.txt file will be created with the titles of the watched videos.

License
This project is open source and is licensed under the terms of the MIT license.

Author: João Arthur Veras Barros Dias
