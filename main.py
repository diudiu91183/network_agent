import streamlit as st
from network_diagnosis_agent import diagnose_network_issue
import sys
from io import StringIO
import contextlib


def capture_and_display_output():
    """
    This function captures print statements from the diagnosis function
    and displays them in real-time in the Streamlit app.
    """
    # Create a string buffer to capture print output
    string_buffer = StringIO()
    
    # Redirect stdout to our buffer
    with contextlib.redirect_stdout(string_buffer):
        try:
            # Call the diagnosis function which will print to our buffer
            result = diagnose_network_issue(st.session_state.user_input)
            
            # After the function completes, get all captured output
            output = string_buffer.getvalue()
            
            # Display the captured output (the intermediate steps)
            if output.strip():
                st.subheader("诊断过程:")
                st.code(output, language="text")
            
            # Display the final result
            st.subheader("诊断结果:")
            st.success(result)

        except Exception as e:
            st.error(f"诊断过程中发生错误: {str(e)}")


def main():
    st.set_page_config(page_title="🖥网络故障诊断 Agent🔎", layout="centered")
    st.title("🌏网络故障诊断 Agent🔎")

    # Initialize session state for user input if it doesn't exist
    if 'user_input' not in st.session_state:
        st.session_state.user_input = ""

    # User input section
    st.header("请输入网络问题：")
    user_input = st.text_area(
        "问题描述", 
        value=st.session_state.user_input,
        height=150,
        placeholder="示例：无法访问公司官网，浏览器报错连接超时。"
    )
    
    # Update session state with the current input
    st.session_state.user_input = user_input

    # Button to trigger diagnosis
    if st.button("开始诊断🚀", type="primary", use_container_width=True):
        if not st.session_state.user_input.strip():
            st.warning("请输入您的网络问题后再点击诊断。")
        else:
            # Disable button by showing status
            with st.spinner('AI正在诊断中，请稍等...'):
                # Capture and display output during diagnosis
                capture_and_display_output()


if __name__ == "__main__":
    main()