import os
import json
import maya
from datetime import datetime, timedelta
import argparse
global data
import subprocess
import sys
global currentDir
currentDir = os.path.dirname(os.path.realpath(__file__))


with open(currentDir+"/prefs.json","r") as f:
    data = json.load(f)
    folder = data["folder"]


home = os.path.expanduser("~")
folder = home+"/"+folder

def check(name):
    try:
        date = maya.parse(name.split(".")[0]).datetime(naive=True)
        if date > datetime.now():
            return True
        else:
            return False
    except:
        return False

def delete(all):
    with open(currentDir+"/prefs.json", "r") as f:
        data = json.load(f)
    if maya.parse(data["time"]).datetime(naive=True) <= datetime.now() or all:
        for root, dirs, files in os.walk(folder):
            if len(os.listdir(root)) == 0 and root is not folder:
                os.rmdir(root)
            for name in files:
                if check(name) is False or all is True:
                    try:
                        os.remove(os.path.join(root, name))
                        if len(os.listdir(root)) == 0 and root is not folder:
                            os.rmdir(root)
                    except FileNotFoundError:
                        pass
    folderSweep()

def folderSweep():
    again = True
    while again:
        again = False
        for root, dirs, files in os.walk(folder):
            if len(os.listdir(root)) == 0 and root is not folder:
                again = True
                os.rmdir(root)

def uninstall():
    cronStr = '''0 * * * * {} {}/delete.py'''.format(sys.executable, currentDir)
    crontab = subprocess.Popen(["crontab", "-l"],
                             stdout=subprocess.PIPE).stdout.read().decode().strip()
    crontab = crontab.replace(cronStr,"")
    with open("mycron","w") as f:
        f.write(crontab)
    subprocess.call(["crontab","mycron"])
    os.remove("mycron")

def fix():
    global data
    data.update({"time":"0"})
    with open(currentDir+"/prefs.json", "w") as f:
        json.dump(data, f)

def delay(hours):
    global data
    global currentDir
    time = datetime.now() + timedelta(hours=hours)
    with open(currentDir+"/prefs.json", "w") as f:
        data.update({"time":time.isoformat()})
        json.dump(data, f)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", type=int, default=0, help="Delays the temporary folder wipe for x hours.")
    parser.add_argument("-a", action="store_true")
    parser.add_argument("-f", action="store_true")
    parser.add_argument("-r", action="store_true", help="Uninstall tempFolder")
    args = parser.parse_args()

    if args.f:
        fix()
    elif args.r:
        uninstall()
    elif args.a:
        delete(True)
    elif args.d == 0:
        delete(False)
    else:
        delay(args.d)
