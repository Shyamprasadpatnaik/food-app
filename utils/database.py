
import pandas as pd

ORDERS_DB = "orders.csv"
FOODS_DB = "foods.csv"

def load_foods():
    return pd.read_csv(FOODS_DB)

def place_order(username, food_name):
    orders = load_orders()
    orders.loc[len(orders)] = [username, food_name]
    orders.to_csv(ORDERS_DB, index=False)

def load_orders():
    try:
        return pd.read_csv(ORDERS_DB)
    except:
        return pd.DataFrame(columns=["username", "food_item"])
