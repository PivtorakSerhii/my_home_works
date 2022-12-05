import argparse
import sys
import os
from pathlib import Path
from shutil import move
import shutil
import re

folder_for_scan = None
FOLDERS = []
CYRILLIC_SYMBOLS = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ'
TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
               "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "u", "ja", "je", "ji", "g")

TRANS = {}
for c, l in zip(CYRILLIC_SYMBOLS, TRANSLATION):
    TRANS[ord(c)] = l
    TRANS[ord(c.upper())] = l.upper()

def base_folders(path: str):
    bs_fld = ["images", "documents", "audio", "video", "archives"]
    for i in bs_fld:
        fold = path / i
        fold.mkdir(exist_ok=True, parents=True)

def scan(folder: Path) -> None:
    for item in folder.iterdir():
        if item.is_dir():
            if item.name not in ("images", "documents", "audio", "video", "archives"):
                FOLDERS.append(item)
                scan(item)
            continue
        else:
            move_file(item)

def move_file(file: Path) -> None:
    global folder_for_scan
    ext = ((file.suffix)[1:]).lower()
    if ext in ("ipeg", "png", "jpg", "svg"):
        new_path = folder_for_scan / "images"
        move(file, new_path / normalize(file.name))
    elif ext in ("doc", "docx", "txt", "pdf", "xlsx", "pptx"):
        new_path = folder_for_scan / "documents"
        move(file, new_path / normalize(file.name))
    elif ext in ("mp3", "ogg", "wav", "amr"):
        new_path = folder_for_scan / "audio"
        move(file, new_path / normalize(file.name))
    elif ext in ("avi", "mp4", "mov", "mkv"):
        new_path = folder_for_scan / "video"
        move(file, new_path / normalize(file.name))
    elif ext in ("zip", "gz", "tar"):
        new_path = folder_for_scan / "archives"
        filename = file.name.replace(file.suffix, "")
        fold = folder_for_scan / "archives" / filename
        shutil.unpack_archive(str(file.resolve()), str(fold.resolve()))
        os.remove(file)

def rem_fold(lst_folders):
    for i in lst_folders:
        if not os.listdir(i):
            Path(i).rmdir()

def normalize(name_file):
    ext = re.findall(r"[.][a-zA-Z0-9]{1,10}", name_file)
    name_file = re.sub(ext[0],"", name_file)
    name_file = name_file.translate(TRANS)
    name_file = re.sub(r'\W', '_', name_file) + ext[0]
    return name_file  

def srt_folder(folder_for_scan):
    base_folders(folder_for_scan)
    scan(folder_for_scan)
    rem_fold(FOLDERS)

def start():
    try:
        global folder_for_scan
        folder_for_scan = Path(sys.argv[1])
        srt_folder(folder_for_scan)
    except IndexError:
        print("Вы не ввели путь к папке") 