import random
import time


class config:
    def __init__(self):
        from configparser import ConfigParser

        config = ConfigParser()
        # 传入读取文件的地址，encoding文件编码格式，中文必须
        config.read('zh_cn.config', encoding='UTF-8')
        # 输出路径
        self._path = config['message_download']['DATA_DIR']
        self.picture_storage_path = config['message_download']['PIC_DIR']
        self.proxy_addr = config['message_download']['PROXY_ADDR']
        self.proxy_port = config['message_download']['PROXY_PORT']
        self.API_ID = config['message_download']['API_ID']
        self.API_HASH = config['message_download']['API_HASH']
        self.TG_AUTH_FILE_NAME = config['message_download']['TG_AUTH_FILE_NAME']

    def getpath(self):
        return self._path

    def get_TG_AUTH_FILE_NAME(self):
        return self.TG_AUTH_FILE_NAME

    def get_API_HASH(self):
        return self.API_HASH

    def get_API_ID(self):
        return self.API_ID

    def get_pic_path(self):
        return self.picture_storage_path

    def get_proxy_port(self):
        return self.proxy_port

    def get_proxy_addr(self):
        return self.proxy_addr

    def get_random_file_name(self):
        H = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
        salt = ''
        for i in range(22):
            salt += random.choice(H)
        t_dir = time.strftime("%Y-%m-%d", time.localtime())
        return salt


if __name__ == '__main__':
    c = config()
    print(c.getpath())
    print(c.get_pic_path())
    print(c.get_socks5_addr())
    print(c.get_socks5_port())