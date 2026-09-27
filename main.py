from switchbot import SwitchBotAPI
from dotenv import load_dotenv
import os

SB_ACCESS_TOKEN:str = os.environ["SWITCHBOT_ACCESS_TOKEN"]
SB_SECRET_KEY:str   = os.environ["SIWTCHBOT_SECRET_KEY"]