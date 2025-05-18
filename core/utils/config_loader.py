import json
import os

def carregar_config():
    caminho = os.path.join("configs", "settings.json")
    if not os.path.exists(caminho):
        raise FileNotFoundError(f"Arquivo de configuração não encontrado: {caminho}")
    with open(caminho, "r", encoding="utf-8") as f:
        return json.load(f)
