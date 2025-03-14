import streamlit as st
import re


def check_password_strength(password):
    length = len(password) >= 8
    digit = bool(re.search(r"\d", password))
    uppercase = bool(re.search(r"[A-Z]", password))
    lowercase = bool(re.search(r"[a-z]", password))
    special_char = bool(re.search(r"[@$!%*?&]", password))

    score = sum([length, digit, uppercase, lowercase, special_char])

    if score == 5:
        return "Very Strong", "green"
    elif score == 4:
        return "Strong", "blue"
    elif score == 3:
        return "Moderate", "orange"
    elif score == 2:
        return "Weak", "red"
    else:
        return "Very Weak", "darkred"

# Streamlit UI
st.title("🔒 Password Strength Meter")
st.write("Enter your password to check its strength.")

password = st.text_input("Enter Password", type="password")

if password:
    strength, color = check_password_strength(password)
    st.markdown(f"**Strength:** <span style='color:{color}; font-weight:bold;'>{strength}</span>", unsafe_allow_html=True)
    
    # Show strength criteria
    st.write("### Password Criteria:")
    st.write(f"{'✅' if len(password) >= 8 else '❌'} At least 8 characters")
    st.write(f"{'✅' if re.search(r'\\d', password) else '❌'} Contains a number")
    st.write(f"{'✅' if re.search(r'[A-Z]', password) else '❌'} Contains an uppercase letter")
    st.write(f"{'✅' if re.search(r'[a-z]', password) else '❌'} Contains a lowercase letter")
    st.write(f"{'✅' if re.search(r'[@$!%*?&]', password) else '❌'} Contains a special character (@$!%*?&)")

    # Save password option
    if st.button("Save Password"):
        st.success("Password saved successfully! (For demo, we are not actually saving it)")









