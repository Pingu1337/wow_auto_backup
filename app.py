import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import json
import os
import logger
import schedule

logging = logger.createLogger()

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.geometry('400x150')
        self.resizable(0, 0)
        self.title('Login')

        # UI options
        paddings = {'padx': 5, 'pady': 5}
        entry_font = {'font': ('Helvetica', 11)}

        # configure the grid
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=3)

        self.addonsDir = tk.StringVar(value='addons folder')
        self.wtfDir = tk.StringVar(value='wtf Folder')
        self.backupDir = tk.StringVar(value='Backup Folder')
        self.loadDirs()

        # AddOns
        addons_label = ttk.Label(self, text="AddOns Directory:")
        addons_label.grid(column=0, row=0, sticky=tk.W, **paddings)

        self.addons_entry = ttk.Entry(self, textvariable=self.addonsDir , width=40, **entry_font)
        self.addons_entry.grid(column=1, row=0, sticky=tk.E, **paddings)
        addons_button = ttk.Button(self, text="Browse", command=self.setAddonDir)
        addons_button.grid(column=2, row=0, sticky=tk.E, **paddings)

        # WTF
        wtf_label = ttk.Label(self, text="WTF Directory:")
        wtf_label.grid(column=0, row=1, sticky=tk.W, **paddings)

        self.wtf_entry = ttk.Entry(self, textvariable=self.wtfDir, width=40, **entry_font)
        self.wtf_entry.grid(column=1, row=1, sticky=tk.E, **paddings)
        wtf_button = ttk.Button(self, text="Browse", command=self.setWtfDir)
        wtf_button.grid(column=2, row=1, sticky=tk.E, **paddings)
        
        # Backup Dest
        wtf_label = ttk.Label(self, text="Backup Destination:")
        wtf_label.grid(column=0, row=2, sticky=tk.W, **paddings)

        self.wtf_entry = ttk.Entry(self, textvariable=self.backupDir, width=40, **entry_font)
        self.wtf_entry.grid(column=1, row=2, sticky=tk.E, **paddings)
        wtf_button = ttk.Button(self, text="Browse", command=self.setBackupDir)
        wtf_button.grid(column=2, row=2, sticky=tk.E, **paddings)

        # save button
        save_button = ttk.Button(self, text="Save", command=self.saveDir)
        save_button.grid(column=2, row=3, sticky=tk.E, **paddings)

        # configure style
        self.style = ttk.Style(self)
        self.style.configure('TLabel', font=('Helvetica', 11))
        self.style.configure('TButton', font=('Helvetica', 11))

    def setAddonDir(self):
        filename = filedialog.askdirectory(title = "Select AddOns Directory")
        self.addonsDir.set(filename) 
    def setWtfDir(self):
        filename = filedialog.askdirectory(title = "Select WTF Directory")
        self.wtfDir.set(filename) 
    def setBackupDir(self):
        filename = filedialog.askdirectory(title = "Select WTF Directory")
        self.backupDir.set(filename) 

    def saveDir(self):
        addons = self.addonsDir.get()
        wtf = self.wtfDir.get()
        backup = self.backupDir.get()

        if not 'AddOns' in addons:
            tk.messagebox.showerror(title='Addon Directory Name Error', message='Please select the "AddOns" folder')
            return
        if not 'WTF' in wtf:
            tk.messagebox.showerror(title='WTF Directory Name Error', message='Please select the "WTF" folder')
            return
        if backup == 'Backup Folder':
            tk.messagebox.showerror(title='Backup Directory Name Error', message='Please select a backup destination')
            return

        paths_json = [{
            "addons": addons,
            "wtf": wtf,
            "source": backup + '/tmp',
            "dest": backup
            }]

        f = open('backup_paths.json', 'w')
        f.write(json.dumps(paths_json, indent=4))
        logging.info('paths saved to "backup_paths.json"')
        print('paths saved to "backup_paths.json"')
        schedule.Schedule_Task()
        self.call(app.destroy())
        

    def loadDirs(self):
        if not os.path.exists('backup_paths.json'):
            logging.info('backup_paths.json does not exist, not loading saved paths')
            return
        f = open('backup_paths.json')
        paths = json.load(f)
        self.addonsDir.set(paths[0]["addons"])
        self.wtfDir.set(paths[0]["wtf"])
        self.backupDir.set(paths[0]["dest"])
        logging.info('saved paths loaded from "backup_paths.json"')


if __name__ == "__main__":
    app = App()
    app.mainloop()