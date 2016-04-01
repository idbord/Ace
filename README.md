# Ace
> 最近挺喜欢火拳艾斯的，所以就取名Ace了=_=

Ace is a simple script that is used to backup databases and projects on server, and upload them to qiniu automaticaly.

## 使用说明
#### 获得脚本
git clone git@github.com:idbord/Ace.git

#### 修改配置
cd Ace 进入项目目录，新建config.py，参考config_example.py，修改自己的配置文件

#### 运行脚本
修改完之后，切换到超级用户，./run.sh，即可在后台运行该脚本

#### 停止脚本
停止脚本，ps -ef | grep python，找到PID，kill掉就好

## 配置文件说明如下

### 数据库备份配置
db_backup = True
databases = [
    "",
    ""
]

### 文件备份配置
file_backup = True
file_paths = [
    "",
    ""
]

### 七牛上传配置
#### 填写你的 Access Key 和 Secret Key
access_key = ''
secret_key = ''

#### 要上传的空间
bucket_name = ''

#### 设置备份周期,秒
backup_circle = 86400

#### 注：
脚本的实现很简单，只要熟悉linux的基本使用，再加上七牛的api文档就OK了

不过前提是，你得先有一个已经认证的七牛账号，如果没有点这里[注册](https://portal.qiniu.com/signup?code=3li1yib3yqg5u)吧,强行安利一下=-=

> 最后，关于本Repo，如有建议，不管是思路，还是具体代码，欢迎给我提Issues