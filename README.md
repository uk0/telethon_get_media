# telethon_get_media




#### 功能

* 1.下载 Telegram 历史Media [频道id里面有自己改一下]

* 2.实时下载所有频道里面的 Media [自己加入的所有频道]


#### Env Python 3.6 

      * telethon
      * socks
      * asyncio
      
      
#### Start nohup 启动即可.

```bash
root     25086     1  0 Oct11 ?        00:00:00 python main.py
root     25091 25086  0 Oct11 ?        00:00:00 [python] <defunct>
root     25093 25086  0 Oct11 ?        00:00:00 [python] <defunct>
root     25094 25086  0 Oct11 ?        00:06:12 [python] <defunct>
root     25095 25086  0 Oct11 ?        00:00:00 [python] <defunct>
root     25097 25086  0 Oct11 ?        00:00:00 [python] <defunct>
root     25098 25086  0 Oct11 ?        00:00:00 [python] <defunct>
root     25101 25086  0 Oct11 ?        00:00:00 [python] <defunct>
root     25102 25086  0 Oct11 ?        00:00:00 [python] <defunct>
root     25104 25086 51 Oct11 ?        3-23:35:57 python main.py
```


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