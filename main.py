import os,sys
import getpass


user = getpass.getuser()

filepath = "C:\\Users\\" + user + "\\AppData\\Local\\osu!\\Songs"

for dirName, subdirList, fileList in os.walk(filepath):
    print(dirName)
    for fname in fileList:
        if ".osu" in fname:
            with open(str(dirName)+ str('\\') +str(fname), "r+") as f:
                d = f.readlines()
                f.seek(0)
                for i in d:
                    if "ApproachRate" not in i:
                        f.write(i)
                    if "OverallDifficulty" in i:
                        f.write("ApproachRate:10\n")
                f.truncate()