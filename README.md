# Temporary Folder
A nifty folder that wipes every hours (with some extra features)

### Installation
Clone the repo and run setup.py, it'll ask you where you would like your temporary folder to live. By default, the folder will be put in the home directory.
Then, a cron job will be added to run delete.py every hour, so don't delete or move delete.py or prefs.json, or it'll break.

### Usage
Pretty simple, just place items you intend to use once in the folder, use them, and watch them disappear on the hour.

But sometimes, you need your files to last a bit longer than that, so if you pass the -d argument, and a number, it'll hold off on deleting for that many hours. 
So `-d 1` will delay deletion for an hour.

To override all delays, use the -a argument to delete everything.

To remove a delay, use the -f argument

### Deactivation
Use the -r argument to uninstall the cron setup. This will stop the folder from deleting.
