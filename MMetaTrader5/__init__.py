import numpy as np
from datetime import datetime
from typing import Tuple, Dict

"""
Mock MetaTrader5 module for development on macOS.
This allows code to run without the actual MetaTrader5 package.
"""


class MockTerminalInfoData:
    def __init__(self):
        self.trade_allowed = True
        self.margin_call = False
        self.stop_out = False


class MockPositionsGetData:
    def __init__(
        self, magic: int, type: int = 0, symbol="EURUSD", volume=0.0, ticket=0
    ):
        self.magic = magic
        self.type = type
        self.symbol = symbol
        self.volume = volume
        self.ticket = ticket


class MockOrderGetData:
    def __init__(
        self, magic: int, type: int = 0, symbol="EURUSD", volume=0.0, ticket=0
    ):
        self.magic = magic
        self.type = type
        self.symbol = symbol
        self.volume = volume
        self.ticket = ticket


class MockSymbolInfoData:

    def __init__(
        self,
        visible: bool,
        volume_min=0.01,
        volume_max=100.0,
        volume_step=0.01,
        trade_tick_size=0.01,
        currency_profit="USD",
        trade_contract_size=100000.0,
        point=0.00001,
        bid=1000.0,
        ask=1000.0,
    ):
        self.visible = visible
        self.volume_min = volume_min
        self.volume_max = volume_max
        self.volume_step = volume_step
        self.trade_tick_size = trade_tick_size
        self.currency_profit = currency_profit
        self.bid = bid
        self.ask = ask
        self.point = point
        self.trade_contract_size = trade_contract_size


class MockAccountInfoData:
    def __init__(self):
        self.login = 123456
        self.balance = 10000.0
        self.equity = 10000.0
        self.margin = 0.0
        self.margin_free = 10000.0
        self.margin_level = 100.0
        self.trade_mode = 0
        self.name = "Javier Gonzalez"
        self.server = "Mock Server"
        self.company = "Mock Broker"
        self.currency = "USD"
        self.leverage = 200
        self._asdict = lambda: {
            "login": self.login,
            "balance": self.balance,
            "equity": self.equity,
            "margin": self.margin,
            "margin_free": self.margin_free,
            "margin_level": self.margin_level,
            "trade_mode": self.trade_mode,
            "name": self.name,
            "server": self.server,
            "company": self.company,
            "currency": self.currency,
            "leverage": self.leverage,
        }


class MockSymbolInfoTickData:
    def __init__(self):
        self.bid = 1.12345
        self.ask = 1.12355
        self.last = 1.12350
        self.volume = 1000
        self.time = 1234567890
        self.flags = 4
        self.time_msc = 1234567890123
        self._asdict = lambda: {
            "bid": self.bid,
            "ask": self.ask,
            "last": self.last,
            "volume": self.volume,
            "time": self.time,
            "flags": self.flags,
            "time_msc": self.time_msc,
        }


class MockHistoryDealsData:
    def __init__(self, symbol: str = "MOCK-SYMBOL", ticket: int = 112345):
        self.symbol = symbol
        self.ticket = ticket
        self.price = 12355
        self.ask = 1.12355
        self.last = 1.12350
        self.volume = 0.4
        self.type = 0
        self.time = 1234567890
        self.flags = 4
        self.time_msc = 1234567890123
        self._asdict = lambda: {
            "ticket": self.ticket,
            "symbol": self.symbol,
            "ask": self.ask,
            "last": self.last,
            "volume": self.volume,
            "type": self.type,
            "time": self.time,
            "flags": self.flags,
            "time_msc": self.time_msc,
        }


class MockOrderSendRequestData:
    def __init__(
        self,
        action: int,
        type: int = 0,
        symbol="EURUSD",
        volume=0.0,
        sl: float = 0.0,
        tp: float = 0.0,
        deviation: float = 0.0,
        magic: int = 0,
        comment: str = "",
        type_filling: int = 0,
        price: float = 0.0,
    ):
        self.action = action
        self.type = type
        self.symbol = symbol
        self.volume = volume
        self.sl = sl
        self.tp = tp
        self.deviation = deviation
        self.magic = magic
        self.comment = comment
        self.type_filling = type_filling
        self.price = price


class MockOrderSendData:
    def __init__(self, request: Dict = {}):
        self.retcode = 10009
        self.deal = 0
        self.order = 0
        self.volume = 0.0
        self.price = 0.0
        self.bid = 0.0
        self.ask = 0.0
        self.comment = "Mock order"
        self.request_id = 0
        self.retcode_external = 0
        self.request = request
        self._asdict = lambda: {
            "retcode": 10009,
            "deal": 0,
            "order": 0,
            "volume": 0.0,
            "price": 0.0,
            "bid": 0.0,
            "ask": 0.0,
            "comment": "Mock order",
            "request_id": 0,
            "retcode_external": 0,
            "request": self.request,
        }


