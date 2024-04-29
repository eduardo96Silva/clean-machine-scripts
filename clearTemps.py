import os
import shutil

def limpar_pasta(pasta):
    for root, dirs, files in os.walk(pasta, topdown=False):
        for file in files:
            try:
                os.remove(os.path.join(root, file))
            except (PermissionError, OSError):
                continue
        for dir in dirs:
            try:
                shutil.rmtree(os.path.join(root, dir))
            except (PermissionError, OSError):
                continue

paths = [
    "C:/Windows/Temp",
    "C:/Users/eduar/AppData/Local/Temp"
]

for path in paths:
    limpar_pasta(path)