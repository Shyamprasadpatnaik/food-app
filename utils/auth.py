
import pandas as pd

USER_DB = "users.csv"

def load_users():
    try:
        return pd.read_csv(USER_DB)
    except:
        return pd.DataFrame(columns=["username", "password"])

def save_user(username, password):
    users = load_users()
    users.loc[len(users)] = [username, password]
    users.to_csv(USER_DB, index=False)

def validate_user(username, password):
    users = load_users()
    return any((users["username"] == username) & (users["password"] == password))
