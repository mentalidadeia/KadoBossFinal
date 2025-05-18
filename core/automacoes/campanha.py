import threading
import time
import random
import uuid
import os
from core.utils.logger import log
from core.utils.config_loader import carregar_config
from core.automacoes.monitor import monitorar_resultados
from core.conexoes.telegram_bot import enviar_mensagem_telegram
from core.automacoes.scheduler import reagendar_tarefa
from datetime import datetime

# Configurações gerais
CONFIG = carregar_config()
MODO_OFFLINE = CONFIG.get("modo_offline", True)
INTERVALO_PADRAO = CONFIG.get("intervalo_padrao", 3600)
CAMINHO_CAMPANHAS = "data/cache/campanhas/"

# Garante que o diretório existe
os.makedirs(CAMINHO_CAMPANHAS, exist_ok=True)

# Função principal da campanha
def executar_campanha(campanha_id, dados):
    log(f"Campanha {campanha_id} iniciada com dados: {dados}")

    while True:
        try:
            if not MODO_OFFLINE or verificar_conexao():
                # Aqui simularíamos a execução da campanha real
                log(f"Executando campanha {campanha_id}...")
                resultado = gerar_resultado_simulado(campanha_id)
                salvar_resultado_local(campanha_id, resultado)
                enviar_mensagem_telegram(f"Campanha {campanha_id} executada:\n{resultado}")
            else:
                log(f"Sem conexão. Campanha {campanha_id} salva para sincronizar depois.")

            monitorar_resultados(campanha_id)

        except Exception as e:
            log(f"Erro na campanha {campanha_id}: {str(e)}")

        time.sleep(random.randint(INTERVALO_PADRAO // 2, INTERVALO_PADRAO))

# Simula uma campanha com resultados falsos para teste
def gerar_resultado_simulado(campanha_id):
    retorno = {
        "campanha": campanha_id,
        "vendas": random.randint(0, 10),
        "cliques": random.randint(10, 100),
        "tempo_execucao": f"{random.randint(1, 3)}min",
        "timestamp": datetime.now().isoformat()
    }
    return retorno

# Salva localmente os resultados (para sincronizar depois se offline)
def salvar_resultado_local(campanha_id, resultado):
    path = os.path.join(CAMINHO_CAMPANHAS, f"{campanha_id}.json")
    with open(path, "a", encoding="utf-8") as f:
        f.write(str(resultado) + "\n")
    log(f"Resultado salvo para campanha {campanha_id}")

# Verifica se há internet (modo offline inteligente)
def verificar_conexao():
    try:
        import urllib.request
        urllib.request.urlopen("https://www.google.com", timeout=3)
        return True
    except:
        return False

# Inicia uma nova campanha em thread paralela
def iniciar_nova_campanha(dados):
    campanha_id = f"camp_{uuid.uuid4().hex[:8]}"
    thread = threading.Thread(target=executar_campanha, args=(campanha_id, dados), daemon=True)
    thread.start()
    log(f"Campanha {campanha_id} iniciada em segundo plano.")
    return campanha_id
