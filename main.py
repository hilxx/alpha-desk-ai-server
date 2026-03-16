from fastapi import FastAPI

from app.domains.news_search.adapter.inbound.api.news_search_router import router as news_search_router
from app.domains.news_search.adapter.inbound.api.saved_article_router import router as saved_article_router
from app.domains.news_search.infrastructure.orm.saved_article_orm import SavedArticleORM  # noqa: F401
from app.domains.post.adapter.inbound.api.post_router import router as post_router
from app.domains.post.infrastructure.orm.post_orm import PostORM  # noqa: F401
from app.infrastructure.config.settings import Settings, get_settings
from app.infrastructure.database.session import Base, engine

settings: Settings = get_settings()

Base.metadata.create_all(bind=engine)

app = FastAPI(
    debug=settings.debug,
    title="Alpha Desk AI Server",
    description=(
        "뉴스 검색 및 기사 저장 API.\n\n"
        "저장 시 Claude AI가 **요약(summary)**, **태그(tags)**, **신뢰도(confidence)**를 자동 생성합니다."
    ),
    version="0.1.0",
)

app.include_router(post_router)
app.include_router(news_search_router)
app.include_router(saved_article_router)


@app.get("/")
async def root():
    return {"message": "Hello World"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=33333)
