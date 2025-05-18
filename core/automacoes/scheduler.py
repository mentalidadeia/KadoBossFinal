import threading
import time
from core.automacoes.campanha import executar_campanha
from core.automacoes.monitor import CAMPANHAS_ATIVAS
from core.utils.logger import registrar_log

# Configurações de agendamento por nome de campanha
CAMPANHAS_CONFIG = {
    "campanha_afiliado_kawai": {"intervalo_min": 60},
    "campanha_hotmart_digital": {"intervalo_min": 90},
    "campanha_tiktok_sprints": {"intervalo_min": 75}
}

def iniciar_scheduler():
    registrar_log("Scheduler iniciado.")

    for nome, config in CAMPANHAS_CONFIG.items():
        thread = threading.Thread(target=loop_campanha, args=(nome, config["intervalo_min"]))
        thread.daemon = True
        thread.start()

def loop_campanha(nome, intervalo_min):
    while True:
        try:
            registrar_log(f"Iniciando execução da campanha: {nome}")
            CAMPANHAS_ATIVAS[nome] = True

            executar_campanha(nome)

            registrar_log(f"Campanha '{nome}' finalizada. Aguardando próximo ciclo...")
            time.sleep(intervalo_min * 60)  # tempo entre execuções
        except Exception as e:
            registrar_log(f"Erro na campanha '{nome}': {str(e)}")
            time.sleep(60)  # espera antes de tentar de novo em caso de erro
