import time
import os
import socket
from core.conexoes.telegram_bot import enviar_mensagem_telegram
from core.utils.logger import registrar_log

CAMPANHAS_ATIVAS = {}

def internet_esta_disponivel():
    try:
        socket.create_connection(("8.8.8.8", 53), timeout=3)
        return True
    except OSError:
        return False

def monitorar_campanhas():
    registrar_log("Monitoramento iniciado.")
    modo_offline = False

    while True:
        try:
            campanhas_ativas = list(CAMPANHAS_ATIVAS.values())
            status = f"Campanhas em execução: {len(campanhas_ativas)}"

            if not internet_esta_disponivel():
                if not modo_offline:
                    modo_offline = True
                    registrar_log("Conexão perdida. Modo offline ativado.")
                    enviar_mensagem_telegram("Alerta: Bot entrou em **modo offline**.")
            else:
                if modo_offline:
                    modo_offline = False
                    registrar_log("Conexão restabelecida. Modo online ativado.")
                    enviar_mensagem_telegram("Conexão restabelecida: Bot voltou ao **modo online**.")

            # Atualizar status no log a cada 1 minuto
            registrar_log(status)
            time.sleep(60)

        except Exception as e:
            registrar_log(f"Erro no monitoramento: {str(e)}")
            enviar_mensagem_telegram(f"Erro detectado no monitoramento: {str(e)}")
            time.sleep(60)
