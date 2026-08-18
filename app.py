import streamlit as st
import os
from dotenv import load_file
from agent import FormSolverAgent

# Load environment variables from .env file for local testing
if os.path.exists(".env"):
    with open(".env") as f:
        for line in f:
            if "=" in line and not line.startswith("#"):
                key, val = line.strip().split("=", 1)
                os.environ[key] = val

# Configure Streamlit page layout
st.set_page_config(page_title="Form Solver AI Agent", page_icon="🤖", layout="wide")

st.title("🤖 Form Solver AI Agent")
st.caption("Scan form structures, identify bugs, and get instant code solutions.")

# Sidebar for configuration and open-source transparency
with st.sidebar:
    st.header("⚙️ Configuration")
    api_key_input = st.text_input("OpenAI API Key", type="password", help="Leave blank if set in environment variables.")
    
    # Override environment variable if user inputs a key via UI
    if api_key_input:
        os.environ["OPENAI_API_KEY"] = api_key_input
        
    st.divider()
    st.markdown("### 📄 About Project")
    st.markdown("This is an open-source project designed to automatically research form fields and fix broken code logic.")
    st.markdown("[⭐ Star on GitHub](https://github.com)")

# Main application interface
form_input = st.text_area(
    "Paste your Form Data here:", 
    placeholder="<form>\n  <input type='text' id='username' required>\n  <!-- Paste your HTML, JSON, or code schema here -->\n</form>",
    height=250
)

if st.button("🚀 Analyze & Solve Issues", type="primary"):
    if not form_input.strip():
        st.warning("Please paste some form data first.")
    else:
        with st.spinner("Agent is researching, thinking, and solving..."):
            try:
                # Initialize your existing agent logic
                agent = FormSolverAgent()
                result = agent.analyze_form(form_input)
                
                st.success("Analysis Complete!")
                st.markdown("### 🛠️ Agent Output")
                st.markdown(result)
            except Exception as e:
                st.error(f"Error running agent: {str(e)}")
