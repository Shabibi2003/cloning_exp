# ... existing code ...
# Update the columns to add one more button
col1, col2, col3, col4, col5, col6 = st.columns(6)
with col1:
    if st.button('People EDS'):
        st.session_state.script_choice = "people"
with col2:
    if st.button('Extract Data'):
        st.session_state.script_choice = "data"
with col3:
    if st.button('Analytics'):
        st.session_state.script_choice = "visual"
with col4:
    if st.button('Device Data Details'):
        st.session_state.script_choice = "abdullah_work"
with col5:
    if st.button('Monthly Trends'):
        st.session_state.script_choice = "monthly_trends"
with col6:
    if st.button('Comparison Device'):
        st.session_state.script_choice = "comparison_device"

# ... existing code ...
# Add this at the end of the script choice conditions
elif st.session_state.script_choice == "comparison_device":
    st.header("Device Comparison")
    st.write("This section will allow you to compare data between different devices.")
// ... existing code ...