import streamlit as st
import builtins
import io
import sys
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


# ---------------- INPUT HANDLER FUNCTION ----------------
def handle_operation(func, inputs, success_msg, show_output=True):
    success, output = run_with_inputs(func, inputs)

    if not success:
        st.error(f"Error: {output}")
        return

    output_lower = output.lower()

    if "successfully" in output_lower:
        st.success(success_msg)
        
        if show_output:
            st.code(output)   
    else:
        st.error(output)

# ---------------- INPUT OVERRIDE FUNCTION ----------------
def run_with_inputs(func, inputs_list):
    original_input = builtins.input
    original_stdout = sys.stdout

    inputs = iter(inputs_list)
    builtins.input = lambda _: next(inputs)

    captured_output = io.StringIO()
    sys.stdout = captured_output

    try:
        func()
        output = captured_output.getvalue()
        return True, output   # ✅ success
    except Exception as e:
        return False, str(e)  # ❌ error
    finally:
        builtins.input = original_input
        sys.stdout = original_stdout


# ---------------- CREATE ACCOUNT ----------------
if menu == "Create Account":
    st.subheader("Create New Account")

    name = st.text_input("Full Name")
    age = st.number_input("Age", min_value=1)
    email = st.text_input("Email")
    pin = st.text_input("4-digit PIN")

    if st.button("Create Account"):
        if not pin.isdigit() or len(pin) != 4:
            st.error("PIN must be exactly 4 digits")
        else:
            handle_operation(
                user.createaccount,
                [name, str(age), email, pin],
                "Account Created Successfully ✅",
                show_output=True
            )


# ---------------- DEPOSIT ----------------
elif menu == "Deposit Money":
    st.subheader("Deposit Money")

    acc = st.text_input("Account Number")
    pin = st.text_input("PIN")
    amount = st.number_input("Amount", min_value=1)

    if st.button("Deposit"):
        handle_operation(
            user.depositmoney,
            [acc, pin, str(amount)],
            "Deposit Successful ✅"
        )


# ---------------- WITHDRAW ----------------
elif menu == "Withdraw Money":
    st.subheader("Withdraw Money")

    acc = st.text_input("Account Number")
    pin = st.text_input("PIN")
    amount = st.number_input("Amount", min_value=0)

    if st.button("Withdraw"):
        try:
            amt = int(amount)
        except:
            st.error("Invalid amount input")
            st.stop()

        if amt <= 0:
            st.error("Amount must be greater than 0")
            st.stop()   # 🚫 stops execution completely

        handle_operation(
            user.withdrawmoney,
            [acc, pin, str(amt)],
            "Withdrawal Successful ✅"
        )


# ---------------- SHOW DETAILS ----------------
elif menu == "Show Details":
    st.subheader("Account Details")

    acc = st.text_input("Account Number")
    pin = st.text_input("PIN")

    if st.button("Show Details"):
        success, output = run_with_inputs(user.showdetails, [acc, pin])

        if not success:
            st.error(output)
        else:
            st.code(output)


# ---------------- UPDATE ----------------
elif menu == "Update Details":
    st.subheader("Update Account")

    acc = st.text_input("Account Number")
    pin = st.text_input("PIN")
    name = st.text_input("New Name (optional)")
    email = st.text_input("New Email (optional)")
    new_pin = st.text_input("New PIN (optional)")

    if st.button("Update"):
        handle_operation(
            user.updatedetails,
            [acc, pin, name, email, new_pin],
            "Details Updated ✅",
            show_output=False   # 👈 hides bottom block
        )

# ---------------- DELETE ----------------
elif menu == "Delete Account":
    st.subheader("Delete Account")

    acc = st.text_input("Account Number")
    pin = st.text_input("PIN")
    confirm = st.selectbox("Confirm Delete", ["n", "Y"])

    if st.button("Delete"):
        handle_operation(
            user.deleteaccount,
            [acc, pin, confirm],
            "Account Deleted ✅",
            show_output=False
        )

# ---------------- TRANSFER ----------------
elif menu == "Transfer Money":
    st.subheader("Transfer Money")

    sender = st.text_input("Sender Account")
    pin = st.text_input("Sender PIN")
    receiver = st.text_input("Receiver Account")
    amount = st.number_input("Amount", min_value=0)

    if st.button("Transfer"):
        handle_operation(
            user.transfermoney,
            [sender, pin, receiver, str(amount)],
            "Transfer Successful ✅"
        )