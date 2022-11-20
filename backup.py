import os
import json
import shutil
import logger

# logging = logger.createLogger()

# def rmErr():
#     logging.error('failed to remove tmp dir')

def DoBackup():
    file = open('backup_paths.json')
    paths = json.load(file)
    source = paths[0]["source"]
    dest = paths[0]["dest"]
    addons = paths[0]["addons"]
    wtf = paths[0]["wtf"]

    if not os.path.exists('backups_count.txt'):
        f = open('backups_count.txt', 'w')
        f.write(str(0))

    f = open('backups_count.txt', 'r')
    backups = int(f.read())
    f.close()
    num = int(backups) + 1

    # if number of backups is larger than 9 start over from 1
    if backups > 9:
        num = 1
    f = open('backups_count.txt', 'w')
    f.write(str(num))
    f.close()

    shutil.copytree(addons, source + '/AddOns')
    shutil.copytree(wtf, source + '/WTF')

    if not os.path.isdir(dest):
        os.makedirs(dest)

    print(f'source: {source} \ndest: {dest}')
    file.close()
    shutil.make_archive(f'{dest}/backup_{num}', 'zip', source)
    shutil.rmtree(source)
    backups_list = os.listdir(dest)

    # remove latest tag from previous backup
    for b in backups_list:
        if 'latest' in b:
            os.rename(f'{dest}/{b}', f'{dest}/{b.replace("(latest)", "")}')

    # tag latest backup
    os.rename(f'{dest}/backup_{num}.zip',f'{dest}/backup_{num} (latest).zip')
    # logging.info('successfully backed up interface')
    

DoBackup()