import requests
import time
import hmac
import hashlib

# Add your API credentials here
API_KEY = "your_api_key"
SECRET_KEY = "your_secret_key"

BASE_URL = "https://testnet.binancefuture.com"


# Get Binance server time (to avoid timestamp issues)
def get_server_time():
    url = BASE_URL + "/fapi/v1/time"
    response = requests.get(url)
    return response.json()["serverTime"]


# Create signature using secret key
def create_signature(query_string):
    return hmac.new(
        SECRET_KEY.encode(),
        query_string.encode(),
        hashlib.sha256
    ).hexdigest()


# Function to place order
def place_order(symbol, side, order_type, quantity, price=None):
    endpoint = "/fapi/v1/order"
    url = BASE_URL + endpoint

    timestamp = get_server_time()

    params = {
        "symbol": symbol,
        "side": side,
        "type": order_type,
        "quantity": quantity,
        "timestamp": timestamp,
        "recvWindow": 5000
    }

    if order_type == "LIMIT":
        params["price"] = price
        params["timeInForce"] = "GTC"

    query_string = "&".join([f"{k}={v}" for k, v in params.items()])
    signature = create_signature(query_string)
    query_string += f"&signature={signature}"

    headers = {
        "X-MBX-APIKEY": API_KEY
    }

    response = requests.post(url + "?" + query_string, headers=headers)
    return response.json()