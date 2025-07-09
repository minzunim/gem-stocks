# API 라우터 (저평가 종목 조회)
from fastapi import APIRouter
from app.services.filter import get_filtered_stocks

router = APIRouter()

@router.get("/stocks")
def get_stocks():
    """
    필터링된 저평가 종목 리스트 반환
    """
    return get_filtered_stocks()
