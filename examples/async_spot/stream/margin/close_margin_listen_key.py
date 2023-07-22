#!/usr/bin/env python

import logging
import asyncio
from binance.async_spot import AsyncSpot as Client
from binance.lib.utils import config_logging
from examples.utils.prepare_env import get_api_key

config_logging(logging, logging.DEBUG)

async def main():
    api_key, _ = get_api_key()
    client = Client(api_key)
    logging.info(await client.close_margin_listen_key(listenKey=""))


if __name__ == "__main__":
    asyncio.run(main())