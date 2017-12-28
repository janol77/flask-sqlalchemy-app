from flask import Flask
from db import db


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://test:test@localhost/test'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    from controllers.test import simple_page
    app.register_blueprint(simple_page)
    db.init_app(app)
    return app

app = create_app()

if __name__ == "__main__":
    app.run(host=app.config.get('HOST', '0.0.0.0'),
            port=app.config.get('PORT', 5000),
            debug=app.config.get('DEBUG', True)
            )
