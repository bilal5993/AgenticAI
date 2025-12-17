from src.langgraphagenticai.main import load_langgraph_agenticai_app
import os
import streamlit as st
from dotenv import load_dotenv
load_dotenv() ## loading all the environment variable

if __name__=="__main__":
    load_langgraph_agenticai_app()