# -*- coding: utf-8 -*-
__author__ = 'idbord'
import time
from config import *
from Ace import Ace


def run():
    if db_backup:
        for i in databases:
            key = Ace.get_mysql_data(i)
            Ace.qiniu_upload("./{}".format(key), key)
    if file_backup:
        for j in file_paths:
            key = Ace.compass_file(j)
            Ace.qiniu_upload("./{}".format(key), key)

if __name__ == "__main__":
    while True:
        print time.strftime('%Y-%m-%d %H:%M:%S')
        run()
        time.sleep(backup_circle)
