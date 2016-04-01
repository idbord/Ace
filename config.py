# -*- coding: utf-8 -*-
__author__ = 'idbord'

# 数据库备份配置
db_backup = True
databases = [
    "hilaw",
    "ebook"
]

# 文件备份配置
file_backup = True
file_paths = [
    "/home/idbord/Pictures"
]

# 七牛上传配置
# 需要填写你的 Access Key 和 Secret Key
access_key = 'l__D-PP23Eyd-_L9F83_iURF4gp7-tqkeJCYXWZG'
secret_key = 'FsdLbm7lEdLhg7DS4QX07oyvhP4h9_1ohJumdCm5'

# 要上传的空间
bucket_name = 'fxy-backup'

# 设置备份周期,秒
backup_circle = 86400