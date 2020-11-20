from telethon import TelegramClient, sync, events, utils

from telethon.tl.functions.messages import ForwardMessagesRequest
from telethon.tl.functions.messages import SendMessageRequest
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


class tg_watchon_class:

    def __init__(self):
        self.data_storage_path = config.getpath()
        self.api_id = 1860111
        self.api_hash = "464a049a4c34k3be65cfa7d7"

        self.client = TelegramClient('some_name', self.api_id, self.api_hash,
                                     proxy=(socks.SOCKS5, '127.0.0.1', 10888)).start()

        @self.client.on(events.NewMessage)
        async def handler(event):
            print("handler init success")
            '''
                print('sender: ' + str(event.input_sender) + 'to: ' + str(event.message.to_id))
            '''

            if event.raw_text == '':
                if event.media is not None:
                    salt = config.get_random_file_name()
                    filename = self.data_storage_path + str(t_dir) + '/' + str(salt)
                    await self.client.download_media(event.media, filename)
            else:
                print('sender: ' + str(event.input_sender) + '#### to: ' + str(
                    event.message.to_id) + '#### Message: ' + event.raw_text)

    def get_client(self):
        return self.client

    def start(self):
        print('(Press Ctrl+C to stop this)')
        self.client.run_until_disconnected()
