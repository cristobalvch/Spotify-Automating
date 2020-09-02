
#libraries
import eyed3
import os 
import time
import re
import csv 
import numpy as np

#Let the user introduce the path music folder
path = str(input("Please Introduce the Path Folder: "))

#Save the paths of each mp3 file on a list called "filenames"
filenames = []
for r,d,f in os.walk(path):
    for file in f:
        if file.endswith(".mp3"):
            filenames.append(file)

#Obtain the features of each mp3 file and saved them on 3 lists 

name_song = []
name_artist  = []
name_album = []

for filename in filenames:
    pathfile = path + "\\" + filename
    audioinfo = eyed3.load(pathfile)

    #in case the mp3 file doesn't have detail information, use the name of the mp3 file to  append the song list.
    if not audioinfo.tag.title:
        temp_name = re.findall("^(.+?).mp3",filename)[0].replace("_"," ")
        name_song.append(temp_name)
    else:
        name_song.append(audioinfo.tag.title)

    name_artist.append(audioinfo.tag.artist)

    #in case the mp3 file doesn't have detail information, append the album list with nan
    if not audioinfo.tag.album:
        name_album.append(np.nan)
    else:
        name_album.append(audioinfo.tag.album)

#print the total number of the tracks obtained
print(f"{str(len(name_song))} tracks obtained! ")


time.sleep(0.05)


#Save the information into a  csv file
#let the user introduce the name of the new csv file
name_file = str(input("Please Introduce the name of the new csv file: "))

with open(name_file,"w",encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerows(zip(name_song,name_artist,name_album))

f.close()

print(f"{name_file} saved and closed!")


