
import streamlit as st
import re

st.set_page_config(
    page_title="Password Checker",
    page_icon="🔐",
    layout="centered"
)

st.title("🔐 Password Strength Checker")
st.write("Check whether your password is weak, medium or strong.")

st.info("Your password is checked here and is not saved.")


# Function to check password
def check_password(password):

    score = 0
    feedback = []

    if len(password) >= 12:
        score += 20
    else:
        feedback.append("Use at least 12 characters.")

    if re.search("[A-Z]", password):
        score += 20
    else:
        feedback.append("Add one capital letter.")

    if re.search("[a-z]", password):
        score += 20
    else:
        feedback.append("Add one small letter.")

    if re.search("[0-9]", password):
        score += 20
    else:
        feedback.append("Add one number.")

    if re.search("[^A-Za-z0-9]", password):
        score += 20
    else:
        feedback.append("Add one special character like @ or #.")

    if score <= 40:
        strength = "Weak"
    elif score <= 80:
        strength = "Medium"
    else:
        strength = "Strong"

    return score, strength, feedback


# Enter password
password = st.text_input(
    "Enter your password",
    type="password",
    placeholder="Type password here..."
)


# Check button
if st.button("Check Password"):

    if password == "":
        st.warning("Please enter a password.")

    else:
        score, strength, feedback = check_password(password)

        st.subheader("Result")

        st.metric("Password Score", f"{score}/100")
        st.progress(score / 100)

        if strength == "Weak":
            st.error("Your password is Weak.")

        elif strength == "Medium":
            st.warning("Your password is Medium.")

        else:
            st.success("Your password is Strong!")

        st.subheader("Suggestions")

        if feedback:
            for msg in feedback:
                st.write("⚠️", msg)
        else:
            st.success("Good! All five checks are passed.")


st.divider()
st.caption("Created using Python and Streamlit")
