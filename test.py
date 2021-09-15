import urllib.request
import re
import youtube_dl

from absl import app
from absl import flags
from pathlib import Path
from os import path, listdir, getcwd

FLAGS = flags.FLAGS
flags.DEFINE_string("search_keyword", "read+korean+books", "search_keyword")

def main(argv):
    
    html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + FLAGS.search_keyword)
    print(html.read().decode())
    video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())

if __name__ == '__main__':
    app.run(main)