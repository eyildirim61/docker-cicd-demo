from flask import Flask, jsonify
import os
import platform
from datetime import datetime

app = Flask(__name__)


@app.route("/")
def index():
    return jsonify({
        "app": "Docker CI/CD Demo",
        "version": os.getenv("APP_VERSION", "1.0.0"),
        "status": "running"
    })


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "timestamp": datetime.utcnow().isoformat()
    })


@app.route("/info")
def info():
    return jsonify({
        "python_version": platform.python_version(),
        "system": platform.system(),
        "environment": os.getenv("ENVIRONMENT", "development"),
        "version": os.getenv("APP_VERSION", "1.0.0"),
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