def random_between_0_and_n(n=1):
    """Return a random float between 0 and n (default 1)."""
    return np.random.rand() * n


ACCOUNT_TRADE_MODE_DEMO = 0
ACCOUNT_TRADE_MODE_CONTEST = 1
ACCOUNT_TRADE_MODE_REAL = 2

TIMEFRAME_M1 = 1
TIMEFRAME_M2 = 2
TIMEFRAME_M3 = 3
TIMEFRAME_M4 = 4
TIMEFRAME_M5 = 5
TIMEFRAME_M6 = 6
TIMEFRAME_M10 = 7
TIMEFRAME_M12 = 8
TIMEFRAME_M20 = 9
TIMEFRAME_M30 = 10
TIMEFRAME_H1 = 11
TIMEFRAME_H2 = 12
TIMEFRAME_H3 = 13
TIMEFRAME_H4 = 14
TIMEFRAME_H5 = 15
TIMEFRAME_H6 = 16
TIMEFRAME_H8 = 17
TIMEFRAME_H12 = 18
TIMEFRAME_D1 = 19
TIMEFRAME_W1 = 20
TIMEFRAME_MN1 = 21

ORDER_TYPE_BUY = 0
ORDER_TYPE_SELL = 1
ORDER_TYPE_BUY_STOP = 2
ORDER_TYPE_SELL_STOP = 3
ORDER_TYPE_BUY_LIMIT = 4
ORDER_TYPE_SELL_LIMIT = 5

ORDER_FILLING_FOK = 0
ORDER_FILLING_IOC = 1
ORDER_TIME_GTC = 1

DEAL_TYPE_BUY = 0
DEAL_TYPE_SELL = 1

TRADE_ACTION_DEAL = 0
TRADE_ACTION_PENDING = 1
TRADE_ACTION_REMOVE = 2

TRADE_RETCODE_DONE = 10009
TRADE_RETCODE_PENDING = 10010
TRADE_RETCODE_DONE_PARTIAL = 10011

account_info_data = MockAccountInfoData()
symbol_info_data = {
    "EURUSD": MockSymbolInfoData(visible=True),
    "GBPUSD": MockSymbolInfoData(visible=True),
    "USDJPY": MockSymbolInfoData(visible=False),
}
terminal_info_data = MockTerminalInfoData()


def initialize(
    path: str,
    login: int,
    password: str,
    server: str,
    timeout: int,
    portable: bool,
):
    return True


def login():
    """Mock login function"""
    return True


def shutdown():
    """Mock shutdown function"""
    return True


def copy_rates_from():
    """Mock copy_rates_from function"""
    return []


def copy_ticks_from():
    """Mock copy_ticks_from function"""
    return []


def positions_get(
    symbol: str = "EURUSD", ticket: int = 0
) -> Tuple[MockPositionsGetData, ...]:
    """Mock positions_get function"""
    if symbol == "EURUSD":
        return (
            MockPositionsGetData(magic=1010101, symbol="EURUSD", volume=0.1),
            MockPositionsGetData(magic=1010101, type=1, symbol="EURUSD", volume=0.1),
        )
    elif symbol == "GBPUSD":
        return (
            MockPositionsGetData(magic=1010101, symbol="GBPUSD", volume=0.1),
            MockPositionsGetData(magic=1010101, type=1, symbol="GBPUSD", volume=0.1),
        )
    return ()


def orders_get(symbol: str = "EURUSD", ticket: int = 0) -> Tuple[MockOrderGetData, ...]:
    """Mock orders_get function"""
    if symbol == "EURUSD":
        return (
            MockOrderGetData(magic=1010101, symbol="EURUSD", volume=0.1),
            MockOrderGetData(magic=1010101, type=1, symbol="EURUSD", volume=0.1),
        )
    elif symbol == "GBPUSD":
        return (
            MockOrderGetData(magic=1010101, symbol="GBPUSD", volume=0.1),
            MockOrderGetData(magic=1010101, type=1, symbol="GBPUSD", volume=0.1),
        )
    return ()


def history_deals_get(ticket: str) -> Tuple[MockHistoryDealsData, ...]:
    """Mock history_deals_get function"""
    data = [MockHistoryDealsData()]
    return tuple(data)


def order_send(request: dict = {}) -> MockOrderSendData:
    """Mock order_send function"""
    return MockOrderSendData()


def account_info() -> MockAccountInfoData:
    """Mock account_info function"""
    return account_info_data


def terminal_info() -> MockTerminalInfoData:
    """Mock terminal_info function"""
    return terminal_info_data


def symbol_info(symbol: str) -> MockSymbolInfoData:
    """Mock symbol_info function"""
    return symbol_info_data.get(symbol, MockSymbolInfoData(visible=False))


def symbol_select(symbol: str, value: bool) -> bool:
    """Mock symbol_select function"""
    return True


