import os
import sys
from core.utils.logger import log
from core.utils.config_loader import carregar_config
from core.automacoes.campanha import executar_campanhas
from core.conexoes.telegram_bot import enviar_relatorio_telegram

def iniciar_kadoboss():
    log("Inicializando KadoBoss...")
    
    # Carrega as configurações
    config = carregar_config()

    # Executa as campanhas principais
    campanhas_resultados = executar_campanhas(config)

    # Envia o relatório da campanha por Telegram
    enviar_relatorio_telegram(campanhas_resultados)

    log("KadoBoss finalizou a execução.")

if __name__ == "__main__":
    try:
        iniciar_kadoboss()
    except Exception as e:
        log(f"Erro durante execução: {str(e)}")
