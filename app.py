import streamlit as st
import builtins
from main import Bank

# Initialize
user = Bank()

st.set_page_config(page_title="Banking System", layout="centered")
st.title("💳 Banking System")

# Sidebar menu
menu = st.sidebar.radio("Select Operation", [
    "Create Account",
    "Deposit Money",
    "Withdraw Money",
    "Show Details",
    "Update Details",
    "Delete Account",
    "Transfer Money"
])

# ---------------- INPUT OVERRIDE FUNCTION ----------------
def run_with_inputs(func, inputs_list):
    original_input = builtins.input
    inputs = iter(inputs_list)

    builtins.input = lambda _: next(inputs)

    try:
        func()
        st.success("Operation executed successfully ✅")
    except Exception as e:
        st.error(f"Error: {e}")
    finally:
        builtins.input = original_input


# ---------------- CREATE ACCOUNT ----------------
if menu == "Create Account":
    st.subheader("Create New Account")

    name = st.text_input("Full Name")
    age = st.number_input("Age", min_value=1)
    email = st.text_input("Email")
    pin = st.text_input("4-digit PIN")

    if st.button("Create Account"):
        if name and email and pin:
            run_with_inputs(user.createaccount, [
                name, str(age), email, pin
            ])
        else:
            st.warning("Please fill all fields")


# ---------------- DEPOSIT ----------------
elif menu == "Deposit Money":
    st.subheader("Deposit Money")

    acc = st.text_input("Account Number")
    pin = st.text_input("PIN")
    amount = st.number_input("Amount", min_value=1)

    if st.button("Deposit"):
        run_with_inputs(user.depositmoney, [
            acc, pin, str(amount)
        ])


# ---------------- WITHDRAW ----------------
elif menu == "Withdraw Money":
    st.subheader("Withdraw Money")

    acc = st.text_input("Account Number")
    pin = st.text_input("PIN")
    amount = st.number_input("Amount", min_value=1)

    if st.button("Withdraw"):
        run_with_inputs(user.withdrawmoney, [
            acc, pin, str(amount)
        ])


# ---------------- SHOW DETAILS ----------------
elif menu == "Show Details":
    st.subheader("Account Details")

    acc = st.text_input("Account Number")
    pin = st.text_input("PIN")

    if st.button("Show Details"):
        run_with_inputs(user.showdetails, [
            acc, pin
        ])
        st.info("ℹ️ Output is printed in terminal")


# ---------------- UPDATE ----------------
elif menu == "Update Details":
    st.subheader("Update Account")

    acc = st.text_input("Account Number")
    pin = st.text_input("PIN")
    name = st.text_input("New Name (optional)")
    email = st.text_input("New Email (optional)")
    new_pin = st.text_input("New PIN (optional)")

    if st.button("Update"):
        run_with_inputs(user.updatedetails, [
            acc, pin, name, email, new_pin
        ])


# ---------------- DELETE ----------------
elif menu == "Delete Account":
    st.subheader("Delete Account")

    acc = st.text_input("Account Number")
    pin = st.text_input("PIN")
    confirm = st.selectbox("Confirm Delete", ["n", "Y"])

    if st.button("Delete"):
        run_with_inputs(user.deleteaccount, [
            acc, pin, confirm
        ])


# ---------------- TRANSFER ----------------
elif menu == "Transfer Money":
    st.subheader("Transfer Money")

    sender = st.text_input("Sender Account")
    pin = st.text_input("Sender PIN")
    receiver = st.text_input("Receiver Account")
    amount = st.number_input("Amount", min_value=1)

    if st.button("Transfer"):
        run_with_inputs(user.transfermoney, [
            sender, pin, receiver, str(amount)
        ])