def symbol_info_tick(symbol: str) -> MockSymbolInfoTickData:
    """Mock symbol_info_tick function"""
    return MockSymbolInfoTickData()


def copy_rates_from_pos(
    symbol: str, timeframe: str, pos: int, count: int
) -> np.ndarray:
    """Mock copy_rates_from_pos function"""
    random_number = random_between_0_and_n()
    print(f"Random number for copy_rates_from_pos: {random_number}")
    date_val = datetime.now().microsecond
    data1 = [
        (
            date_val,
            1.29568,
            1.30692,
            random_between_0_and_n(40000),
            1.30412,
            68228,
            0,
            0,
        ),
    ]
    data2 = [
        (
            date_val,
            1.29568,
            1.30692,
            random_between_0_and_n(40000),
            2.30412,
            78228,
            0,
            0,
        ),
        (
            date_val,
            1.30385,
            1.30631,
            random_between_0_and_n(40000),
            2.30471,
            66498,
            0,
            0,
        ),
        (
            date_val,
            1.30324,
            1.30536,
            random_between_0_and_n(40000),
            2.30039,
            59400,
            0,
            0,
        ),
        (
            date_val,
            1.30039,
            1.30486,
            random_between_0_and_n(40000),
            2.29952,
            72288,
            0,
            0,
        ),
        (
            date_val,
            1.29952,
            1.3023,
            random_between_0_and_n(40000),
            2.29187,
            87909,
            0,
            0,
        ),
        (
            date_val,
            1.29186,
            1.29281,
            random_between_0_and_n(40000),
            2.28792,
            71033,
            0,
            0,
        ),
        (
            date_val,
            1.28802,
            1.29805,
            random_between_0_and_n(40000),
            2.29566,
            76386,
            0,
            0,
        ),
        (
            date_val,
            1.29426,
            1.29547,
            random_between_0_and_n(40000),
            2.29283,
            76933,
            0,
            0,
        ),
        (
            date_val,
            1.2929,
            1.30178,
            random_between_0_and_n(40000),
            2.30037,
            90121,
            0,
            0,
        ),
        (
            date_val,
            1.30036,
            1.30078,
            random_between_0_and_n(40000),
            2.29374,
            49286,
            0,
            0,
        ),
    ]
    if random_number > 0.5:
        data1 = [
            (
                date_val,
                1.29568,
                1.30692,
                random_between_0_and_n(40000),
                2.30412,
                88228,
                0,
                0,
            ),
        ]
        data2 = [
            (
                date_val,
                1.29568,
                1.30692,
                random_between_0_and_n(40000),
                1.30412,
                68228,
                0,
                0,
            ),
        ]
        data2 = [
            (
                date_val,
                1.29568,
                1.30692,
                random_between_0_and_n(40000),
                1.30412,
                68228,
                0,
                0,
            ),
            (
                date_val,
                1.30385,
                1.30631,
                random_between_0_and_n(40000),
                1.30471,
                56498,
                0,
                0,
            ),
            (
                date_val,
                1.30324,
                1.30536,
                random_between_0_and_n(40000),
                1.30039,
                49400,
                0,
                0,
            ),
            (
                date_val,
                1.30039,
                1.30486,
                random_between_0_and_n(40000),
                1.29952,
                62288,
                0,
                0,
            ),
            (
                date_val,
                1.29952,
                1.3023,
                random_between_0_and_n(40000),
                1.29187,
                57909,
                0,
                0,
            ),
            (
                date_val,
                1.29186,
                1.29281,
                random_between_0_and_n(40000),
                1.28792,
                61033,
                0,
                0,
            ),
            (
                date_val,
                1.28802,
                1.29805,
                random_between_0_and_n(40000),
                1.29566,
                66386,
                0,
                0,
            ),
            (
                date_val,
                1.29426,
                1.29547,
                random_between_0_and_n(40000),
                1.29283,
                66933,
                0,
                0,
            ),
            (
                date_val,
                1.2929,
                1.30178,
                random_between_0_and_n(40000),
                1.30037,
                80121,
                0,
                0,
            ),
            (
                date_val,
                1.30036,
                1.30078,
                random_between_0_and_n(40000),
                random_between_0_and_n(40000),
                49286,
                0,
                0,
            ),
        ]

    if count == 1:
        return np.array(
            data1,
            dtype=[
                ("time", "i4"),
                ("open", "f4"),
                ("high", "f4"),
                ("low", "f4"),
                ("close", "f4"),
                ("tick_volume", "i4"),
                ("spread", "i4"),
                ("real_volume", "i4"),
            ],
        )
    else:
        return np.array(
            data2,
            dtype=[
                ("time", "i4"),
                ("open", "f4"),
                ("high", "f4"),
                ("low", "f4"),
                ("close", "f4"),
                ("tick_volume", "i4"),
                ("spread", "i4"),
                ("real_volume", "i4"),
            ],
        )
