#!/usr/bin/env python

import logging
import asyncio
from binance.async_spot import AsyncSpot as Client
from binance.lib.utils import config_logging
from examples.utils.prepare_env import get_api_key

config_logging(logging, logging.DEBUG)

async def main():
    api_key, api_secret = get_api_key()

    spot_client = Client(api_key, api_secret)

    logger = logging.getLogger(__name__)

    logger.info(
        await spot_client.sub_account_api_get_ip_restriction(
            email="alice@test.com",
            subAccountApiKey="sub_account_api_key",
        )
    )


if __name__ == "__main__":
    asyncio.run(main())
