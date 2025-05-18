import threading
import time
import os
from core.automacoes.campanha import executar_campanha
from core.utils.logger import log
from core.database.db_manager import salvar_status_campanha, carregar_campanhas_ativas
from core.utils.helpers import tem_conexao_internet

campanhas_em_execucao = {}

def iniciar_campanha(campanha_id, dados):
    def loop_campanha():
        while True:
            try:
                log(f"Iniciando execução da campanha {campanha_id}")
                status = executar_campanha(dados)
                salvar_status_campanha(campanha_id, status)
                log(f"Campanha {campanha_id} finalizada com status: {status}")

                if not tem_conexao_internet():
                    log("Sem internet. Salvando execução localmente...")
                    salvar_localmente(campanha_id, dados)

                time.sleep(30)  # Delay entre execuções da mesma campanha
            except Exception as e:
                log(f"Erro na campanha {campanha_id}: {str(e)}")
                time.sleep(10)

    thread = threading.Thread(target=loop_campanha)
    thread.daemon = True
    thread.start()
    campanhas_em_execucao[campanha_id] = thread

def salvar_localmente(campanha_id, dados):
    try:
        from datetime import datetime
        pasta_offline = "data/cache/"
        if not os.path.exists(pasta_offline):
            os.makedirs(pasta_offline)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        with open(f"{pasta_offline}offline_{campanha_id}_{timestamp}.txt", "w") as f:
            f.write(str(dados))
        log(f"Campanha {campanha_id} salva localmente")
    except Exception as e:
        log(f"Erro ao salvar localmente: {e}")

def iniciar_todas_campanhas():
    campanhas = carregar_campanhas_ativas()
    for campanha_id, dados in campanhas.items():
        if campanha_id not in campanhas_em_execucao:
            iniciar_campanha(campanha_id, dados)

def loop_global():
    log("Monitoramento global de campanhas iniciado.")
    while True:
        try:
            iniciar_todas_campanhas()
            time.sleep(60)
        except Exception as e:
            log(f"Erro no loop global: {str(e)}")
            time.sleep(15)
