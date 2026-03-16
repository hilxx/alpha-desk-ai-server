from tests.fakes.fake_summarization_adapter import EXAMPLE_SUMMARY


class TestSummarizationResult:
    def test_summarize_returns_string(self, fake_summarizer):
        result = fake_summarizer.summarize("삼성전자는 16일 신제품을 발표했다.")
        assert isinstance(result, str)

    def test_summarize_returns_non_empty(self, fake_summarizer):
        result = fake_summarizer.summarize("삼성전자는 16일 신제품을 발표했다.")
        assert len(result.strip()) > 0

    def test_summarize_matches_example(self, fake_summarizer):
        result = fake_summarizer.summarize("어떤 내용이든")
        assert result == EXAMPLE_SUMMARY

    def test_summary_contains_key_sentences(self, fake_summarizer):
        result = fake_summarizer.summarize("삼성전자는 16일 신제품을 발표했다.")
        assert "삼성전자" in result
        assert "반도체" in result

    def test_normalized_article_summary_matches_format(self, normalized_article):
        summary = normalized_article.summary
        assert summary is not None
        sentences = [s.strip() for s in summary.split(".") if s.strip()]
        assert len(sentences) >= 2, "요약은 최소 2문장 이상이어야 한다"
