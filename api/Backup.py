"""
=================================================
@Project -> File    ：Share_And_Talk -> Backup.py
@IDE                ：PyCharm
@Author             ：Skyler Sun
@Date               ：2023/6/22 9:32
@用途               ：备份数据库
@email              ：3385213313@qq.com
==================================================
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
