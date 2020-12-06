import http
import json
import os


def send_ding_talk_robot(title, bash_line):
    import http.client
    conn = http.client.HTTPSConnection("oapi.dingtalk.com")
    payload = {
        "msgtype": "markdown",
        "markdown": {
            "title": "### {}".format(title),
            "text": "#### msg \n"
                    "```\n"
                    "{}"

                    "```"
                    "\n".format(bash_line)
        },
        "at": {
            "atMobiles": [
                '18515601947'
            ],
            "isAtAll": 'true',
        },
    }
    headers = {
        'content-type': "application/json",
    }
    String_textMsg = json.dumps(payload)
    conn.request("POST", "/robot/send?access_token=dingding token",
                 String_textMsg, headers)
    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))


if __name__ == '__main__':
    disk_table = os.popen(
        "cd /volumeUSB1/usbshare/py/ && du -sh data_online/* | awk -F' ' '{print \"| \" $1 \" | \" $2 \" |\"}'").read()
    # disk_table = os.popen("cd /volumeUSB1/usbshare/py/data_online && du -sh * | awk -F' ' '{ print $1 \" - \" $2 \n }'").read()
    disk_used = "{} \n{} \n ".format("大小（单位：字节 - 文件名) ", disk_table);

    send_ding_talk_robot("硬盘使用量", disk_used)

    send_ding_talk_robot("硬盘使用量", os.popen(
        "df -h | grep -v 'tmpfs' |awk '{print$1 \",\"$2\",\"$3\",\"$4\",\"$5\",\"$6}'").read())

    send_ding_talk_robot("个类型文件磁盘占比", os.popen("cd /volumeUSB1/usbshare/py/data_online && bash show_groupby.sh").read())
