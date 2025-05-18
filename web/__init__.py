from flask import Flask, render_template
import threading

app = Flask(__name__)

@app.route('/')
def painel():
    return render_template('index.html')

def iniciar_painel_web():
    thread = threading.Thread(target=lambda: app.run(host="0.0.0.0", port=5000, debug=False, use_reloader=False))
    thread.daemon = True
    thread.start()
