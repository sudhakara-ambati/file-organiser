# -=-=-= imports =-=-=-
import shutil, os, sys
from os import listdir
from os.path import isfile, join

# -=-=-= file extensions =-=-=-
# media
image_exts = ["bmp", "gif", "jpeg", "jpg", "png", "svg", "tif", "tiff", "ico"]
video_exts = ["avi", "fly", "m4v", "mkv", "mov", "mp4", "mpg", "mpeg", "wmv"]
audio_exts = ["mp3", "wav"]

# documents
text_exts = ["pdf", "txt", "doc", "docx"]
presentations_exts = ["ppt", "pptx", "pps"]
spreadsheets_exts = ["xls", "xlsm", "xlsx"]

# other
compressed_exts = ["rar", "zip"]
internet_exts = ["html", "css", "js", "php"]

#   code
python_exts = ["py"]
csharp_exts = ["cs"]

executable_exts = ["bat", "exe", "jar", "msi"]
system_exts = ["cfg", "dll", "ini", "sys", "tmp"]

current_dir = os.path.dirname(os.path.abspath(__file__))                    # gets current directory
files = [f for f in listdir(current_dir) if isfile(join(current_dir, f))]   # creates list all files in directory but not other directories

for f in files:                                                             # iterating through all files in directory
    file_ext = f.split('.')[len(f.split('.')) - 1].lower()                      # obtaining file extension by splitting by dot in the file name and isolating all text after it
    
    if ".\\" + f == sys.argv[0]:                                                # verifies if the file being iterated over is the script itself
        continue                                                                # in order to not move the script itself, we skip that iteration in the loop
    
    # all statements below pertain to the movement of files to their respective directory depending on extension set
    # template past here is as follows:
    # elif file_ext in set_exts:
    #     shutil.move(f, "Directory\\Subdirectory\\...")
    
    # media
    elif file_ext in image_exts:
        shutil.move(f, "Media\\Images")
    elif file_ext in video_exts:
        shutil.move(f, "Media\\Video")
    elif file_ext in audio_exts:
        shutil.move(f, "Media\\Audio")
    
    # documents
    elif file_ext in text_exts:
        shutil.move(f, "Documents\\Text")
    elif file_ext in presentations_exts:
        shutil.move(f, "Documents\\Presentations")
    elif file_ext in spreadsheets_exts:
        shutil.move(f, "Documents\\Spreadsheets")

    # other
    elif file_ext in compressed_exts:
        shutil.move(f, "Other\\Compressed")
    
    #    code
    elif file_ext in internet_exts:
        shutil.move(f, "Other\\Code\\Internet")
    elif file_ext in python_exts:
        shutil.move(f, "Other\\Code\\Python")
    elif file_ext in csharp_exts:
        shutil.move(f, "Other\\Code\\C#")
    
    elif file_ext in executable_exts:
        shutil.move(f, "Other\\Executable")
    elif file_ext in system_exts:
        shutil.move(f, "Other\\System")

    else:                                                                       # consider all other file extensions as unrecognised
        shutil.move(f, "Uncategorised")                                         # and place them into their own uncategorised folder