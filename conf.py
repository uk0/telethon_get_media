import random
import time


class config:
    def __init__(self):
        # 输出路径
        self._path = "/volumeUSB1/usbshare/py/data_online/"
        self.picture_storage_path = "/volumeUSB1/usbshare/py/data_pic/"

    def getpath(self):
        return self._path

    def get_pic_path(self):
        return self.picture_storage_path

    def get_random_file_name(self):
        H = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
        salt = ''
        for i in range(22):
            salt += random.choice(H)
        t_dir = time.strftime("%Y-%m-%d", time.localtime())
        return salt