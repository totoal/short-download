import os
import sys

import pytube

def download_vid(url, folder):
    you = pytube.YouTube(url)

    try:
        vid = you.streams.get_highest_resolution()
    except:
        print(f'Failed: {you.title}')
        return

    print(f'Downloading: {you.title}')

    vid.download(folder)

if __name__ == '__main__':
    playlist_url = 'https://youtube.com/playlist?list=PLMj2crhs4VJS5lmbg0BIfHoljLSDZKfrW'

    p = pytube.Playlist(playlist_url)

    try:
        folder = sys.argv[1]
    except:
        folder = './'

    if not os.path.exists(folder):
        os.mkdir(folder)

    for url in p.video_urls:
        download_vid(url, folder)
