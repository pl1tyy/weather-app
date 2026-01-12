from fastapi import APIRouter, HTTPException
from app.services.weather_service import get_weather

router = APIRouter(prefix="/weather", tags=["weather"])

@router.get("/{city}")
async def weather_by_city(city: str):
    data = await get_weather(city)
    if not data:
        raise HTTPException(status_code=404, detail="City not found or API error")
    return data