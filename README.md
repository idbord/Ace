# Ace
> Ace是一个用来自动备份服务器数据并上传至七牛空间的脚本，最近挺喜欢火拳艾斯的，所以就取名Ace了=_=

Ace is a simple script that is used to backup databases and projects on server, and upload them to qiniu automaticaly.

## 使用说明
#### 获得脚本
```sh
git clone git@github.com:idbord/Ace.git
```
#### 修改配置
```sh
cd Ace
```
进入项目目录，新建config.py，参考config_example.py，修改自己的配置文件

#### 运行脚本
配置完之后，切换到超级用户，
```sh
su
chmod a+x run.sh
# 给脚本以执行权限
./run.sh
# 即可在后台运行该脚本
```
#### 停止脚本
停止脚本，
```sh
ps -ef | grep python 
# 找到PID，kill掉就好
```
## 配置文件说明如下

### 数据库备份配置
```py
db_backup = True
databases = [
    "",
    ""
]
```
### 文件备份配置
```py
file_backup = True
file_paths = [
    "",
    ""
]
```
### 七牛上传配置
#### 填写你的 Access Key 和 Secret Key
```py
access_key = ''
secret_key = ''
```
#### 要上传的空间
```py
bucket_name = ''
```
#### 设置备份周期,秒
```py
backup_circle = 86400
```
#### 注：
***请一定在root用户下执行脚本，***且脚本运行的日志文件路径为/etc/ace.log

脚本的实现很简单，只要熟悉linux的基本使用，再加上七牛的api文档就OK了

不过前提是，你得先有一个已经认证的七牛账号，如果没有点这里[注册](https://portal.qiniu.com/signup?code=3li1yib3yqg5u)吧,强行安利一下=-=

> 最后，关于本Repo，如有建议，不管是思路，还是具体代码，欢迎给我提Issues