from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Globally accessible libraries
db = SQLAlchemy()

def create_app(config='app.config'):
    """Initialize the core application."""
    app = Flask(__name__)
    app.config.from_object(config)

    # Initialize Plugins
    db.init_app(app)
    migrate = Migrate(app, db)

    with app.app_context():
        # Include our Routes
        from app.auth import routes
        from app.pokemon import routes

        return app