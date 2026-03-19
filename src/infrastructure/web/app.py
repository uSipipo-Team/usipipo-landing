"""Flask application factory."""

from flask import Flask


def create_app() -> Flask:
    """Create and configure the Flask application."""
    app = Flask(
        __name__,
        template_folder="templates",
        static_folder="static",
    )

    # Configuration
    app.config.from_mapping(
        SECRET_KEY="dev-secret-key-change-in-production",
    )

    # Register blueprints
    from src.features.home.routes import home_bp
    from src.features.pricing.routes import pricing_bp
    from src.features.docs.routes import docs_bp
    from src.features.status.routes import status_bp

    app.register_blueprint(home_bp)
    app.register_blueprint(pricing_bp)
    app.register_blueprint(docs_bp)
    app.register_blueprint(status_bp)

    @app.route("/")
    def index():
        """Root endpoint."""
        from flask import redirect, url_for
        return redirect(url_for("home.index"))

    @app.route("/health")
    def health():
        """Health check endpoint."""
        return {"status": "healthy"}

    return app
