# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 01:09:53 2023

@author: Lucky
"""

import os
import pytube
from moviepy.editor import *
from pytube import Playlist

def get_mp3(url, folder):
    # Create a PyTube object and get the audio stream
    yt = pytube.YouTube(url)
    stream = yt.streams.filter(only_audio=True).first()
    
    # Download the audio stream and save it as an mp4 file
    mp4_file = stream.download()
    
    # Use MoviePy to convert the mp4 file to an mp3 file
    mp3_file = os.path.splitext(mp4_file)[0] + ".mp3"
    audio_clip = AudioFileClip(mp4_file)
    audio_clip.write_audiofile(mp3_file)
    
    # Delete the original mp4 file
    os.remove(mp4_file)
    
    if not os.path.exists(folder):
        os.makedirs(folder)
    
    # Move the mp3 file to the audio folder
    os.replace(mp3_file, os.path.join(folder, os.path.basename(mp3_file)))
    

def urls_from_playlist(playlist_urls):
    
    # Create a PyTube playlist object
    playlist = Playlist(playlist_url)
    
    # Get the video URLs from the playlist
    video_urls = []
    for video in playlist.videos:
        video_url = video.watch_url
        video_urls.append(video_url)
        
    return video_urls

if __name__ == "__main__":
    
    # Specify the URL of the YouTube playlist
    playlist_url = "https://www.youtube.com/playlist?list=<playlist>"
    # Create/Select the folder to store the mp3 file
    folder = "audio"
    
    video_urls = urls_from_playlist(playlist_url)
    
    for url in video_urls:
        get_mp3(url, folder)
