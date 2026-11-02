
from flask import Flask, jsonify
from app.logger import setup_logger

app = Flask(__name__)

logger = setup_logger()


@app.route("/")
def home():
    logger.info("Homepage accessed")

    return jsonify({
        "application": "Cloud DevOps Platform",
        "message": "Application is running"
    })


@app.route("/health")
def health():
    logger.info("Health endpoint accessed")

    return jsonify({"status": "healthy"}), 200


@app.errorhandler(404)
def not_found(error):
    logger.warning("Page not found: %s", error)

    return jsonify({
        "error": "Resource not found"
    }), 404


@app.errorhandler(500)
def internal_server_error(error):
    logger.error("Internal server error: %s", error)

    return jsonify({
        "error": "Internal server error"
    }), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)

