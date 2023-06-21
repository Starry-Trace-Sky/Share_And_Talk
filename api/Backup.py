"""

This is a script used for auto backuping django database

rate: one time per day
    
"""
import subprocess
from time import strftime

import pysnooper


class Backuper:
    def __backupDB(self):
        """Backup share and talk database"""
        # Export database as backup.json
        date = strftime('%Y_%m_%d_%H_%M_%S')
        filepath = f'backup/backup_{date}.json'
        args = ['py', '-Xutf8', 'manage.py', 'dumpdata', '-o', 
                filepath]
        # py -Xutf8 manage.py dumpdata -o backup_2023_06_06.json
        subprocess.check_call(args, creationflags=subprocess.CREATE_NO_WINDOW)

    @pysnooper.snoop('info.log')
    def backup(self):
        """Main backup function"""
        try:
            self.__backupDB()
            return 'ok'
        except Exception as e:
            return str(e)
