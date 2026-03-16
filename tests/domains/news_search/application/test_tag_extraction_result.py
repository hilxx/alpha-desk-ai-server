from tests.fakes.fake_tag_extraction_adapter import EXAMPLE_TAGS


class TestTagExtractionResult:
    def test_extract_tags_returns_list(self, fake_tag_extractor):
        result = fake_tag_extractor.extract_tags("삼성전자 AI 반도체 발표", "본문 내용")
        assert isinstance(result, list)

    def test_extract_tags_returns_non_empty(self, fake_tag_extractor):
        result = fake_tag_extractor.extract_tags("삼성전자 AI 반도체 발표", "본문 내용")
        assert len(result) > 0

    def test_extract_tags_all_strings(self, fake_tag_extractor):
        result = fake_tag_extractor.extract_tags("삼성전자 AI 반도체 발표", "본문 내용")
        assert all(isinstance(tag, str) for tag in result)

    def test_extract_tags_max_five(self, fake_tag_extractor):
        result = fake_tag_extractor.extract_tags("삼성전자 AI 반도체 발표", "본문 내용")
        assert len(result) <= 5

    def test_extract_tags_matches_example(self, fake_tag_extractor):
        result = fake_tag_extractor.extract_tags("어떤 제목이든", "어떤 내용이든")
        assert result == EXAMPLE_TAGS

    def test_normalized_article_tags_match_format(self, normalized_article):
        tags = normalized_article.tags
        assert isinstance(tags, list)
        assert 1 <= len(tags) <= 5
        assert all(isinstance(tag, str) and len(tag) > 0 for tag in tags)

    def test_normalized_article_tags_contain_expected_keywords(self, normalized_article):
        tags = normalized_article.tags
        assert "삼성전자" in tags
        assert "AI" in tags
        assert "반도체" in tags
