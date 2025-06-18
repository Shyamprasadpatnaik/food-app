
import streamlit as st
from utils.auth import validate_user, save_user
from utils.database import load_foods, place_order, load_orders

st.set_page_config(page_title="Sri Venketswaraa Food", layout="wide")

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.username = ""

def header():
    st.image("logo.png", width=100)
    st.markdown("""
    <h1 style='text-align: center;'>🌿 SRI VENKETSWARAA FOOD 🌿</h1>
    <h4 style='text-align: center; color: green;'>Pure Vegetarian & Hygienic</h4>
    """, unsafe_allow_html=True)

def login_page():
    st.title("Login / Sign Up")
    tab1, tab2 = st.tabs(["Login", "Register"])
    with tab1:
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        if st.button("Login"):
            if validate_user(username, password):
                st.success("Logged in successfully!")
                st.session_state.logged_in = True
                st.session_state.username = username
            else:
                st.error("Invalid credentials")
    with tab2:
        new_user = st.text_input("New Username")
        new_pass = st.text_input("New Password", type="password")
        if st.button("Sign Up"):
            save_user(new_user, new_pass)
            st.success("Registered successfully!")

def home_page():
    header()
    col1, col2, col3 = st.columns([4, 3, 2])
    with col1:
        search = st.text_input("🔍 Search Food")
    with col2:
        st.markdown("### 👤 " + st.session_state.username)
    with col3:
        if st.button("🧾 View My Orders"):
            show_orders()
    st.markdown("---")
    st.subheader("🍽 Available Dishes")
    foods = load_foods()
    filtered = foods[foods["food_name"].str.contains(search, case=False)] if search else foods
    for idx, row in filtered.iterrows():
        col = st.columns(2)
        with col[0]:
            st.image(row["image_path"], width=150)
        with col[1]:
            st.markdown(f"### {row['food_name']}")
            if st.button(f"Order {row['food_name']}", key=idx):
                place_order(st.session_state.username, row['food_name'])
                st.success(f"{row['food_name']} added to your order.")

def show_orders():
    st.subheader("🧾 Your Orders")
    orders = load_orders()
    user_orders = orders[orders["username"] == st.session_state.username]
    if not user_orders.empty:
        st.table(user_orders)
    else:
        st.info("You have not placed any orders yet.")

if not st.session_state.logged_in:
    login_page()
else:
    home_page()
