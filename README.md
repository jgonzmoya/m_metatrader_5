# MMetaTrader5

Metatrader5 mock for macOS development.

This package provides a lightweight, dependency-free mock of the MetaTrader5 Python API so you can develop and test trading code on macOS (or any environment without MetaTrader5 installed). It mirrors common functions, constants, and data structures you typically use from the real MetaTrader5 package.

Note: This is a mock intended for development and testing only. It does not execute real trades or connect to real brokers.


## Features

- Drop-in style API similar to MetaTrader5 for the most-used calls
- Deterministic/stubbed data with a bit of randomness where useful
- Basic data classes for account, symbols, positions, orders, ticks
- Useful constants (timeframes, order types, trade actions, etc.)


## Installation

Install into your current environment from the local source:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -U pip
pip install -e .
```

After installation you can import it as `MMetaTrader5`.


## Quick start

```python
import MMetaTrader5 as mt5

# Initialize/login (mocked and always returns True)
mt5.initialize(path="/Applications/MetaTrader 5.app", login=123456, password="***", server="Mock-Server", timeout=5, portable=True)
mt5.login()

info = mt5.account_info()
print(info._asdict())

# Get current tick for a symbol (mocked values)
tick = mt5.symbol_info_tick("EURUSD")
print(tick._asdict())

# Positions and orders (mocked tuples of data)
positions = mt5.positions_get(symbol="EURUSD")
orders = mt5.orders_get(symbol="EURUSD")
print(positions, orders)

# Copy rates from position (returns numpy structured array)
rates = mt5.copy_rates_from_pos("EURUSD", mt5.TIMEFRAME_M5, 0, 10)
print(rates.dtype, rates.shape)

# Place an order (mocked response)
req = {
    "action": mt5.TRADE_ACTION_DEAL,
    "type": mt5.ORDER_TYPE_BUY,
    "symbol": "EURUSD",
    "volume": 0.1,
}
res = mt5.order_send(req)
print(res._asdict())

mt5.shutdown()
```


## API Overview

The mock surfaces a subset of the MetaTrader5 interface used commonly in bots and strategies. The following items are available:

### Functions
- initialize(path: str, login: int, password: str, server: str, timeout: int, portable: bool) -> bool
- login() -> bool
- shutdown() -> bool
- copy_rates_from() -> list
- copy_ticks_from() -> list
- positions_get(symbol: str = "EURUSD", ticket: int = 0) -> Tuple[MockPositionsGetData, ...]
- orders_get(symbol: str = "EURUSD", ticket: int = 0) -> Tuple[MockOrderGetData, ...]
- history_deals_get(ticket: str) -> Tuple[MockHistoryDealsData, ...]
- order_send(request: dict = {}) -> MockOrderSendData
- account_info() -> MockAccountInfoData
- terminal_info() -> MockTerminalInfoData
- symbol_info(symbol: str) -> MockSymbolInfoData
- symbol_select(symbol: str, value: bool) -> bool
- symbol_info_tick(symbol: str) -> MockSymbolInfoTickData
- copy_rates_from_pos(symbol: str, timeframe: int, pos: int, count: int) -> numpy.ndarray

### Constants
- Account trade modes: ACCOUNT_TRADE_MODE_DEMO, ACCOUNT_TRADE_MODE_CONTEST, ACCOUNT_TRADE_MODE_REAL
- Timeframes: TIMEFRAME_M1, TIMEFRAME_M2, ..., TIMEFRAME_MN1
- Order types: ORDER_TYPE_BUY, ORDER_TYPE_SELL, ORDER_TYPE_BUY_STOP, ORDER_TYPE_SELL_STOP, ORDER_TYPE_BUY_LIMIT, ORDER_TYPE_SELL_LIMIT
- Order filling: ORDER_FILLING_FOK, ORDER_FILLING_IOC
- Order time: ORDER_TIME_GTC
- Deal types: DEAL_TYPE_BUY, DEAL_TYPE_SELL
- Trade actions: TRADE_ACTION_DEAL, TRADE_ACTION_PENDING, TRADE_ACTION_REMOVE
- Trade retcodes: TRADE_RETCODE_DONE, TRADE_RETCODE_PENDING, TRADE_RETCODE_DONE_PARTIAL

### Data objects (selected attributes)
- MockAccountInfoData: login, balance, equity, margin, margin_free, margin_level, trade_mode, name, server, company, currency, leverage, _asdict()
- MockSymbolInfoData: visible, volume_min, volume_max, volume_step, trade_tick_size, currency_profit, trade_contract_size, point, bid, ask
- MockSymbolInfoTickData: bid, ask, last, volume, time, flags, time_msc, _asdict()
- MockPositionsGetData / MockOrderGetData: magic, type, symbol, volume, ticket
- MockHistoryDealsData: ticket, symbol, ask, last, volume, type, time, flags, time_msc, _asdict()
- MockOrderSendRequestData: action, type, symbol, volume, sl, tp, deviation, magic, comment, type_filling, price
- MockOrderSendData: retcode, deal, order, volume, price, bid, ask, comment, request_id, retcode_external, request, _asdict()


## Behavior notes and limitations

- All functions are mocked and return fixed or pseudo-random data. No network or broker calls are made.
- Some helpers introduce randomness (e.g., copy_rates_from_pos) and may print a random number for demonstration purposes.
- Only a small set of symbols is preconfigured: EURUSD, GBPUSD (visible=True) and USDJPY (visible=False).
- This module is intended to be API-compatible enough for local development; do not use it for backtesting fidelity or production trading.


## Compatibility

- Python 3.x
- macOS primary target, but should work anywhere Python and numpy are available.

Dependencies are declared in setup.py and include:
- numpy (imported directly by the module)
- requests (declared as a setup dependency)


## Development

Run tests or your scripts against the mock to iterate on your trading logic without requiring a Windows/MetaTrader5 setup.

Recommended workflow:
- Keep your strategy code importing `import MetaTrader5 as mt5` in production.
- For macOS development without MT5 installed, temporarily change the import to `import MMetaTrader5 as mt5`.
- Alternatively, use an environment switch in your code to select the module at runtime.

Example environment switch:

```python
try:
    import MetaTrader5 as mt5  # real package when available
except Exception:
    import MMetaTrader5 as mt5  # fallback to mock
```


## Versioning

- Current version: 0.0.1
- Status: Alpha


## License

MIT License © Javier Gonzalez Moya


## Acknowledgements

Inspired by the MetaTrader5 Python API. This project is not affiliated with MetaQuotes or MetaTrader.

