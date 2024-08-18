import os
import yt_dlp

def download_tiktok_profile(profile_url):
    ydl_opts = {
        'format': 'best',
        'outtmpl': '%(title)s.%(ext)s',
        'noplaylist': True,
        'download_archive': 'downloaded.txt',  # To keep track of downloaded videos
        'ignoreerrors': True
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([profile_url])

if __name__ == '__main__':
    profile_url = input("Enter the TikTok profile URL: ")
    download_tiktok_profile(profile_url)
