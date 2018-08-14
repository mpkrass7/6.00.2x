# -*- coding: utf-8 -*-
"""
Created on Sat Mar  3 09:29:31 2018

@author: mpkra
"""

songs = [('Roar',4.4, 4.0),('Sail',3.5, 7.7),('Timber', 5.1, 6.9),('Wannabe',2.7, 1.2)]

def song_playlist(songs, max_size):
    """
    songs: list of tuples, ('song_name', song_len, song_size)
    max_size: float, maximum size of total songs that you can fit

    Start with the song first in the 'songs' list, then pick the next 
    song to be the one with the lowest file size not already picked, repeat

    Returns: a list of a subset of songs fitting in 'max_size' in the order 
             in which they were chosen.
    """
    song_playlist = []
    currentSize = 0
    if songs[0][2] < max_size:
        song_playlist.append(songs[0][0])
        currentSize += songs[0][2]
    else:
        return song_playlist
    restList = sorted(songs[1:len(songs)], key= lambda songs: songs[2])
#    print(restList)
    for song in restList:
        if currentSize + song[2] < max_size:
            song_playlist.append(song[0])
            currentSize += song[2]
    return song_playlist
        
print(song_playlist(songs, 20))
print(song_playlist([('a', 4.4, 4.0), ('b', 3.5, 7.7), ('c', 5.1, 6.9), ('d', 2.7, 1.2)], 12.2))
