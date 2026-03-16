from fastapi import HTTPException

from app.domains.news_search.application.request.save_article_request import SaveArticleRequest
from app.domains.news_search.application.response.save_article_response import SaveArticleResponse
from app.domains.news_search.application.usecase.article_content_port import ArticleContentPort
from app.domains.news_search.application.usecase.confidence_scoring_port import ConfidenceScoringPort
from app.domains.news_search.application.usecase.saved_article_repository_port import SavedArticleRepositoryPort
from app.domains.news_search.application.usecase.summarization_port import SummarizationPort
from app.domains.news_search.application.usecase.tag_extraction_port import TagExtractionPort
from app.domains.news_search.domain.entity.saved_article import SavedArticle


class SaveArticleUseCase:
    def __init__(
        self,
        repository: SavedArticleRepositoryPort,
        content_fetcher: ArticleContentPort,
        summarizer: SummarizationPort,
        tag_extractor: TagExtractionPort,
        confidence_scorer: ConfidenceScoringPort,
    ):
        self._repository = repository
        self._content_fetcher = content_fetcher
        self._summarizer = summarizer
        self._tag_extractor = tag_extractor
        self._confidence_scorer = confidence_scorer

    def execute(self, request: SaveArticleRequest) -> SaveArticleResponse:
        existing = self._repository.find_by_link(request.link)
        if existing:
            raise HTTPException(status_code=409, detail="이미 저장된 기사입니다.")

        content = self._content_fetcher.fetch_content(request.link)
        summary = self._summarizer.summarize(content) if content else None
        tags = self._tag_extractor.extract_tags(request.title, content) if content else []
        confidence = self._confidence_scorer.score(request.title, content) if content else None

        article = SavedArticle(
            title=request.title,
            link=request.link,
            source=request.source,
            snippet=request.snippet,
            published_at=request.published_at,
            content=content,
            summary=summary,
            tags=tags,
            confidence=confidence,
        )

        saved = self._repository.save(article)

        return SaveArticleResponse(
            id=saved.id,
            title=saved.title,
            link=saved.link,
            source=saved.source,
            snippet=saved.snippet,
            content=saved.content,
            summary=saved.summary,
            tags=saved.tags,
            confidence=saved.confidence,
            published_at=saved.published_at,
            saved_at=saved.saved_at,
        )
