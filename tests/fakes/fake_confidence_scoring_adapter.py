from app.domains.news_search.application.usecase.confidence_scoring_port import ConfidenceScoringPort

EXAMPLE_CONFIDENCE: float = 0.91


class FakeConfidenceScoringAdapter(ConfidenceScoringPort):
    """Claude API를 호출하지 않는 테스트용 신뢰도 평가 어댑터."""

    def score(self, title: str, content: str) -> float:
        return EXAMPLE_CONFIDENCE
