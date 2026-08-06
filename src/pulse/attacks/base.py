from abc import ABC, abstractmethod


class Attack(ABC):
    @property
    @abstractmethod
    def name(self) -> str:
        """Return the attack name."""

    @property
    @abstractmethod
    def description(self) -> str:
        """Return a short description of the attack."""

    @abstractmethod
    def execute(self) ->str:
        """Execute the attack."""