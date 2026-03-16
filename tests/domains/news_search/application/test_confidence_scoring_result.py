from tests.fakes.fake_confidence_scoring_adapter import EXAMPLE_CONFIDENCE


class TestConfidenceScoringResult:
    def test_score_returns_float(self, fake_confidence_scorer):
        result = fake_confidence_scorer.score("삼성전자 AI 반도체 발표", "본문 내용")
        assert isinstance(result, float)

    def test_score_is_within_valid_range(self, fake_confidence_scorer):
        result = fake_confidence_scorer.score("삼성전자 AI 반도체 발표", "본문 내용")
        assert 0.0 <= result <= 1.0

    def test_score_matches_example(self, fake_confidence_scorer):
        result = fake_confidence_scorer.score("어떤 제목이든", "어떤 내용이든")
        assert result == EXAMPLE_CONFIDENCE

    def test_score_is_not_zero(self, fake_confidence_scorer):
        result = fake_confidence_scorer.score("삼성전자 AI 반도체 발표", "본문 내용")
        assert result > 0.0

    def test_normalized_article_confidence_is_valid(self, normalized_article):
        assert normalized_article.confidence is not None
        assert isinstance(normalized_article.confidence, float)
        assert 0.0 <= normalized_article.confidence <= 1.0

    def test_normalized_article_confidence_is_high(self, normalized_article):
        assert normalized_article.confidence >= 0.7, "정규화된 기사의 신뢰도는 0.7 이상이어야 한다"
