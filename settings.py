import os
from dotenv import load_dotenv

load_dotenv()


class Config():
    bot_token = os.getenv('BOT_TOKEN')
    request_kwargs = {
        'proxy_url': os.getenv('PROXY_URL'),
        'urllib3_proxy_kwargs': {'username': os.getenv('PROXY_USERNAME'), 'password': os.getenv('PROXY_PASSWORD')},
    }
