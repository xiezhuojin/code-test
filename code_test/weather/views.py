from flask import request, current_app
import requests

from . import weather_blueprint


@weather_blueprint.route("/")
def get_weather_by_city():
    """Current weather of given city
    ---
    parameters:
      - name: city
        in: query
        type: string
        required: true
    responses:
      200:
        description:
    """

    city = request.args.get("city")

    params = {
        "q": city,
        "appid": current_app.config.get("OPEN_WEATHER_APPID")
    }
    try:
        resp = requests.get("https://api.openweathermap.org/data/2.5/weather", params=params)
    except requests.exceptions.RequestException as e:
        raise Exception(f"error fetching weather data {e}")
    else:
        data = resp.json()
        if data["cod"] != 200:
            raise Exception(data["message"])
        else:
            return data