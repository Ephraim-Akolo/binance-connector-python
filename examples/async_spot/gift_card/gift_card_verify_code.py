#!/usr/bin/env python

import logging
import asyncio
from binance.async_spot import AsyncSpot as Client
from binance.lib.utils import config_logging
from examples.utils.prepare_env import get_api_key

config_logging(logging, logging.DEBUG)

async def main():
    api_key, api_secret = get_api_key()

    client = Client(api_key, api_secret)

    logger = logging.getLogger(__name__)

    response = await client.gift_card_verify_code("<the_reference_number_to_verify")
    logger.info(response)


if __name__ == "__main__":
    asyncio.run(main())


