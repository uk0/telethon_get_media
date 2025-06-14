## telethon_get_media


### 分享文件相关

* 可以通过 https://github.com/uk0/file_encryption 加密后自释放分享 ：）Safe

### 当前版本

* beta 1.0.0 

#### 功能

* 1.下载 Telegram 历史Media [频道id里面有自己改一下] `main.py`

* 2.实时下载所有频道里面的 Media [自己加入的所有频道] `rt.py`

* 3.下载获取历史与评论区 `his.py` 自己调用download media即可。


#### Env Python 3.6 

   * telethon
   * socks  ` pip install PySocks`
   * asyncio
      

#### 说明

```bash

#1 https://my.telegram.org/auth 输入手机号申请 APIID

#2.直接把自己的API KEY 写入进去 运行程序会让你输入手机号，以及验证码。

#3.第一次需要输入手机号 停止后在启动不需要了就。

#4.纯属无聊。。。。。

```

#### quick start

* 修改配置文件

  > `DELETE_DUP` 现在没有使用

  > 自己创建一个名字=`zh_cn.config`的文件和python脚本同级将以下内容稍作修改写入即可

```config
[message_download]
PIC_DIR=/Users/firshme/Desktop/tmp
DATA_DIR=/Users/firshme/Desktop/tmp
DELETE_DUP=AUTO  
API_ID=100851
API_HASH=464f1f154c34c1f93057f3be
TG_AUTH_FILE_NAME=auto_download
PROXY_ADDR=127.0.0.1
PROXY_PORT=1089
```


* 安装依赖

```bash
pip install telethon
pip install PySocks
```

* 启动

```bash
sudo -u root /opt/miniconda3/bin/python3 main.py

```



* 启动后 console 

```bash
(Press Ctrl+C to stop this)
handler init success
download - /volume5/green_hdd/pysuper/telethon_get_media/data/2022-07-06/XfBFEXrBc18TJL9XjU4zcI
handler init success
download - /volume5/green_hdd/pysuper/telethon_get_media/data/2022-07-06/xIbFtL3zpDjImhujE8IaWX
handler init success
download - /volume5/green_hdd/pysuper/telethon_get_media/data/2022-07-06/DdNU5sqUv3B771R1Yr5aZt
handler init success
download - /volume5/green_hdd/pysuper/telethon_get_media/data/2022-07-06/UYH1CzsvgTQzyuTB2gjlKt
handler init success
download - /volume5/green_hdd/pysuper/telethon_get_media/data/2022-07-06/EcdhKSMTszWYFLtYlMdUGL
handler init success
download - /volume5/green_hdd/pysuper/telethon_get_media/data/2022-07-06/vm6Fbx1o1QR3u2VcpTK9HP
handler init success
download - /volume5/green_hdd/pysuper/telethon_get_media/data/2022-07-06/Wx1wj1BSmQTkdzne5nVehG
handler init success
download - /volume5/green_hdd/pysuper/telethon_get_media/data/2022-07-06/5hyks1pWPE5yt0ACuyyc3g
handler init success
download - /volume5/green_hdd/pysuper/telethon_get_media/data/2022-07-06/5NqBudIhSLFeNGHdphxSPj
handler init success
download - /volume5/green_hdd/pysuper/telethon_get_media/data/2022-07-06/JIDBfFvplFxMA2ruXyaGb5


# 查看文件夹
admin@DS918:/volume5/green_hdd/pysuper/telethon_get_media/data/2022-07-06$ ls -al
total 84920
drwxr-xr-x 2 root  root      4096 Jul  6 23:34 .
drwxr-xr-x 3 admin users     4096 Jul  6 23:26 ..
-rw-r--r-- 1 root  root     22599 Jul  6 23:34 FrB1elMKv84c7pGQr7Dkmi.jpg
-rw-r--r-- 1 root  root  16908288 Jul  6 23:34 UYH1CzsvgTQzyuTB2gjlKt_QMYxxx1271124695396634624-20200612_005838-vid1.mp4
-rw-r--r-- 1 root  root  55574528 Jul  6 23:34 vm6Fbx1o1QR3u2VcpTK9HP_xxxxxxxxxx.mp4
-rw-r--r-- 1 root  root  14417920 Jul  6 23:34 Wx1wj1BSmQTkdzne5nVehG_xxxxxxx.mp4

```


#### show_groupby.sh 使用

```bash
sh show_groupby.sh /path/to/dir

# 例如
admin@DS918:/volume5/green_hdd/pysuper/telethon_get_media$ sh show_groupby.sh /volume5/green_hdd/pysuper/telethon_get_media/data/2022-07-06
         468KiB   11 jpg
         699MiB    7 mp4
```



#### happy continue

* 先给个`✨`直接提问题即可看到就会修改。

#### tools

* 里面都是测试写的统计脚本和工具之前在arm里面跑的 后面整合以后在删除吧。
