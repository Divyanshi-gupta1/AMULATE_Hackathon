import streamlit as st
from ai_agent import ProductivityAgent

st.set_page_config(page_title="AI Student Productivity Agent")

st.title("AI Student Productivity Agent")
st.write("Enter a task and let the agent plan it for you.")

if "agent" not in st.session_state:
    st.session_state.agent = ProductivityAgent()

user_input = st.text_input("Enter a task (type exit to end session)")

if st.button("Submit") and user_input:
    if user_input.lower() in ["exit", "quit"]:
        st.warning("Session ended. You can close the tab or refresh to restart.")
    else:
        outputs = st.session_state.agent.run_and_collect_output(user_input)

        st.markdown("### Agent Output")
        for line in outputs:
            st.text(line)
