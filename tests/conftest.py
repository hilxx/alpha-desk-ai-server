from datetime import datetime

import pytest

from app.domains.news_search.domain.entity.saved_article import SavedArticle
from tests.fakes.fake_summarization_adapter import FakeSummarizationAdapter


@pytest.fixture
def fake_summarizer() -> FakeSummarizationAdapter:
    return FakeSummarizationAdapter()


@pytest.fixture
def normalized_article() -> SavedArticle:
    """
    모든 필드가 채워진 정규화된 SavedArticle fixture.
    summary, tags, confidence 등 AI 생성 필드까지 포함한다.
    """
    return SavedArticle(
        id=1,
        title="삼성전자, AI 반도체 신제품 발표",
        link="https://example.com/article/1",
        source="연합뉴스",
        snippet="삼성전자가 차세대 AI 반도체를 공개했다...",
        content=(
            "삼성전자는 16일 서울 서초구 본사에서 기자간담회를 열고 "
            "차세대 AI 반도체 신제품을 공개했다. 해당 제품은 기존 대비 "
            "성능이 2배 향상됐으며, 전력 소비는 30% 줄었다."
        ),
        summary=(
            "삼성전자가 차세대 AI 반도체 신제품을 공개했다. "
            "성능은 2배 향상되고 전력 소비는 30% 감소했다. "
            "올해 하반기 양산을 목표로 하고 있다."
        ),
        tags=["삼성전자", "AI", "반도체", "신제품", "기술"],
        confidence=0.91,
        published_at="2026-03-16",
        saved_at=datetime(2026, 3, 16, 10, 0, 0),
    )
