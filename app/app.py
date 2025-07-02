from flask import Flask
from prometheus_client import Counter, generate_latest

app = Flask(__name__)
visits = Counter('webapp_visits_total', 'Total de visitas a la página principal')

@app.route("/")
def hello():
    visits.inc()
    return "¡Hola, Prometheus!"

@app.route("/metrics")
def metrics():
    return generate_latest()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)