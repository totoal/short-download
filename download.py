import os
import sys

import pytube

def download_vid(n, url, folder):
    you = pytube.YouTube(url)

    # Replace '/' characters with '-'
    title = you.title.replace('/', '-')

    try:
        vid = you.streams.get_highest_resolution()
    except:
        print(f'Failed: {title}')
        return

    print(f'Downloading: {title}')

    vid.download(folder, filename=f'{n}.{title}')

if __name__ == '__main__':
    playlist_url = 'https://youtube.com/playlist?list=PLMj2crhs4VJS5lmbg0BIfHoljLSDZKfrW'

    p = pytube.Playlist(playlist_url)

    try:
        folder = sys.argv[1]
    except:
        folder = './downloaded/'

    if not os.path.exists(folder):
        os.mkdir(folder)

    for i, url in enumerate(p.video_urls):
        download_vid(i + 1, url, folder)
