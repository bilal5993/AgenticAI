from src.langgraphagenticai.main import load_langgraph_agenticai_app
import os
from dotenv import load_dotenv
load_dotenv() ## aloading all the environment variable

os.environ["TAVILY_API_KEY"]=os.getenv("TAVILY_API_KEY")
os.environ["GROQ_API_KEY"]=os.getenv("GROQ_API_KEY")

if __name__=="__main__":
    load_langgraph_agenticai_app()