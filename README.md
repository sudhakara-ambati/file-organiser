# File Organiser - Never have an unorganised folder again.
A script that automatically organises files in a folder by file type.

Originally designed for the "Downloads" folder, which is very commonly cluttered, but is entirely folder agnostic.

## Requisites
- Windows
- Python 3.x

## Usage
- Click the green "Clone or download" button and then "Download ZIP".
- Then extract the ZIP file.
- Copy/move the folder structure and the `organise_dir.py` file into the folder you wish to organise.
  - Be carful not to overwrite folders of the same name you may currently have in the directory you wish to organise.
  - If this is the case, move all files into the root of the directory you wish to organise, or keep them in separately named folders to the ones in this program's structure.
- Run the python script in the root directory, by doing `python organise_dir.py` or alternative.
- The script will then organise all the files into their respective folders based on their extension.
- The script will not move itself.

## Customisation
- The script is very easily modifiable.
- You can add, change or remove file types that are organised by changing the `set_exts` list definitions at the top of the file.
- You can also change the directory structure by modifying the statements in the `elif`s.

## TODO
- Currently requires manual creation of directory structure, otherwise creates blank file and does not work.
  - Implement automatically created directory structure using `try`/`except`, `if` statement, and `os.mkdir()`.
  - This will also mitigate the need for the `.keep` files in the directory that we currently need for Git to function correctly.
- Currently only organises files (and not other directories) in root directory that script is placed in.
  - Implement option/flag eg `python file_organiser.py -r` to allow organisation of files within directories recursively.
- Method of retrieving file type is intended to work with Windows filesystems and may work on macOS, but does not extend to Linux or other UNIX based systems.
  - Find alternative cross-platform implementation.
- Using continue to break out of loop to stop script moving itself may not be the most efficient.
  - Find more efficient alternative implementation.

## Default folder structure and extensions
### Media
#### Images
- bmp
- gif
- jpeg
- jpg
- png
- svg
- tif
- tiff
- ico

#### Video
- avi
- flv
- m4v
- mkv
- mov
- mp4
- mpg
- mpeg
- wmv

#### Audio
- mp3
- wav

### Documents
#### Text
- pdf
- txt
- doc
- docx

#### Presentations
- ppt
- pptx
- pps

#### Spreadsheets
- xls
- xlsm
- xlsx

### Other
#### Compressed
- rar
- zip

#### Code
##### Internet
- html
- css
- js
- php
##### Python
- py

##### C#
- cs

#### Executable
- bat
- exe
- jar
- msi

#### System
- cfg
- dll
- ini
- sys
- tmp
