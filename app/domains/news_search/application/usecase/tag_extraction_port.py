from abc import ABC, abstractmethod
from typing import List


class TagExtractionPort(ABC):
    @abstractmethod
    def extract_tags(self, title: str, content: str) -> List[str]:
        pass
