# -*- coding: utf-8 -*-
__author__ = 'idbord'

import subprocess
import time
from qiniu import Auth, put_file, etag
from config import access_key, secret_key, bucket_name


class Ace:
    def __init__(self):
        pass

    @classmethod
    def compass_file(cls, path):
        filename = path.split('/')[-1]
        timestamp = time.strftime("%Y%m%d")
        target = "{}_{}.tar.gz".format(filename, timestamp)
        command = "tar -zcvf {} {}".format(target, path)
        subprocess.call(command, shell=True)
        return target

    @classmethod
    def get_mysql_data(cls, db, path=None):
        timestamp = time.strftime("%Y%m%d")
        path = path is None and "/var/lib/mysql/" or path
        target = "mysql_{}_{}.tar.gz".format(db, timestamp)
        command = "tar -zcvf {} {}{}".format(target, path, db)
        subprocess.call(command, shell=True)
        return target

    @classmethod
    def qiniu_upload(cls, localfile, key):
        # 构建鉴权对象
        q = Auth(access_key, secret_key)

        # 生成上传 Token，可以指定过期时间等
        token = q.upload_token(bucket_name, key, 3600)

        ret, info = put_file(token, key, localfile)
        print(info)
        assert ret['key'] == key
        assert ret['hash'] == etag(localfile)