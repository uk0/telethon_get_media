# telethon_get_media




#### 功能

* 1.下载 Telegram 历史Media [频道id里面有自己改一下]

* 2.实时下载所有频道里面的 Media [自己加入的所有频道]


#### Env Python 3.6 

      * telethon
      * socks
      * asyncio
      

#### 说明

```bash

#1 https://my.telegram.org/auth 输入手机号申请 APIID

#2.直接把自己的API KEY 写入进去 运行程序会让你输入手机号，以及验证码。

#3.第一次需要输入手机号 停止后在启动不需要了就。

#4.纯属无聊。。。。。

```


#### Up 


* 添加了其他的脚本 来处理去重和统计（group by count）

* 定时任务脚本

* dingding 提示脚本



#### quick start


```bash
# modify 和 /volumeUSB1/usbshare 类似的目录


# 启动本身的程序
# Control + C 程序会自动杀掉 python 
./watch_dog.sh 
or
nohup ./watch_dog.sh &

# 停止服务 必须要用kill -15 因为用了 trap 捕捉到 15 才会去结束 main 和 task
ps -ef | grep 'watch_dog.sh' | awk '{print$2}'| xargs  kill -15 
```



### up

* 未来几天我会更新新的版本。：）
