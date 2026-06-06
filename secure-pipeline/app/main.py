from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/')
def home():
    # Production Grade Guardrail: Read configuration from environments
    app_env = os.getenv("APP_ENV", "Development")
    return jsonify({
        "status": "Healthy",
        "framework": "Flask",
        "environment": app_env,
        "message": "Welcome to the Secure IC Platform Sandbox!"
    })

if __name__ == '__main__':
    # Do not run with debug=True in production configurations
    app.run(host='0.0.0.0', port=8080)