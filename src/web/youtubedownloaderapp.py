
import os
from pytube import YouTube

# TODO: make script runnable from command line
# 1. Create new project for youtube downloader
# 2. Create project structure
# 3. pass parameters as command line variables
# 4. create main() function
# 5. create modules: pytube, converter, etc


def download_watchlist(url, file_path, audio_only=True):
    yt = YouTube('https://www.youtube.com/playlist?list=PLibRuvYnntNTWM2gp3vCVyciWtZWRAJoe')  # download watchlist?
    yt.streams.filter(progressive=False, only_audio=audio_only).all()
    # yt.streams.filter(progressive=False, file_extension='mp4').order_by('resolution').desc().first().download()


def download_single_video(url, file_path, audio_only=True):
    yt = YouTube(url)
    yt.title = yt.title.replace(" ", "_").replace("/", "")
    # download(save_path, aftersave_filename)
    yt.streams.filter(progressive=False, only_audio=audio_only).first().download()
    file_ext_download = ".mp4"
    file_ext_audio = ".mp3"
    target_file_path = file_path + "/" + yt.title + file_ext_download
    print(target_file_path)
    os.system("mv `pwd`/" + yt.title + file_ext_download + " " + target_file_path)
    os.system("ls " + target_file_path)
    if audio_only:
        os.system("ffmpeg -i " + target_file_path + " " + target_file_path.replace(file_ext_download, file_ext_audio))
        # remove mp4 file
    print("finished downloading")


if __name__ == '__main__':
    print(download_single_video('https://youtu.be/crM3pu-nig0', '/mnt/3bde1171-23bc-4713-a398-ce325f2843a1/1_Music/3_heavy_metal/MORBID_M3CHANICS'))
    # file_path = '/mnt/3bde1171-23bc-4713-a398-ce325f2843a1/1_Music/3_heavy_metal/MORBID_M3CHANICS'
    # os.system("mv `pwd`/*.mp4 " + file_path)
    # os.system("ls `pwd`'/Waveform Lobotomy.mp4'")
    # os.system("ls -lah `pwd`/*.mp4")
