import datetime
import win32com.client
import os
import logger

log = logger.createLogger()

def Schedule_Task():
    scheduler = win32com.client.Dispatch('Schedule.Service')
    scheduler.Connect()
    work_dir = os.getcwd()
    root_folder = scheduler.GetFolder('\\') 
    task_def = scheduler.NewTask(0)

    # Create daily trigger 
    start_time = datetime.datetime.now() + datetime.timedelta(seconds=5) 
    start_time = start_time.replace(hour=00, minute=00, second=1, microsecond=0)
    TASK_TRIGGER_TYPE  = 2
    trigger = task_def.Triggers.Create(TASK_TRIGGER_TYPE)
    trigger.StartBoundary = start_time.isoformat()

    # Create one time trigger
    exec_time = datetime.datetime.now() + datetime.timedelta(seconds=5) 
    TASK_TRIGGER_ONCE  = 1
    trigger = task_def.Triggers.Create(TASK_TRIGGER_ONCE)
    trigger.StartBoundary = exec_time.isoformat()

    # Create action
    TASK_ACTION_EXEC = 0
    action = task_def.Actions.Create(TASK_ACTION_EXEC)
    action.ID = 'BACKUP WOW INTERFACE'
    action.WorkingDirectory = work_dir
    action.Path = os.getcwd() + "\\backup.exe"


    # Set parameters
    task_def.RegistrationInfo.Description = 'Interface Backup for World of Warcraft'
    task_def.Settings.Enabled = True
    task_def.Settings.StopIfGoingOnBatteries = False
    task_def.Settings.StartWhenAvailable = True # <- credit: https://github.com/mathisson

    # Register task
    # If task already exists, it will be updated
    TASK_CREATE_OR_UPDATE = 6
    TASK_LOGON_INTERACTIVE_TOKEN = 3
    root_folder.RegisterTaskDefinition(
        'wow backup',  # Task name
        task_def,
        TASK_CREATE_OR_UPDATE,
        '',  # No user
        '',  # No password
        TASK_LOGON_INTERACTIVE_TOKEN)
    log.info('task scheduled')


# use this when debugging
# Schedule_Task()



