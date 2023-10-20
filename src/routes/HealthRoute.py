from flask import Blueprint

#Se registra la ruta
health_route = Blueprint("health", __name__)

@health_route.route('/health')
def health():
    return "Hola Mundo!!!"