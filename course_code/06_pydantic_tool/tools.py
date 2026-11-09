import httpx
from pydantic_ai import RunContext
from deps import WeatherDeps

def get_weather(ctx: RunContext[WeatherDeps], lat: float, lon: float) -> str:
    """get current weather for latitude and longitude"""
    response = httpx.get(
        "https://api.open-meteo.com/v1/forecast",
        params={"latitude": lat, "longitude": lon, "current": "temperature_2m"},
        timeout=30,
    )
    response.raise_for_status()
    current = response.json().get("current")
    temperature = current.get("temperature_2m")

    return f"Current temperature in {ctx.deps.city} is {temperature}°C"

def geocode(city: str) -> dict:
    response = httpx.get(
        "https://geocoding-api.open-meteo.com/v1/search",
        params={"name": city, "count": 1},
    )
    response.raise_for_status()
    place = response.json().get("results")[0]

    return {"latitude": place.get("latitude"), "longitude": place.get("longitude")}

#get_weather(WeatherDeps(city="London"),25,30)
#print(geocode("stockholm"))