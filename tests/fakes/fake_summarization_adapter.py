from app.domains.news_search.application.usecase.summarization_port import SummarizationPort

EXAMPLE_SUMMARY = (
    "삼성전자가 차세대 AI 반도체 신제품을 공개했다. "
    "성능은 기존 대비 2배 향상되고 전력 소비는 30% 감소했다. "
    "회사는 올해 하반기 양산을 목표로 하고 있다."
)


class FakeSummarizationAdapter(SummarizationPort):
    """Claude API를 호출하지 않는 테스트용 요약 어댑터."""

    def summarize(self, content: str) -> str:
        return EXAMPLE_SUMMARY
