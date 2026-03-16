import anthropic

from app.domains.news_search.application.usecase.confidence_scoring_port import ConfidenceScoringPort
from app.infrastructure.config.settings import get_settings

_MAX_CONTENT_CHARS = 4000


class ClaudeConfidenceScoringAdapter(ConfidenceScoringPort):
    def score(self, title: str, content: str) -> float:
        settings = get_settings()
        client = anthropic.Anthropic(api_key=settings.anthropic_api_key)

        truncated = content[:_MAX_CONTENT_CHARS]

        message = client.messages.create(
            model="claude-haiku-4-5-20251001",
            max_tokens=16,
            messages=[
                {
                    "role": "user",
                    "content": (
                        "다음 뉴스 기사의 내용이 얼마나 충실하고 신뢰할 수 있는지 평가해줘. "
                        "0.0(매우 낮음)에서 1.0(매우 높음) 사이의 숫자 하나만 출력해. "
                        "다른 텍스트는 절대 포함하지 마.\n\n"
                        f"제목: {title}\n\n"
                        f"본문: {truncated}"
                    ),
                }
            ],
        )

        raw = message.content[0].text.strip()
        try:
            value = float(raw)
            return max(0.0, min(1.0, value))
        except ValueError:
            return 0.0
