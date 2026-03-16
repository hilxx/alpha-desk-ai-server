from typing import List, Optional

from pydantic import BaseModel, Field


class NewsArticleItem(BaseModel):
    title: str = Field(..., description="기사 제목")
    snippet: str = Field(..., description="기사 요약 스니펫")
    source: str = Field(..., description="언론사 이름")
    published_at: Optional[str] = Field(default=None, description="기사 발행일")
    link: Optional[str] = Field(default=None, description="기사 원문 URL")


class SearchNewsResponse(BaseModel):
    items: List[NewsArticleItem] = Field(..., description="검색된 기사 목록")
    total_count: int = Field(..., description="전체 검색 결과 수")
    page: int = Field(..., description="현재 페이지 번호")
    page_size: int = Field(..., description="페이지당 기사 수")

    model_config = {
        "json_schema_extra": {
            "example": {
                "items": [
                    {
                        "title": "삼성전자, AI 반도체 신제품 발표",
                        "snippet": "삼성전자가 차세대 AI 반도체를 공개했다...",
                        "source": "연합뉴스",
                        "published_at": "2026-03-16",
                        "link": "https://example.com/article/1",
                    }
                ],
                "total_count": 42,
                "page": 1,
                "page_size": 5,
            }
        }
    }
