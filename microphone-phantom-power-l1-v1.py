import streamlit as st

# Title of the app
st.title("AKG Perception 150 Voltage Requirements")

# Display the voltage information
st.header("Voltage Specifications")
st.write("Here are the voltage requirements for the AKG Perception 150:")

# Using columns for a structured layout
col1, col2 = st.columns([1, 2])
with col1:
    st.subheader("Parameter")
    st.write("Phantom Power Range")
    st.write("Recommended Voltage")
    st.write("Current Draw")
with col2:
    st.subheader("Details")
    st.write("9V to 52V")
    st.write("48V (standard phantom power)")
    st.write("Approximately 2 mA")

# Additional description
st.markdown("""
The AKG Perception 150, a small-diaphragm condenser microphone, requires phantom power delivered via a balanced XLR cable from a compatible audio interface, mixer, or external power supply. The 48V setting is optimal and most commonly used.
""")

# Optional: Add a footer
st.write("---")
st.write("Information provided for the AKG Perception 150 microphone.")
