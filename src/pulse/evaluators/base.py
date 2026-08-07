from abc import ABC, abstractmethod


class Evaluator(ABC):
    @abstractmethod
    def evaluate(self, payload: str, response: str):
        """Evaluate a model's response to an attack."""