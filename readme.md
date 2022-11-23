# wowAutoBackup

_wowAutoBackup is a tool used to automatically backup AddOns/WTF directories to avoid losing things like WeakAuras in case of file corruption._

_World of Warcraft UI Backup Tool_
<img src="assets/icon.svg" alt="drawing" width="300"/>

## How it works

### **Setup**

When you start the application the first time you will be prompted to set the path to your WTF and AddOns folder aswell as a destination folder where the backups will be saved.
Once the paths are set up everything will be handled automatically.
A backup is done every time you login to windows.

### **Backups**

A total of 10 backups are stored in the destination of your choice, when 10 backups have been done the first backup is replaced. The latest backup is tagged with _`(latest)`_.
To reduce size backups are compressed to zip archives. When tested on my own game files i was able to reduce my `800MB` UI to `211MB`.

### **Restore to a backup**

To restore to a backup all you need to do is unzip the `backup_<number>.zip` file and replace the WTF and Addons folder located at `World of Warcraft\_retail_\WTF` and `World of Warcraft\_retail_\Interface\AddOns` with the ones contained in `backup_<number>.zip`

<br>

# Download

### 🚧 The application is currently being developed and is undergoing a testing phase.

### **Use it at your own risk!**

<details>
  <summary><b>I understand the risks</b></summary>
  
  **[⚠️Download Anyway⚠️](https://github.com/Pingu1337/wow_auto_backup/raw/master/release/wowAutoBackup1.0-setup.exe)**
  
</details>

<br>

<br>

## License

**[MIT](https://github.com/pingu1337/wow_auto_backup/blob/master/license)**

<br>

# Contribute 🔧

Feel free to contribute, fork the project and make a pull request!

**⬇️Below is some information that may be useful as you work on this project.⬇️**

### Install pip packages

`pip install -r requirements.txt`

### Working with PyInstaller

> To create Executable files and test the program either use [auto-py-to-exe](https://pypi.org/project/auto-py-to-exe/) or [pyinstaller](https://pypi.org/project/pyinstaller/)

When using pyinstaller use following commands:

- `pyinstaller --onefile -w backup.py`
- `pyinstaller --onedir -w app.py`
- `pyinstaller --onefile -w uninstaller.py`

To debug `schedule.py` only backup.exe is needed, it is placed in the root directory.
To debug the entire app as an executable run above commands or setup auto-py-to-exe in a similar way _(make sure to move icon.ico to the output directory)_. Then place **backup.exe** and **uninstaller.exe** in the same directory as the app executable.
