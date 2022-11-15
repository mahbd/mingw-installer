import urllib.request
import zipfile
import os

from clint.textui import progress
import requests


url = "https://github.com/mahbd/mingw-installer/releases/download/mingw12.1/mingw64.zip"
path = "mingw.zip"
print("Downloading mingw64.zip")
r = requests.get(url, stream=True)
with open(path, 'wb') as f:
    total_length = int(r.headers.get('content-length'))
    for chunk in progress.bar(r.iter_content(chunk_size=1024), expected_size=(total_length/1024) + 1):
        if chunk:
            f.write(chunk)
            f.flush()
print("Deleting old mingw64 folder")
if os.path.exists("c:\\mingw64"):
    os.system("rmdir /s /q c:\\mingw64")
print("Extracting mingw64.zip")
with zipfile.ZipFile(path, 'r') as zip_ref:
    zip_ref.extractall("C:/")
print("Deleting useless files")
os.remove(path)
print("Setting up environment variables")
os.system('setx PATH "$Env:PATH$;C:\\mingw64\\bin"')
print("Installation complete")
input("Press enter to exit")
