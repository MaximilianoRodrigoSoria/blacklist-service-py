from flask import Flask
from src.routes.HealthRoute import health_route

app = Flask(__name__)
app.register_blueprint(health_route)

if __name__ == "__main__":
    app.run()