import os
from pathlib import Path
import platform
import subprocess
import json

global currentDir
currentDir = os.path.dirname(os.path.realpath(__file__))

def setup():
    print("Welcome to Temp Folder setup.")
    nameData = chooseName()

    with open(os.path.dirname(os.path.realpath(__file__))+"/prefs.json", "w")as f:
        json.dump({"folder": nameData, "time": "0"}, f)

    if platform.system() is "Darwin" or "Linux":
        unixInit(str(Path.home())+"/"+nameData)

def tempTaken(folder):
    if not os.path.isdir(str(Path.home()) + "/{}".format(folder)):
        return True
    else:
        return False


def writeTo():
    global currentDir
    # because i'm too lazy to figure out subprocess
    return '''
#write out current crontab
crontab -l > mycron
#echo new cron into cron file
echo "0 * * * * python3 {}/delete.py" >> mycron
#install new cron file
crontab mycron
rm mycron
    '''.format(currentDir)

def chooseName():
    folderName = input("What would you like your temporary folder to be called?\t")
    if folderName is not tempTaken(folderName):
        if input("{} already exists. Overwrite? (y\\n)".format(folderName)) is "y":
            return folderName
        else:
            return chooseName()
    return folderName

def unixInit(path):
    global currentDir
    # make folder
    try:
        os.makedirs(path)
    except FileExistsError:
        pass

    with open("{}/setup.sh".format(currentDir), "w") as f:
        f.write(writeTo())

    subprocess.call(["chmod", "+x", "{}/setup.sh".format(currentDir)])

    subprocess.call("{}/setup.sh".format(currentDir), shell=True, stdout=subprocess.DEVNULL)
    subprocess.call("rm {}/setup.sh".format(currentDir), shell=True)
setup()
