import requests
import json
from core.utils.logger import log

class APIIntegrations:
    def __init__(self, tokens):
        self.tokens = tokens

    def monetizze_produtos(self):
        try:
            headers = {"Authorization": f"Bearer {self.tokens['monetizze']}"}
            response = requests.get("https://api.monetizze.com.br/2.1/products", headers=headers)
            if response.status_code == 200:
                log("Produtos Monetizze carregados com sucesso.")
                return response.json()
            else:
                log(f"Erro Monetizze: {response.status_code}")
                return None
        except Exception as e:
            log(f"Erro ao integrar com Monetizze: {e}")
            return None

    def hotmart_produtos(self):
        try:
            headers = {"Authorization": f"Bearer {self.tokens['hotmart']}"}
            response = requests.get("https://api-sec-vlc.hotmart.com/security/oauth/token", headers=headers)
            if response.status_code == 200:
                log("Produtos Hotmart carregados com sucesso.")
                return response.json()
            else:
                log(f"Erro Hotmart: {response.status_code}")
                return None
        except Exception as e:
            log(f"Erro ao integrar com Hotmart: {e}")
            return None

    def kwai_dados(self):
        try:
            # Exemplo fictício, personalize conforme sua integração
            headers = {"Authorization": f"Bearer {self.tokens['kwai']}"}
            response = requests.get("https://api.kwai.com/user/content", headers=headers)
            if response.status_code == 200:
                log("Dados Kwai obtidos.")
                return response.json()
            else:
                log(f"Erro Kwai: {response.status_code}")
                return None
        except Exception as e:
            log(f"Erro ao integrar com Kwai: {e}")
            return None

    def tiktok_dados(self):
        try:
            headers = {"Authorization": f"Bearer {self.tokens['tiktok']}"}
            response = requests.get("https://open-api.tiktok.com/user/info/", headers=headers)
            if response.status_code == 200:
                log("Dados TikTok obtidos.")
                return response.json()
            else:
                log(f"Erro TikTok: {response.status_code}")
                return None
        except Exception as e:
            log(f"Erro ao integrar com TikTok: {e}")
            return None
