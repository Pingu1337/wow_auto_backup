# wowAutoBackup

_wowAutoBackup is a tool for automatically backup AddOns/WTF directories to avoid losing things like WeakAuras in case of file corruption._

<center>
<img src="assets/icon.svg" alt="drawing" width="300"/>
</center>

## How it works

You set up the path to AddOns and WTF folders aswell as an backup directory.
A task is scheduled in windows Task Scheduler to run when user logs in.

<br>

<br>

---

## Contribute

Feel free to contribute, fork the project and make a pull request!

Here follows some information that might be useful when developing on this project.

### Install pip packages

`pip install -r requirements.txt`

### Working with PyInstaller

> To create Executable files and test the program either use [auto-py-to-exe](https://pypi.org/project/auto-py-to-exe/) or [pyinstaller](https://pypi.org/project/pyinstaller/)

When using pyinstaller use following commands:

- `pyinstaller --onefile -w backup.py`
- `pyinstaller --onedir -w app.py`
- `pyinstaller --onefile -w uninstaller.py`

To debug schedule.py only backup.exe is needed, it is placed in the root directory.
To debug the entire app as an executable run above commands or setup auto-py-to-exe in a similar way _(make sure to move icon.ico to the output directory)_. Then place **backup.exe** and **uninstaller.exe** in the same directory as the app executable.
