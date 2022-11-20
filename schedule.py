import datetime
import win32com.client
import os
import logger

log = logger.createLogger()

def Schedule_Task():
    scheduler = win32com.client.Dispatch('Schedule.Service')
    scheduler.Connect()
    # root_folder = scheduler.GetFolder('\\')
    root_folder = os.getcwd() # <- if this dont work, this where i pick up
    task_def = scheduler.NewTask(0)

    # Create trigger
    start_time = datetime.datetime.now() + datetime.timedelta(seconds=5)
    TASK_TRIGGER_TIME = 1
    trigger = task_def.Triggers.Create(TASK_TRIGGER_TIME)
    trigger.StartBoundary = start_time.isoformat()

    # Create action
    TASK_ACTION_EXEC = 0
    action = task_def.Actions.Create(TASK_ACTION_EXEC)
    action.ID = 'DO NOTHING'
    action.Path = os.getcwd() + "/backup.exe"

    # action.Arguments = f'/k echo test'

    # Set parameters
    task_def.RegistrationInfo.Description = 'Test Task'
    task_def.Settings.Enabled = True
    task_def.Settings.StopIfGoingOnBatteries = False

    # Register task
    # If task already exists, it will be updated
    TASK_CREATE_OR_UPDATE = 6
    TASK_LOGON_NONE = 0
    root_folder.RegisterTaskDefinition(
        'Test Task',  # Task name
        task_def,
        TASK_CREATE_OR_UPDATE,
        '',  # No user
        '',  # No password
        TASK_LOGON_NONE)
    log.info('task scheduled')