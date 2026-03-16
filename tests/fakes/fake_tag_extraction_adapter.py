from typing import List

from app.domains.news_search.application.usecase.tag_extraction_port import TagExtractionPort

EXAMPLE_TAGS: List[str] = ["삼성전자", "AI", "반도체", "신제품", "기술"]


class FakeTagExtractionAdapter(TagExtractionPort):
    """Claude API를 호출하지 않는 테스트용 태그 추출 어댑터."""

    def extract_tags(self, title: str, content: str) -> List[str]:
        return EXAMPLE_TAGS
