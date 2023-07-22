#!/usr/bin/env python

import logging
import asyncio
from binance.async_spot import AsyncSpot as Client
from binance.lib.utils import config_logging
from examples.utils.prepare_env import get_api_key

config_logging(logging, logging.DEBUG)

async def main():
    api_key, api_secret = get_api_key()

    logger = logging.getLogger(__name__)
    spot_client = Client(api_key, api_secret, show_header=True)
    logging.info(await spot_client.bnb_convertible_assets())


if __name__ == "__main__":
    asyncio.run(main())