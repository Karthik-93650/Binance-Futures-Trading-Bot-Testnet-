# Trading Bot (Binance Futures Testnet)

## Setup
1. Install dependencies:
pip install -r requirements.txt
2. Add your API keys in bot/client.py

## Run Example
Market Order:
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001

Limit Order:
python cli.py --symbol BTCUSDT --side BUY --type LIMIT --quantity 0.001 --price 30000

## Notes
- Add your API keys inside client.py before running.
- Uses Binance Futures Testnet
- Supports BUY and SELL
- Logging saved in trading_bot.log
- Example output will show orderId, status and execution details.