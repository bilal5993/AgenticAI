import streamlit as st
import os

from src.langgraphagenticai.ui.uiconfigfile import Config

class LoadStreamlitUI:
    def __init__(self):
        self.config=Config()
        self.user_controls={}

    def login(self):
        """Login form using Streamlit secrets"""
        st.sidebar.subheader("Login")
        username = st.sidebar.text_input("Username")
        password = st.sidebar.text_input("Password", type="password")
        login_btn = st.sidebar.button("Login")

        if login_btn:
            users = st.secrets["users"]
            if username in users and password == users[username]:
                st.session_state["logged_in"] = True
                st.session_state["username"] = username
                # Auto-populate GROQ API key from secrets
                st.session_state["GROQ_API_KEY"] = st.secrets["GROQ"]["api_key"]
                # st.success(f"Logged in as {username}")
            else:
                st.session_state["logged_in"] = False
                st.error("❌ Invalid username or password")


    def load_streamlit_ui(self):
        # Check if user is logged in
        if "logged_in" not in st.session_state or not st.session_state["logged_in"]:
            self.login()
            return  # Stop loading rest of UI until login succeeds
        
        st.set_page_config(page_title= "🤖 " + self.config.get_page_title(), layout="wide")
        st.header("🤖 " + self.config.get_page_title())
        st.markdown("<i style='color:gray;'>This chatbot has been developed by <b>Bilal Bhat</b> and will be continuously enhanced into a more advanced agentic AI system. It is currently in an active development phase.</i>",
                    unsafe_allow_html=True)



        with st.sidebar:
            # Get options from config
            llm_options = self.config.get_llm_options()
            usecase_options = self.config.get_usecase_options()

            # LLM selection
            self.user_controls["selected_llm"] = st.selectbox("Select LLM", llm_options)

            if self.user_controls["selected_llm"] == 'Groq':
                # Model selection
                model_options = self.config.get_groq_model_options()
                self.user_controls["selected_groq_model"] = st.selectbox("Select Model", model_options)
                # self.user_controls["GROQ_API_KEY"] = st.session_state["GROQ_API_KEY"]=st.text_input("API Key",type="password")

                # Use API key from session_state (auto-populated)
                self.user_controls["GROQ_API_KEY"] = st.session_state["GROQ_API_KEY"]
                st.text_input("API Key", value=self.user_controls["GROQ_API_KEY"], type="password", disabled=True)

                # Validate API key
                if not self.user_controls["GROQ_API_KEY"]:
                    st.warning("⚠️ Please enter your GROQ API key to proceed. Don't have? refer : https://console.groq.com/keys ")
            
            ## USecase selection
            self.user_controls["selected_usecase"]=st.selectbox("Select Usecases",usecase_options)

            if self.user_controls["selected_usecase"] =="Chatbot with Web":
                os.environ["TAVILY_API_KEY"]=self.user_controls["TAVILY_API_KEY"]=st.session_state["TAVILY_API_KEY"]=st.text_input("TAVILY API KEY",type="password")

                # Validate API key
                if not self.user_controls["TAVILY_API_KEY"]:
                    st.warning("⚠️ Please enter your TAVILY_API_KEY key to proceed. Don't have? refer : https://app.tavily.com/home")

        return self.user_controls