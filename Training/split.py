import glob
import os
import tkinter
import tkinter.constants
import tkinter.filedialog
import subprocess

while True:
    print("Please select your image directory.")
    current_dir = tkinter.filedialog.askdirectory()
    if current_dir == None or current_dir == "":
        print("You must select a directory.")
        continue
    break

# Percentage of images to be used for the validate set and test set (each)
percentage_test = 20

# Create and/or truncate train.txt and test.txt
file_train = open('train.txt', 'w')
file_test = open('test.txt', 'w')

# Populate train.txt and test.txt
counter = 1
index_test = round(100 / percentage_test)
for pathAndFilename in glob.iglob(os.path.join(current_dir, "*.jpg")):
    title, ext = os.path.splitext(os.path.basename(pathAndFilename))
    if counter == index_test:
        counter =  1
        file_test.write(current_dir + "/" + title + '.jpg' + "\n")
    else:
        file_train.write(current_dir + "/" + title + '.jpg' + "\n")
        counter = counter + 1
subprocess.call(['./split.sh'])
