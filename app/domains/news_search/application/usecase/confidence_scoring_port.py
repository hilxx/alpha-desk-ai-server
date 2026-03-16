from abc import ABC, abstractmethod


class ConfidenceScoringPort(ABC):
    @abstractmethod
    def score(self, title: str, content: str) -> float:
        """Return a confidence score in the range [0.0, 1.0]."""
        pass
