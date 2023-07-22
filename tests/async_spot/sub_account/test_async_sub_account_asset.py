import pytest

from tests.util import random_str
from tests.util import mock_async_http_response
from binance.async_spot import AsyncSpot as Client
from binance.error import ParameterRequiredError

mock_item = {"key_1": "value_1", "key_2": "value_2"}

key = random_str()
secret = random_str()

@pytest.mark.asyncio
async def test_sub_account_assets_without_email():
    """Tests the API endpoint to get sub account asset without email"""

    client = Client(key, secret)
    try:
        response = await client.sub_account_assets("")
    except Exception as e:
        assert isinstance(e, ParameterRequiredError)
    else:
        assert isinstance(response, ParameterRequiredError)



@pytest.mark.asyncio
@mock_async_http_response(
    "GET", "/sapi/v3/sub-account/assets\\?email=alice@test.com", mock_item, 200
)
async def test_sub_account_assets():
    """Tests the API endpoint to  get sub account asset"""

    client = Client(key, secret)
    response = await client.sub_account_assets(email="alice@test.com")
    response.should.equal(mock_item)