from flask import Blueprint


weather_blueprint = Blueprint("weather", __name__)
from . import views