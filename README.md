# isaac-save-edit-script
A script build in python for editing save files for the binding of isaac repentance.
This project was heavily inspired and relies on the source code for the afterbirth save editor found here:
https://moddingofisaac.com/mod/3236/afterbirth-save-editor-v10

THIS PROJECT HAS NOT BEEN TESTED ON THE ONLINE BETA, USE AT YOUR OWN RISK!!!

As always, be sure to backup any saves before using this tool, as I do not guarantee that your save file will not be corrupted.

<img width="681" alt="image" src="https://github.com/jamesthejellyfish/isaac-save-edit-script/assets/11594527/23bfc7f2-fa00-40c4-849d-b702f9989f4e">

# Running

To run, either download the latest release of the graphical version found here: https://github.com/jamesthejellyfish/isaac-save-edit-script/releases/
then simply open the exe file.

## Opening your save file
Select the "Open Isaac Save File" menu item to locate your save file. By default, you will be navigated to your steam userdata folder. To find your save file, go to 
```
{steam_installation_path}\Steam\userdata\{steamid}\250900\remote\rep_persistengamedata{1|2|3}.dat
```
where {1|2|3} is either 1,2, or 3 depending on the save file you want to edit.
For non-steam users, your save file location is generally in Documents\My Games\Binding of Isaac Repentance\persistentgamedata{1|2|3}.dat

## Editing save data
once you have imported your save data, the fields should be populated with the current information that is within that save. you should then be able to easily edit it according to your liking.
NOTE: There is no "save" button to commit your changes to a save file, once you make a change it changes the file in real time. **Once again, make sure to backup any saves before using this tool**.
### Editing Entries
The current entries that you can edit are win streak, eden tokens, donation machine coins, and greed machine coins. To edit them, simply replace the number shown with the number desired and press the enter key.
<img width="681" alt="image" src="https://github.com/jamesthejellyfish/isaac-save-edit-script/assets/11594527/c25c1d9f-bd72-4cee-984a-065ac0101ea3">

### Editing Completion Marks
in the "Completion Marks" Tab, you will be able to see the completion marks of all characters, and edit them. to edit a specific character's completion page, select them from the drop-down menu, and then check off the completion marks that you want them to have unlocked. You can also press the "unlock All" button to unlock all completion marks for a specific character, or the "unlock All All Chars" button to unlock every completion mark for every character. NOTE: The GUI version of this script only supports adding hard mode completion marks to characters. However, it is possible to add normal mode completion marks via the manual script. If you need a normal completion mark, see "Manual configuration".

<img width="685" alt="image" src="https://github.com/jamesthejellyfish/isaac-save-edit-script/assets/11594527/8dcb02f3-1ec3-4a8b-987e-57a91906e1c2">
<img width="682" alt="image" src="https://github.com/jamesthejellyfish/isaac-save-edit-script/assets/11594527/1075a5d4-1b2f-413b-afe7-2963b3607f3b">

### Editing Secrets
in the "Secrets" Tab, you can manually unlock or disable secrets one at a time by clicking the check box. In the "misc" tab, pressing the "Unlock All" secrets button will unlock all secrets. Note that this tool does not support the online beta, so unlocking online beta secrets is not supported. However, it is possible to do this using the manual script. For more info, see "Manual Configuration".

<img width="683" alt="image" src="https://github.com/jamesthejellyfish/isaac-save-edit-script/assets/11594527/80bea766-f3b2-4140-a3fe-fce56e7ca02a">



### Editing Items:
in the "Items" Tab, you can manually select seen items one at a time by clicking the check box. In the "misc" tab, pressing the "Unlock All" items button will unlock all items.

<img width="685" alt="image" src="https://github.com/jamesthejellyfish/isaac-save-edit-script/assets/11594527/0e8b3e1b-9e3f-4182-af57-86d203c4de6c">



### Editing Challenges:
in the "Challenges" Tab, you can manually complete challenges one at a time by clicking the check box. In the "misc" tab, pressing the "Unlock All" challenges button will complete all challenges.

<img width="682" alt="image" src="https://github.com/jamesthejellyfish/isaac-save-edit-script/assets/11594527/bbe8acf2-fa2b-4314-8501-b461b23dbf32">


# Manual configuration
This section is for advanced users who want to modify the functionality of the script, or perform actions that aren't currently supported in the graphical version. This guide assumes you have already set up a python environment and are familiar with entering console commands. For more information on how to setup python, visit https://docs.python.org/3/using/index.html
## Dependencies
the script file script.py does not have any dependencies, but the gui depends on the tkinter module and the ttkwidgets module. These can be installed using the following commands:
```bash
pip install tkinter
pip install ttkwidgets
```

## more
the base script.py file contains functions that should illustrate how to edit your file. To use the script, change the 'filename' variable to the filename of the savedata you want to edit, and then you can edit
the main section like so:
```py
if __name__ == "__main__":
  offset = 0x10
  with open(filename, "rb") as file:
      data = file.read()
      length = len(data) - offset - 4
      checksum = calcAfterbirthChecksum(data, offset, length).to_bytes(5, 'little', signed=True)[:4]
      print(checksum)
      old_checksum = data[offset + length:]    
  #your code goes here
  ...
```
Within the main section are also some examples of things you might want to do, such as edit a different secret, or add a normal completion mark.
It is important to note that the functions do not edit data in-place, so if you actually want to change the data, you will need to re-assign the "data" variable to the output of the function.


# More information
releases are made using the command:
```bash
pyinstaller --onefile -w gui.py
```
and require the pyinstaller module to be installed.
