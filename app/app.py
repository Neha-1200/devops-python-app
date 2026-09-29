
from flask import Flask, jsonify
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST
import time

app = Flask(__name__)

REQUEST_COUNT = Counter(
    "app_http_requests_total",
    "Total HTTP requests",
    ["method", "endpoint", "status"],
)

REQUEST_LATENCY = Histogram(
    "app_http_request_duration_seconds",
    "HTTP request latency in seconds",
    ["method", "endpoint"],
)

@app.before_request
def start_timer():
    from flask import g
    g.start_time = time.perf_counter()

@app.after_request
def record_metrics(response):
    from flask import request, g
    endpoint = request.path
    elapsed = time.perf_counter() - getattr(g, "start_time", time.perf_counter())
    REQUEST_COUNT.labels(request.method, endpoint, response.status_code).inc()
    REQUEST_LATENCY.labels(request.method, endpoint).observe(elapsed)
    return response

@app.get("/")
def home():
    return jsonify(
        application="devops-python-app",
        message="Hello from Python!",
        version="1.0.0",
    )

@app.get("/health")
def health():
    return jsonify(status="UP"), 200

@app.get("/ready")
def ready():
    return jsonify(status="READY"), 200

@app.get("/metrics")
def metrics():
    return generate_latest(), 200, {"Content-Type": CONTENT_TYPE_LATEST}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
