from typing import Optional

from pydantic import BaseModel, Field


class SaveArticleRequest(BaseModel):
    title: str = Field(..., min_length=1, description="기사 제목")
    link: str = Field(..., min_length=1, description="기사 원문 URL")
    source: str = Field(default="", description="언론사 이름")
    snippet: Optional[str] = Field(default=None, description="기사 요약 스니펫 (검색 결과에서 제공되는 짧은 미리보기)")
    published_at: Optional[str] = Field(default=None, description="기사 발행일 (예: 2026-03-16)")

    model_config = {
        "json_schema_extra": {
            "example": {
                "title": "삼성전자, AI 반도체 신제품 발표",
                "link": "https://example.com/article/1",
                "source": "연합뉴스",
                "snippet": "삼성전자가 차세대 AI 반도체를 공개했다...",
                "published_at": "2026-03-16",
            }
        }
    }
