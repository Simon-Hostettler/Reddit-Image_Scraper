import praw
from tqdm import tqdm
import requests
import time as t
import os.path

reddit = praw.Reddit(client_id = "xxx",
                     client_secret = "xxx",
                     username= "xxx",
                     password="xxx",
                     user_agent="xxx")

reddit_data = reddit.subreddit("xxx").hot(limit=None)
image_list = []
start_time = t.time()
directory = "xxx"
img_limit = 25

def download_img(img_url):
    img = requests.get(img_url)
    filename = img_url.split("/")[-1]

    try:
        img.raise_for_status()
    except Exception:
        print("There was a problem...")
    if not os.path.isfile(directory + filename):
        file = open(directory + filename, "xb")
        for chunk in img.iter_content(10000):
            file.write(chunk)

for image in reddit_data:
    if len(image_list) > img_limit:
        print("Images found! Starting download")
        break
    elif("Some requirements the image needs to have, can leave empty"):
        image_list.append(image.url)

for image in image_list:
    download_img(image)
    print('Image ' + str(int(image_list.index(image) + 1)) + ' downloaded!\n')

print('Program finished without errors! Runtime:' + str(int(t.time()) - start_time) + ' seconds')
