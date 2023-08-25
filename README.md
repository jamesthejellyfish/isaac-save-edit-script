# isaac-save-edit-script
A simple python script which can edit save data from the binding of isaac to unlock any secret that you want. Checksum code based off of the afterbirth+ save editor source code: https://moddingofisaac.com/mod/3236/afterbirth-save-editor-v10

to use, simply run the script in a folder with the save data persistentgamedata1.dat in it, and then the save data will be modified to have the new secrets unlocked. By default the script only unlocks the daily run achievements (The Marathon{325}, Dedication{325}, and Broken modem{354}), but any achievement can be unlocked simply by adding its unlock number to the list in the script. Achievement ids can be found on this page: https://bindingofisaacrebirth.fandom.com/wiki/Achievements

As always, be sure to backup any saves before using this tool, as I do not guarantee that your save file will not be corrupted. The tool has been tested on afterbirth, afterbirth+, and repentance and they all worked.

currently this tool only supports unlocking secrets, since that is the only use-case that I needed, but if you know the offset for any other information you want to modify (eden tokens, item touches, bestiary, mom kills, etc.), then the checksum function will still work if you modify that data as well.
