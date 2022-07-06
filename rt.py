from telethon import TelegramClient, sync, events, utils

from telethon.tl.functions.messages import ForwardMessagesRequest
from telethon.tl.functions.messages import SendMessageRequest
from telethon.tl.types.messages import Messages
from telethon.tl.functions.account import UpdateStatusRequest
from telethon.tl.functions.channels import GetChannelsRequest
from telethon.tl.functions.users import GetUsersRequest

import random
import logging
import time
import socks
from multiprocessing import Process, cpu_count

import asyncio

from conf import config

# Printing download progress
def callback(current, total):
    print('Downloaded', current, 'out of', total,
          'bytes: {:.2%}'.format(current / total))

class tg_watchon_class:

    def __init__(self):
        cfg = config()
        self.cfg1 = cfg
        self.data_storage_path = cfg.getpath()
        self.api_id = cfg.get_API_ID()
        self.api_hash = cfg.get_API_HASH()

        self.client = TelegramClient(cfg.get_TG_AUTH_FILE_NAME(), self.api_id, self.api_hash,
                                     proxy=(socks.HTTP,cfg.get_proxy_addr(), int(cfg.get_proxy_port()))).start()

        @self.client.on(events.NewMessage)
        async def handler(event):
            print("handler init success")
            '''
                print('sender: ' + str(event.input_sender) + 'to: ' + str(event.message.to_id))
            '''
            salt = self.cfg1.get_random_file_name()
            t_dir = time.strftime("%Y-%m-%d", time.localtime())
            filename_temp = self.data_storage_path + '/' + str(t_dir) + '/' + str(salt)

            print("download - " + filename_temp)

            import re
            filename_ = re.findall(r"file_name='(.+?)'", str(event.media))  #
            # print(str(event.media))
            if len(filename_) > 0:
                filename = "{}_{}".format(filename_temp, str(filename_[0]).replace(" ", "_"))
            else:
                filename = filename_temp
            await event.message.download_media(filename)


    def get_client(self):
        return self.client

    def start(self):
        print('(Press Ctrl+C to stop this)')
        self.client.run_until_disconnected()
