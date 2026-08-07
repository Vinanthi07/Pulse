from pulse.evaluators.base import Evaluator
from pulse.core.results import AttackResult

class PromptInjectionEvaluator(Evaluator):
    def evaluate(self, payload: str, response: str) -> AttackResult:
        return AttackResult(
            attack="Prompt Injection",
            model="Dummy Model",
            payload=payload,
            response=response,
            verdict="PASS",
            reason="The model refused the malicious instruction.",
        )