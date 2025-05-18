import os
import json
import uuid
import time
import socket
from datetime import datetime
from core.utils.logger import log

def gerar_id():
    return str(uuid.uuid4())

def data_hora_atual():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def tem_conexao(host="8.8.8.8", port=53, timeout=3):
    try:
        socket.setdefaulttimeout(timeout)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
        return True
    except socket.error:
        return False

def esperar_conexao(max_tempo=300):
    log("Aguardando conexão com a internet...")
    tempo_inicial = time.time()
    while not tem_conexao():
        if time.time() - tempo_inicial > max_tempo:
            log("Tempo de espera excedido. Continuando em modo offline.")
            return False
        time.sleep(5)
    log("Conexão restabelecida!")
    return True

def salvar_json_local(nome, dados, pasta="dados"):
    try:
        os.makedirs(pasta, exist_ok=True)
        caminho = os.path.join(pasta, f"{nome}.json")
        with open(caminho, "w", encoding="utf-8") as f:
            json.dump(dados, f, indent=4, ensure_ascii=False)
        log(f"Arquivo salvo: {caminho}")
    except Exception as e:
        log(f"Erro ao salvar {nome}: {e}")

def carregar_json_local(nome, pasta="dados"):
    try:
        caminho = os.path.join(pasta, f"{nome}.json")
        if os.path.exists(caminho):
            with open(caminho, "r", encoding="utf-8") as f:
                return json.load(f)
        else:
            return {}
    except Exception as e:
        log(f"Erro ao carregar {nome}: {e}")
        return {}

def arquivo_ja_postado(nome, pasta="dados"):
    postados = carregar_json_local("postados", pasta)
    return nome in postados.get("ids", [])

def registrar_postagem(nome, pasta="dados"):
    postados = carregar_json_local("postados", pasta)
    postados.setdefault("ids", []).append(nome)
    salvar_json_local("postados", postados, pasta)
