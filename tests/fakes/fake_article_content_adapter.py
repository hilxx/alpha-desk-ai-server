from app.domains.news_search.application.usecase.article_content_port import ArticleContentPort

EXAMPLE_CONTENT = (
    "삼성전자는 16일 서울 서초구 본사에서 기자간담회를 열고 "
    "차세대 AI 반도체 신제품을 공개했다. 해당 제품은 기존 대비 "
    "성능이 2배 향상됐으며, 전력 소비는 30% 줄었다. "
    "회사는 올해 하반기 양산을 목표로 하고 있다."
)


class FakeArticleContentAdapter(ArticleContentPort):
    """HTTP 요청 없이 고정 본문을 반환하는 테스트용 어댑터."""

    def fetch_content(self, url: str) -> str:
        return EXAMPLE_CONTENT
