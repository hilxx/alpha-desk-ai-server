from datetime import datetime
from typing import Optional

from app.domains.news_search.application.usecase.saved_article_repository_port import SavedArticleRepositoryPort
from app.domains.news_search.domain.entity.saved_article import SavedArticle


class FakeSavedArticleRepository(SavedArticleRepositoryPort):
    """DB 없이 인메모리로 동작하는 테스트용 저장소."""

    def __init__(self):
        self._store: dict[str, SavedArticle] = {}
        self._next_id = 1

    def save(self, article: SavedArticle) -> SavedArticle:
        article.id = self._next_id
        article.saved_at = datetime(2026, 3, 16, 10, 0, 0)
        self._next_id += 1
        self._store[article.link] = article
        return article

    def find_by_link(self, link: str) -> Optional[SavedArticle]:
        return self._store.get(link)
