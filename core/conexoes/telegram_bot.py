import requests
from core.utils.logger import registrar_log
from configs.credentials import TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID

def enviar_mensagem_telegram(mensagem):
    try:
        url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
        payload = {
            "chat_id": TELEGRAM_CHAT_ID,
            "text": mensagem,
            "parse_mode": "HTML"
        }
        response = requests.post(url, data=payload)
        if response.status_code != 200:
            raise Exception(response.text)
        registrar_log("Mensagem enviada para o Telegram.")
    except Exception as e:
        registrar_log(f"Erro ao enviar mensagem para o Telegram: {str(e)}")

def gerar_relatorio_campanha(nome_campanha, resultados):
    try:
        mensagem = f"<b>Relatório da campanha:</b> {nome_campanha}\n"
        mensagem += "<b>Resultados:</b>\n"
        for chave, valor in resultados.items():
            mensagem += f"• <b>{chave}:</b> {valor}\n"
        enviar_mensagem_telegram(mensagem)
    except Exception as e:
        registrar_log(f"Erro ao gerar relatório: {str(e)}")
