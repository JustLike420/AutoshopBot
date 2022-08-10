#  Copyright (c) 2021. Tocenomiczs
import re
import time
from typing import Optional, Union
import requests
from telethon import TelegramClient


class Banker:
    client: TelegramClient
    _me_id: int

    def __init__(self, api_id: int, api_hash: str, number: Optional[str] = None,
                 password: Optional[str] = None):
        self.client = TelegramClient("banker", api_id=api_id, api_hash=api_hash)

        # self._me_id = self._client.loop.run_until_complete(self._client.get_me()).id

    # def __del__(self):
    #     self.client.disconnect()
    #     del self.client

    async def check_cheque(self, cheque_id: str) -> Union[bool, float]:
        async with self.client as client:
            await client.send_message('BTC_CHANGE_BOT', f"/start {cheque_id}")
            response = await self.get_last_message()
            if "Упс!" in response:
                return False
            try:
                btc = float(re.findall(r'\d+\.\d+ BTC', response)[0][:-4])
                response = btc * float(requests.get("https://apirone.com/api/v2/ticker?currency=btc").json()["rub"])
            except IndexError or ValueError:
                return False
            return response

    async def get_last_message(self) -> str:
        while True:
            message = (await self.client.get_messages("BTC_CHANGE_BOT", limit=1))[0]
            if message.message.startswith("Приветствую,"):
                time.sleep(0.5)
                continue
            if message.from_id is not None:
                if message.from_id.user_id == 5343257130:
                    time.sleep(0.5)
                    continue
            else:
                return message.message
