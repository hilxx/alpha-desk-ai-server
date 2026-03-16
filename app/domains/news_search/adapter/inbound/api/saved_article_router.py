from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.domains.news_search.adapter.outbound.external.article_content_adapter import ArticleContentAdapter
from app.domains.news_search.adapter.outbound.external.claude_confidence_scoring_adapter import ClaudeConfidenceScoringAdapter
from app.domains.news_search.adapter.outbound.external.claude_summarization_adapter import ClaudeSummarizationAdapter
from app.domains.news_search.adapter.outbound.external.claude_tag_extraction_adapter import ClaudeTagExtractionAdapter
from app.domains.news_search.adapter.outbound.persistence.saved_article_repository_impl import SavedArticleRepositoryImpl
from app.domains.news_search.application.request.save_article_request import SaveArticleRequest
from app.domains.news_search.application.response.save_article_response import SaveArticleResponse
from app.domains.news_search.application.usecase.save_article_usecase import SaveArticleUseCase
from app.infrastructure.database.session import get_db

router = APIRouter(prefix="/news", tags=["news"])


@router.post(
    "/saved",
    response_model=SaveArticleResponse,
    status_code=201,
    summary="기사 저장",
    description=(
        "기사 URL을 받아 본문을 크롤링하고 저장합니다.\n\n"
        "저장 시 Claude AI가 자동으로 **요약**, **태그**, **신뢰도**를 생성합니다.\n\n"
        "- **409**: 이미 저장된 기사 (동일 URL)"
    ),
    responses={
        409: {"description": "이미 저장된 기사입니다.", "content": {"application/json": {"example": {"detail": "이미 저장된 기사입니다."}}}},
    },
)
async def save_article(request: SaveArticleRequest, db: Session = Depends(get_db)):
    repository = SavedArticleRepositoryImpl(db)
    content_fetcher = ArticleContentAdapter()
    summarizer = ClaudeSummarizationAdapter()
    tag_extractor = ClaudeTagExtractionAdapter()
    confidence_scorer = ClaudeConfidenceScoringAdapter()
    usecase = SaveArticleUseCase(repository, content_fetcher, summarizer, tag_extractor, confidence_scorer)
    return usecase.execute(request)
