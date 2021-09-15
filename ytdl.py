import urllib.request
import re
import youtube_dl

from absl import app
from absl import flags
from pathlib import Path
from os import path, listdir, getcwd

FLAGS = flags.FLAGS
flags.DEFINE_string("search_keyword", "korean+talking", "ASCII, '+'for space bar")
flags.DEFINE_integer("file_num", 5, "number of files to download")

def is_have_music(id:str):
    html = urllib.request.urlopen("https://www.youtube.com/watch?v=" + id)
    chechlist = re.findall('<div id="description" slot="content" class="style-scope ytd-video-secondary-info-renderer">{}<div>', html.read().decode())

    return

def youtube_dl_hook(d):
    if d["status"] == "finished":
        print("Done downloading...")

def main(argv):
    
    html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + FLAGS.search_keyword)
    video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
    #print("https://www.youtube.com/watch?v=" + video_ids[0])

    ydl_opts = {
        "format": "bestaudio/best",
        "postprocessors": [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": "wav",
            "preferredquality": "44100",
        }],
        "outtmpl": "%(title)s.wav",
        "progress_hooks": [youtube_dl_hook],
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        for i in range(FLAGS.file_num):
            #if is_have_music([video_ids[i]]):

            info = ydl.extract_info(video_id, download=False)
            status = ydl.download([video_ids[i]])


if __name__ == '__main__':
    app.run(main)
