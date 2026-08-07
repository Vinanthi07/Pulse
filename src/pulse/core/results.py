from dataclasses import dataclass


@dataclass
class AttackResult:
    attack: str
    model: str
    payload: str
    response: str
    verdict: str
    reason: str