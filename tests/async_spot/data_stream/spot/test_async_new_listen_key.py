import pytest

from binance.async_spot import AsyncSpot as Client
from tests.util import random_str
from tests.util import mock_async_http_response

mock_item = {"key_1": "value_1", "key_2": "value_2"}
mock_exception = {"code": -1, "msg": "error message"}

key = random_str()
secret = random_str()


@pytest.mark.asyncio
@mock_async_http_response("POST", "/api/v3/userDataStream", mock_item, 200)
async def test_new_listen_key():
    """Tests the API endpoint to create a new listen key"""

    client = Client(key)
    response = await client.new_listen_key()
    response.should.equal(mock_item)