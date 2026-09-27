import os
import requests
from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(__file__), '.env'))

API_BASE_URL = "https://api.switch-bot.com"

SB_ACCESS_TOKEN:str = os.environ["SWITCHBOT_ACCESS_TOKEN"]
SB_SECRET_KEY:str = os.environ["SWITCHBOT_SECRET_KEY"]

