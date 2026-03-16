from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, Field


class SaveArticleResponse(BaseModel):
    id: int = Field(..., description="저장된 기사 고유 ID")
    title: str = Field(..., description="기사 제목")
    link: str = Field(..., description="기사 원문 URL")
    source: str = Field(..., description="언론사 이름")
    snippet: Optional[str] = Field(default=None, description="기사 요약 스니펫")
    content: str = Field(..., description="크롤링된 기사 본문 전문")
    summary: Optional[str] = Field(default=None, description="Claude AI가 생성한 3~5문장 한국어 요약")
    tags: List[str] = Field(default=[], description="Claude AI가 추출한 핵심 키워드 태그 (최대 5개)")
    confidence: Optional[float] = Field(default=None, description="Claude AI가 평가한 기사 신뢰도 (0.0 ~ 1.0)")
    published_at: Optional[str] = Field(default=None, description="기사 발행일")
    saved_at: datetime = Field(..., description="서버에 저장된 시각 (ISO 8601)")

    model_config = {
        "json_schema_extra": {
            "example": {
                "id": 1,
                "title": "삼성전자, AI 반도체 신제품 발표",
                "link": "https://example.com/article/1",
                "source": "연합뉴스",
                "snippet": "삼성전자가 차세대 AI 반도체를 공개했다...",
                "content": "삼성전자는 16일 서울 서초구 본사에서 기자간담회를 열고 차세대 AI 반도체 신제품을 공개했다...",
                "summary": "삼성전자가 차세대 AI 반도체 신제품을 공개했다. 해당 제품은 기존 대비 성능이 2배 향상됐으며, 전력 소비는 30% 줄었다. 회사는 올해 하반기 양산을 목표로 하고 있다.",
                "tags": ["삼성전자", "AI", "반도체", "신제품", "기술"],
                "confidence": 0.91,
                "published_at": "2026-03-16",
                "saved_at": "2026-03-16T10:00:00",
            }
        }
    }
