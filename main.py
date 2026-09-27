import os
import requests
from dotenv import load_dotenv

import json
import time
import hashlib
import hmac
import base64
import uuid

load_dotenv(os.path.join(os.path.dirname(__file__), '.env'))

# MARK: - Constants

API_BASE_URL = "https://api.switch-bot.com"

SB_ACCESS_TOKEN:str = os.environ["SWITCHBOT_ACCESS_TOKEN"]
SB_SECRET_KEY:str = os.environ["SWITCHBOT_SECRET_KEY"]

# MARK - Functions

class SwitchBotAPI:
    def __init__(self, access_token: None, secret_key: None):
        self.access_token = access_token or SB_ACCESS_TOKEN
        self.secret_key = secret_key or SB_SECRET_KEY

    def generate_request_headers() -> dict:
        """
        SwitchBot API用のリクエストヘッダーを生成する関数
        """

        # ヘッダーを生成

        token   = SB_ACCESS_TOKEN
        secret  = SB_SECRET_KEY
        nonce   = str(uuid.uuid4())
        t = int(round(time.time() * 1000))
        string_to_sign = "{}{}{}".format(token, t, nonce)

        string_to_sign = bytes(string_to_sign, 'utf-8')
        secret = bytes(secret, 'utf-8')

        # 署名
        sign = base64.b64encode(
            hmac.new(
                secret,
                msg = string_to_sign,
                digestmod = hashlib.sha256
            ).digest()
        )

        # ヘッダー組み立て
        headers = {
            "Authorization": token,
            "Content-Type": "application/json",
            "charset": "utf-8",
            "t": str(t),
            "sign": sign.decode('utf-8'),
            "nonce": nonce
        }

        return headers
        

if __name__ == "__main__":
    print("init")