import argparse
from bot.orders import execute_order
from bot.validators import *
from bot.logging_config import setup_logging
import logging


def main():
    setup_logging()

    parser = argparse.ArgumentParser(description="Simple Trading Bot")

    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--type", required=True)
    parser.add_argument("--quantity", type=float, required=True)
    parser.add_argument("--price", type=float)

    args = parser.parse_args()

    try:
        # Validate inputs
        validate_side(args.side)
        validate_order_type(args.type)
        validate_quantity(args.quantity)
        validate_price(args.type, args.price)

        print("\nOrder Details:")
        print("Symbol:", args.symbol)
        print("Side:", args.side)
        print("Type:", args.type)
        print("Quantity:", args.quantity)
        print("Price:", args.price)

        # Place order
        response = execute_order(args.symbol,args.side,args.type,args.quantity,args.price)

        print("\nResponse:")
        print("Order ID:", response.get("orderId"))
        print("Status:", response.get("status"))
        print("Executed Qty:", response.get("executedQty"))

        if "orderId" in response:
            print("\nSUCCESS")
        else:
            print("\nFAILED")

        logging.info(response)

    except Exception as e:
        print("Error:", e)
        logging.error(str(e))


if __name__ == "__main__":
    main()