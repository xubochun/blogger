import os
from dotenv import load_dotenv

# 載入 .env 檔案
load_dotenv()

# 讀取 API 金鑰從環境變數
api_key = os.getenv("api_key")

# 打印 API 金鑰
print("API 金鑰:", api_key)
