import os
import json
import shutil
import logger

logging = logger.createLogger()


def DoBackup():
    file = open('backup_paths.json')
    paths = json.load(file)
    source = paths[0]["source"]
    dest = paths[0]["dest"]
    logging.warn('Reactor 4 is unstable')
    logging.critical('MELTDOWN IN REACTOR 4')
    # small source when debugging
    source = 'mock_backup/small_from'
    print(f'source: {source} \ndest: {dest}')
    file.close()
    shutil.make_archive(f'{dest}/backup', 'zip', source, logger=logging)
    


DoBackup()