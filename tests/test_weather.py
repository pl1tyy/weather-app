import pytest
from httpx import AsyncClient
from app.main import app

@pytest.mark.asyncio
async def test_weather_endpoint():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/weather/London")
        assert response.status_code in (200, 404)