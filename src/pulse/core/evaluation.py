from dataclasses import dataclass


@dataclass
class EvaluationContext:
    attack: str
    model: str
    payload: str
    response: str