from fastapi import APIRouter, Query

from app.domains.news_search.adapter.outbound.external.serp_news_search_adapter import SerpNewsSearchAdapter
from app.domains.news_search.application.response.search_news_response import SearchNewsResponse
from app.domains.news_search.application.usecase.search_news_usecase import SearchNewsUseCase

router = APIRouter(prefix="/news", tags=["news"])


@router.get(
    "/search",
    response_model=SearchNewsResponse,
    summary="뉴스 검색",
    description="키워드로 Google News를 검색합니다. 페이지네이션을 지원합니다.",
)
async def search_news(
    keyword: str = Query(..., min_length=1, description="검색 키워드 (예: AI반도체, 경제)"),
    page: int = Query(default=1, ge=1, description="페이지 번호 (1부터 시작)"),
    page_size: int = Query(default=10, ge=1, le=100, description="페이지당 기사 수 (최대 100)"),
):
    adapter = SerpNewsSearchAdapter()
    usecase = SearchNewsUseCase(adapter)
    return usecase.execute(keyword, page, page_size)
