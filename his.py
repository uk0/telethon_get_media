import random
import asyncio
from telethon import TelegramClient, types
from telethon.errors import ChannelPrivateError, UsernameInvalidError, UsernameNotOccupiedError
from telethon.tl.functions.messages import GetHistoryRequest
from telethon.tl.functions.channels import GetFullChannelRequest
from telethon.tl.types import PeerChat, PeerChannel, InputPeerChat

from logger_config import setup_logger
logger = setup_logger()
#  支持获取评论区的内容。
class TgHistoryClass:
    def __init__(self, channel_id, limit, total_count_limit):
        # EasyImage 图床平台的 API URL 和 Token
        api_id = "xxxxxx"  # 替换为你的 API ID
        api_hash = "xxxxxx"
        username = "xxxx"

        # 创建客户端
        self.client = TelegramClient(username, api_id, api_hash)
        self.channel_id = channel_id
        if isinstance(self.channel_id, int):
            # 数字频道
            self.my_channel = PeerChannel(channel_id)
        self.limit = limit
        self.total_count_limit = total_count_limit

    def disconnection(self):
        # 这行会阻塞，直到客户端断连并且无法重连，或你主动停止
        self.client.disconnect()


    async def offline_msg_task_test(self):
        await self.client.start()
        try:
            if isinstance(self.channel_id, str):
                self.my_channel = await self.client.get_entity(self.channel_id)
        except (UsernameInvalidError, UsernameNotOccupiedError) as e:
            logger.warning(f"频道 {self.channel_id} 不存在或无效: {e}")
            return
        except Exception as e:
            logger.error(f"获取频道 {self.channel_id} 时出错: {e}")
            return

        # 1. 拉频道历史消息
        all_messages = []
        offset_id = 0
        while True:
            try:
                history = await self.client(GetHistoryRequest(
                    peer=self.my_channel,
                    offset_id=offset_id,
                    offset_date=None,
                    add_offset=0,
                    limit=self.limit,
                    max_id=0,
                    min_id=0,
                    hash=0
                ))
                await asyncio.sleep(random.uniform(3.5, 5.0))
            except ChannelPrivateError:
                logger.warning(f"频道 {self.channel_id} 是私有的或无访问权限")
                break
            except ConnectionError as e:
                logger.warning(f"连接错误: {e}，等待 10 秒后重试")
                await asyncio.sleep(10)
                continue
            except Exception as e:
                logger.error(f"获取频道 {self.channel_id} 历史消息时出错: {e}")
                break

            if not history.messages:
                break

            all_messages.extend(history.messages)
            offset_id = history.messages[-1].id
            if self.total_count_limit and len(all_messages) >= self.total_count_limit:
                break

        logger.info(f"从频道 {self.channel_id} 获取了 {len(all_messages)} 条消息")

        # 2. 获取讨论组实体
        discussion_entity = None
        try:
            full = await self.client(GetFullChannelRequest(channel=self.my_channel))
            linked_id = getattr(full.full_chat, 'linked_chat_id', None)
            if linked_id:
                discussion_entity = await self.client.get_entity(PeerChannel(linked_id))
                logger.info(f"讨论组实体已获取: id={discussion_entity.id}, type={type(discussion_entity)}")
            else:
                logger.info(f"频道 {self.channel_id} 未开启评论功能（无讨论组）。")
        except Exception as e:
            logger.warning(f"获取频道讨论组时出错: {e}")

        if discussion_entity:
            logger.info("开始扫描讨论组消息，建立转发帖映射...")
            async for dmsg in self.client.iter_messages(discussion_entity, limit=120): # limit可调整
                if dmsg.media:
                    all_messages.append(dmsg)
        # 打印并下载原始消息及其评论
        try:
            for msg in all_messages:
                if msg.media:
                    await self.client.download_media(msg, file='./downloads/')
                    logger.info(f"下载消息 {msg.id} 的 media: {msg.media}")
                print(f"【消息 {msg.id}】: {msg}")
        except Exception as e:
            logger.error(f"处理评论区时出错: {e}")

        await self.client.disconnect()
        logger.info("客户端已断开连接")
if __name__ == '__main__':
    # 示例用法
    channel_id = 'hao123'  # 替换为你的频道ID
    limit = 100  # 每次获取的消息数量
    total_count_limit = 2  # 0 表示不限制总数

    tg_history = TgHistoryClass(channel_id, limit, total_count_limit)

    # 使用 asyncio 运行异步任务
    loop = asyncio.get_event_loop()
    loop.run_until_complete(tg_history.offline_msg_task_test())

    tg_history.disconnection()
