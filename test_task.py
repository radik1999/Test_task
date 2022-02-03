from unittest import TestCase
from unittest.mock import patch

from task import get_coin_price


class TestTask(TestCase):

    @patch("task.get_coin_id", lambda coin_code: -1)
    def test_get_coin_price_no_coin_data(self):
        coin_price = get_coin_price("btc", "uah")

        self.assertEqual(coin_price, "There is no data for coin with the 'btc' code")

    @patch("task.get_coin_data", lambda coin_code: {"market_data": {"current_price": {}}})
    def test_get_coin_price_no_currency_data(self):
        coin_price = get_coin_price("btc", "uah")

        self.assertEqual(coin_price, "There is no price data for currency with the 'uah' code")

    @patch("task.get_coin_data", lambda coin_code: {"market_data": {"current_price": {"uah": 10350000}}})
    def test_get_coin_price(self):
        coin_price = get_coin_price("btc", "uah")

        self.assertEqual(coin_price, 10350000)
