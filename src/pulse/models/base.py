from abc import ABC, abstractmethod


class Model(ABC):
    @property
    @abstractmethod
    def name(self) -> str:
        """Return the model name."""

    @abstractmethod
    def generate(self, prompt: str) -> str:
        """Generate a response for the given prompt."""