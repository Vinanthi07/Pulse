from abc import ABC, abstractmethod

from pulse.core.evaluation import EvaluationContext
from pulse.core.results import AttackResult


class Evaluator(ABC):
    @abstractmethod
    def evaluate(self, context: EvaluationContext) -> AttackResult:
        """Evaluate a model response."""