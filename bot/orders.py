from bot.client import place_order


# Wrapper function for placing order
def execute_order(symbol, side, order_type, quantity, price=None):
    response = place_order(symbol, side, order_type, quantity, price)
    return response