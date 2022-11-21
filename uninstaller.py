import win32com.client

scheduler = win32com.client.Dispatch('Schedule.Service')
scheduler.Connect()
root_folder = scheduler.GetFolder('\\')

root_folder.DeleteTask('wow backup',0)