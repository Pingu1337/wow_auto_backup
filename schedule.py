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

    """
    Daily Trigger is currently not being used. 
    Keeping this in the code in case it will be needed for upcoming features.
    """

    # Create daily trigger 
    # start_time = datetime.datetime.now() + datetime.timedelta(seconds=5) 
    # start_time = start_time.replace(hour=4, minute=5, second=0, microsecond=0) 
    # TASK_TRIGGER_TYPE  = 2
    # trigger = task_def.Triggers.Create(TASK_TRIGGER_TYPE)
    # trigger.StartBoundary = start_time.isoformat()

    # Create one time trigger
    exec_time = datetime.datetime.now() + datetime.timedelta(seconds=5) 
    TASK_TRIGGER_ONCE  = 1
    trigger = task_def.Triggers.Create(TASK_TRIGGER_ONCE)
    trigger.StartBoundary = exec_time.isoformat()

    # Create on logon trigger
    TASK_TRIGGER_LOGON  = 9
    trigger = task_def.Triggers.Create(TASK_TRIGGER_LOGON)
    trigger.Id = "LogonTriggerId"
    trigger.UserId = os.environ.get('USERNAME') # current user account

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

    # Set RunLevel
    TASK_RUNLEVEL_HIGHEST = 1
    TASK_LOGON_SERVICE_ACCOUNT = 5
    # task_def.Principal.UserID = os.environ.get('USERNAME') 
    task_def.Principal.DisplayName = os.environ.get('USERNAME')
    task_def.Principal.GroupID = "Administrators"
    task_def.Principal.LogonType = TASK_LOGON_SERVICE_ACCOUNT
    task_def.Principal.RunLevel = TASK_RUNLEVEL_HIGHEST # This only works when executed with admin priviliges. 


    # Register task
    # If task already exists, it will be updated
    TASK_CREATE_OR_UPDATE = 6
    root_folder.RegisterTaskDefinition(
        'wow backup',  # Task name
        task_def,
        TASK_CREATE_OR_UPDATE,
        task_def.Principal.UserID,
        None, 
        TASK_LOGON_SERVICE_ACCOUNT
    )
    log.info('task scheduled')


"""
Note: When debugging this file, start CMD as administrator and run "python schedule.py"
this is because the Task Scheduler needs to run backup.exe as administrator
"""

# Uncomment this when debugging
# Schedule_Task()

