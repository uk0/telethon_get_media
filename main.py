from telethon import TelegramClient, sync
import random
import time
import socks
from multiprocessing import Process ,cpu_count
import os
picture_storage_path = './data/'

from main_v1 import tg_watchon_class

import logging
pids = []
def get_media(channel_username,client):
    #myself = client.get_me()
    #print(channel_username)
    for msgs in client.get_messages(channel_username, limit=10):
        # print(msgs.message)
        # print(msgs.media)
        if msgs.media is not None:

            H = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
            salt = ''
            for i in range(22):
                salt += random.choice(H)

            t_dir = time.strftime("%Y-%m-%d", time.localtime())
            filename = picture_storage_path + str(t_dir) + '/' + str(salt)
            client.download_media(msgs.media, filename)


if __name__ == '__main__':

    t = tg_watchon_class()
    
    if __name__ == '__main__':
        p_list = []
        for xx in ['china-news']:
            p_list.append(Process(target=get_media, args=('%s' % xx,t.get_client(),)))
        # 独立启动监听
        p_list.append(Process(target=t.start, args=()))
        for xx in p_list:
            xx.start()

        print(get_pids())
        
        for xx in p_list:
            xx.join()


    print('(Press Ctrl+C to stop this)')


