from datetime import datetime

import pytest

from app.domains.news_search.application.request.save_article_request import SaveArticleRequest
from app.domains.news_search.application.response.save_article_response import SaveArticleResponse
from app.domains.news_search.application.usecase.save_article_usecase import SaveArticleUseCase


@pytest.fixture
def save_article_usecase(
    fake_repository,
    fake_content_fetcher,
    fake_summarizer,
    fake_tag_extractor,
    fake_confidence_scorer,
) -> SaveArticleUseCase:
    return SaveArticleUseCase(
        repository=fake_repository,
        content_fetcher=fake_content_fetcher,
        summarizer=fake_summarizer,
        tag_extractor=fake_tag_extractor,
        confidence_scorer=fake_confidence_scorer,
    )


@pytest.fixture
def save_request() -> SaveArticleRequest:
    return SaveArticleRequest(
        title="삼성전자, AI 반도체 신제품 발표",
        link="https://example.com/article/1",
        source="연합뉴스",
        snippet="삼성전자가 차세대 AI 반도체를 공개했다...",
        published_at="2026-03-16",
    )


class TestSaveArticleResponseStructure:
    def test_response_type_is_correct(self, save_article_usecase, save_request):
        response = save_article_usecase.execute(save_request)
        assert isinstance(response, SaveArticleResponse)

    def test_id_is_assigned(self, save_article_usecase, save_request):
        response = save_article_usecase.execute(save_request)
        assert isinstance(response.id, int)
        assert response.id > 0

    def test_title_matches_request(self, save_article_usecase, save_request):
        response = save_article_usecase.execute(save_request)
        assert response.title == save_request.title

    def test_link_matches_request(self, save_article_usecase, save_request):
        response = save_article_usecase.execute(save_request)
        assert response.link == save_request.link

    def test_content_is_populated(self, save_article_usecase, save_request):
        response = save_article_usecase.execute(save_request)
        assert isinstance(response.content, str)
        assert len(response.content) > 0

    def test_summary_is_populated(self, save_article_usecase, save_request):
        response = save_article_usecase.execute(save_request)
        assert response.summary is not None
        assert len(response.summary) > 0

    def test_tags_is_non_empty_list(self, save_article_usecase, save_request):
        response = save_article_usecase.execute(save_request)
        assert isinstance(response.tags, list)
        assert len(response.tags) > 0
        assert all(isinstance(tag, str) for tag in response.tags)

    def test_confidence_is_valid_range(self, save_article_usecase, save_request):
        response = save_article_usecase.execute(save_request)
        assert response.confidence is not None
        assert 0.0 <= response.confidence <= 1.0

    def test_saved_at_is_datetime(self, save_article_usecase, save_request):
        response = save_article_usecase.execute(save_request)
        assert isinstance(response.saved_at, datetime)

    def test_duplicate_link_raises_409(self, save_article_usecase, save_request):
        from fastapi import HTTPException
        save_article_usecase.execute(save_request)
        with pytest.raises(HTTPException) as exc_info:
            save_article_usecase.execute(save_request)
        assert exc_info.value.status_code == 409
