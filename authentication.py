import streamlit as st
import pymongo
import bcrypt
from homepage import homepage  # Import your homepage function

# MongoDB connection
MONGO_URI = "mongodb+srv://pawargaurav1349:gaurav123@infosys.yocr7.mongodb.net/?retryWrites=true&w=majority&appName=Infosys"

client = pymongo.MongoClient(MONGO_URI)
db = client['infosys']
users_collection = db['users']

# Register user
def register_user(username, password):
    # Check if user already exists
    existing_user = users_collection.find_one({"username": username})
    if existing_user:
        st.error("User already exists. Please login.")
        return False
    
    # Hash the password before storing
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    users_collection.insert_one({"username": username, "password": hashed_password.decode()})
    st.success("Signup successful! Redirecting to homepage...")

    # Set session state to mark the user as authenticated
    st.session_state["authenticated"] = True
    st.session_state["username"] = username

    # Use session state to trigger the rerun
    st.session_state["rerun"] = True  # Flag to trigger rerun
    return True

# Authenticate user
def authenticate_user(username, password):
    # Check if the user exists
    user = users_collection.find_one({"username": username})
    if user and bcrypt.checkpw(password.encode('utf-8'), user["password"].encode()):
        return True  # Successful authentication
    return False  # Invalid credentials

# Login / Signup Page
def login_signup():
    st.title("Login / Signup")

    # User selects login or signup
    choice = st.radio("Select an option:", ["Login", "Signup"], key="login_signup_radio")

    # User input fields
    username = st.text_input("Username", key="username_input")
    password = st.text_input("Password", type="password", key="password_input")

    if choice == "Signup":
        if st.button("Signup", key="signup_button"):
            if username and password:
                register_user(username, password)
            else:
                st.warning("Please enter a username and password.")
    else:  # Login functionality
        if st.button("Login", key="login_button"):
            if username and password:
                if authenticate_user(username, password):
                    st.session_state["authenticated"] = True
                    st.session_state["username"] = username
                    st.session_state["rerun"] = True  # Set flag to trigger rerun
                else:
                    st.error("Invalid username or password.")
            else:
                st.warning("Please enter a username and password.")


# Render homepage if authenticated
if "authenticated" in st.session_state and st.session_state["authenticated"]:
    homepage()

    # Check if rerun flag is set to true, then reset it
    if st.session_state.get("rerun", False):
        st.session_state["rerun"] = False
        st.experimental_rerun()  # Trigger rerun to refresh the session state
else:
    login_signup()
