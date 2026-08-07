from abc import ABC, abstractmethod


class Model(ABC):
    @abstractmethod
    def generate(self, prompt: str) -> str:
        """Generate a response for the given prompt."""