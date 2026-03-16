from app.domains.news_search.domain.entity.saved_article import SavedArticle


class TestNormalizedArticleFixture:
    def test_fixture_returns_saved_article(self, normalized_article):
        assert isinstance(normalized_article, SavedArticle)

    def test_required_fields_are_present(self, normalized_article):
        assert normalized_article.id == 1
        assert normalized_article.title == "삼성전자, AI 반도체 신제품 발표"
        assert normalized_article.link == "https://example.com/article/1"
        assert normalized_article.source == "연합뉴스"
        assert normalized_article.content != ""

    def test_summary_is_defined(self, normalized_article):
        assert normalized_article.summary is not None
        assert len(normalized_article.summary) > 0

    def test_tags_is_non_empty_list(self, normalized_article):
        assert isinstance(normalized_article.tags, list)
        assert len(normalized_article.tags) > 0
        assert all(isinstance(tag, str) for tag in normalized_article.tags)

    def test_confidence_is_valid_range(self, normalized_article):
        assert normalized_article.confidence is not None
        assert 0.0 <= normalized_article.confidence <= 1.0

    def test_optional_fields_are_present(self, normalized_article):
        assert normalized_article.snippet is not None
        assert normalized_article.published_at is not None
        assert normalized_article.saved_at is not None
