from flask import Flask
from routes.product_routes import product_bp
from config import Config


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Register blueprints without a prefix
    app.register_blueprint(product_bp)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=8080, debug=True)