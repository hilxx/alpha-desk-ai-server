import json
from typing import List

import anthropic

from app.domains.news_search.application.usecase.tag_extraction_port import TagExtractionPort
from app.infrastructure.config.settings import get_settings

_MAX_CONTENT_CHARS = 4000


class ClaudeTagExtractionAdapter(TagExtractionPort):
    def extract_tags(self, title: str, content: str) -> List[str]:
        settings = get_settings()
        client = anthropic.Anthropic(api_key=settings.anthropic_api_key)

        truncated = content[:_MAX_CONTENT_CHARS]

        message = client.messages.create(
            model="claude-haiku-4-5-20251001",
            max_tokens=128,
            messages=[
                {
                    "role": "user",
                    "content": (
                        "다음 뉴스 기사의 제목과 본문을 읽고, "
                        "핵심 키워드 태그를 최대 5개 추출해줘. "
                        "JSON 배열 형식으로만 출력해. 예시: [\"AI\", \"경제\", \"삼성\"]\n\n"
                        f"제목: {title}\n\n"
                        f"본문: {truncated}"
                    ),
                }
            ],
        )

        raw = message.content[0].text.strip()
        try:
            tags = json.loads(raw)
            if isinstance(tags, list):
                return [str(t) for t in tags]
        except (json.JSONDecodeError, ValueError):
            pass
        return []
