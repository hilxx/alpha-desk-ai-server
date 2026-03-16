from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Optional


@dataclass
class SavedArticle:
    title: str
    link: str
    source: str
    content: str
    snippet: Optional[str] = None
    published_at: Optional[str] = None
    summary: Optional[str] = None
    tags: List[str] = field(default_factory=list)
    confidence: Optional[float] = None
    id: Optional[int] = None
    saved_at: datetime = field(default_factory=datetime.now)
