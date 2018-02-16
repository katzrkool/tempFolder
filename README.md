# Temporary Folder
A nifty folder that wipes every hours (with some extra features)

### Installation
Clone the repo and run setup.py, it'll ask you where you would like your temporary folder to live. By default, the folder will be put in the home directory.
Then, a cron job will be added to run delete.py every hour, so don't delete or move delete.py or prefs.json, or it'll break.

### Usage
Pretty simple, just place items you intend to use once in the folder, use them, and watch them disappear on the hour.

But sometimes, you need your files to last a bit longer than that, so if you pass the -d argument, and a number, it'll hold off on deleting for that many hours. 
So `-d 1` will delay deletion for an hour.

To delay single files, name the files a time in the future like `4pm.txt` or `2018-03-02` and they won't be deleted until then.
Most time formats should be picked up, for more detail on what is and isn't accepted, check out the (maya library)[https://github.com/kennethreitz/maya]

To override all delays, use the -a argument to delete everything.

To remove a delay, use the -f argument

### Deactivation
If you don't use crontab, or don't know what it is, you are most likely safe using the `crontab -r` command to remove the cron job, which will stop the deletion permanently.
If you do use crontab, just remove it from the cron job list.