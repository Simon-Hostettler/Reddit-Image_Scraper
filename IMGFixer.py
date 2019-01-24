import subprocess
import os
import re
import logging
import traceback
from PIL import Image

#Directory where images are stored
directory = "xxx"

# Tries to open image file and checks errors
# If file does not open correctly, file deleted!
# WARNING: DO NOT HAVE ANY OTHER FILES THAN IMAGES IN THIS DIRECTORY!!!

files = os.listdir(directory)
for file in files:
    try:
        img = Image.open(directory+file)
        img.verify()
    except Exception:
        os.remove(directory+file)
        print("Invalid Image removed")

# Checks if PNG files have .jpg extension or JPG files have .png extension, renames them if possible
filelist=os.listdir(directory)
for file_obj in filelist:
    file_obj = directory + file_obj
    try:
        jpg_str = subprocess.check_output(['file', file_obj]).decode()
        if (re.search('JPEG image data', jpg_str, re.IGNORECASE)) and file_obj[-3:] == "png":

            old_path = os.path.splitext(file_obj)
            if not os.path.isfile(old_path[0]+'.jpg'):
                new_file = old_path[0]+'.jpg'
            elif not os.path.isfile(file_obj+'.jpg'):
                new_file = file_obj+'.jpg'
            else:
                print("Found JPG hiding as PNG but couldn't rename:", file_obj)
                continue

            print("Found JPG hiding as PNG, renaming:", file_obj, '->', new_file)
            subprocess.run(['mv', file_obj, new_file])
        if (re.search('PNG image data', jpg_str, re.IGNORECASE)) and file_obj[-3:] == "jpg":

            old_path = os.path.splitext(file_obj)
            if not os.path.isfile(old_path[0]+'.png'):
                new_file = old_path[0]+'.png'
            elif not os.path.isfile(file_obj+'.png'):
                new_file = file_obj+'.png'
            else:
                print("Found PNG hiding as JPG but couldn't rename:", file_obj)
                continue

            print("Found PNG hiding as JPG, renaming:", file_obj, '->', new_file)
            subprocess.run(['mv', file_obj, new_file])

    except Exception as e:
        logging.error(traceback.format_exc())

print("Cleaning JPGS and PNGS done")
