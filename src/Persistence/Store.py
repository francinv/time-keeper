import json
import os
from Persistence.Deserialize import deserializeFile
from Persistence.Serialize import serializeTimeKeeper
from pathlib import Path


def openFile():
    path_dir = Path.home() / 'TimeKeeper'
    path_to_file = path_dir / 'time-keeper-data.json'
    if not Path.is_dir(path_dir):
        os.mkdir(Path.home() / 'TimeKeeper')
    if Path.is_file(path_to_file):
        with open(path_to_file) as json_file:
            data = json.load(json_file)
            return data['groups']
    else :
        dict = {
            "groups": [],
        }
        with open(path_to_file, 'w') as outfile:
            json.dump(dict, outfile, indent=4)

def loadTimeKeeper():
    groups = openFile()
    return deserializeFile(groups)

def saveTimeKeeper(timeKeeper):
    path = Path.home() / 'TimeKeeper/time-keeper-data.json'
    with open(path, 'w') as outfile:
        json.dump(serializeTimeKeeper(timeKeeper), outfile, indent=4)