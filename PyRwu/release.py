import datetime
import shutil
import os
import os.path
import urllib.request

PYTHON="python-3.9.10"
PYTHON_URL="https://www.python.org/ftp/python/3.9.10/python-3.9.10-embed-amd64.zip"

BUILD_DIR = os.path.join("..", "release", "build")
PROJECTNAME = "PyRwu"
RELEASE_FILE = os.path.join("..", "release", PROJECTNAME + "-" + datetime.datetime.strftime(datetime.datetime.now(), "%Y%m%d"))
EXE_DIR = os.path.join("..", "PyRwuExe", "bin", "Release", "net6.0-windows")
EXE_DIR_EXTENSIONS = [".exe",".dll",".runtimeconfig.json"]
SOURCE_FILES = []
for pathname, dirnames, filenames in os.walk("."):
    if "env" in pathname:
        continue
    if "tests" in pathname:
        continue
    for filename in filenames:
        if not filename.endswith(".py"):
            continue
        if filename != "release.py":
            SOURCE_FILES.append(os.path.join(pathname, filename))

print(SOURCE_FILES)
README=os.path.join("..","README.md")
LICENSE=os.path.join("..","LICENSE")

os.makedirs(BUILD_DIR, exist_ok=True)
os.makedirs(os.path.join(BUILD_DIR, "src"), exist_ok=True)

exe_dir_files = os.listdir(EXE_DIR)
for file in exe_dir_files:
    for extensions in EXE_DIR_EXTENSIONS:
        if file.endswith(extensions):
            shutil.copy(os.path.join(EXE_DIR, file),os.path.join(BUILD_DIR, file))
            break
            
for file in SOURCE_FILES:
    os.makedirs(os.path.join(BUILD_DIR, "src", os.path.dirname(file)), exist_ok=True)
    shutil.copy(file, os.path.join(BUILD_DIR, "src", file))

if not os.path.isdir(os.path.join(BUILD_DIR,PYTHON)):
    urllib.request.urlretrieve(PYTHON_URL, os.path.join(BUILD_DIR,PYTHON+".zip"))
    shutil.unpack_archive(os.path.join(BUILD_DIR,PYTHON+".zip"),os.path.join(BUILD_DIR,PYTHON))
    os.remove(os.path.join(BUILD_DIR,PYTHON+".zip"))

if os.path.exists(LICENSE):
    shutil.copy(LICENSE, os.path.join(BUILD_DIR, "license.txt"))
if os.path.exists(README):
    shutil.copy(README, os.path.join(BUILD_DIR, "readme.txt"))

shutil.make_archive(RELEASE_FILE, format="zip", root_dir=BUILD_DIR)