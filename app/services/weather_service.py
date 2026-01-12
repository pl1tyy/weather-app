# app/services/weather_service.py
import httpx
from app.core.config import settings
from app.utils.cache import cache

OPENWEATHER_URL = "http://api.openweathermap.org/data/2.5/weather"

async def get_weather(city: str) -> dict | None:
    cached = await cache.get(city)
    if cached:
        return cached
    async with httpx.AsyncClient() as client:
        params = {
            "q": city,
            "appid": settings.OPENWEATHER_API_KEY,
            "units": "metric"
        }
        response = await client.get(OPENWEATHER_URL, params=params)
        if response.status_code != 200:
            return None

        data = response.json()
        await cache.set(city, data)
        return data