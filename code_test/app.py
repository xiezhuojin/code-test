from flask import Flask, jsonify, current_app, redirect
from werkzeug.exceptions import HTTPException
from flasgger import Swagger

from .weather import weather_blueprint
from .config import DefaultConfig


app = Flask(__name__)
app.config.from_object(DefaultConfig)

swwgger = Swagger(app)

@app.errorhandler(Exception)
def handle_exception(e):
    current_app.logger.exception(e)

    message = ""
    if isinstance(e, HTTPException):
        message = e.description
    else:
        message = str(e)
    response = jsonify({
        "error": message
    })
    response.status_code = getattr(e, "code", 500)

    return response

app.register_blueprint(weather_blueprint, url_prefix="/api/weather")