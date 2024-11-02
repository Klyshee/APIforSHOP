from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config.config import Config
from routes.product_routes import product_bp
from routes.user_routes import user_bp

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)


with app.app_context():
    db.create_all()  


app.register_blueprint(product_bp)
app.register_blueprint(user_bp)

if __name__ == '__main__':
    app.run(debug=True)
