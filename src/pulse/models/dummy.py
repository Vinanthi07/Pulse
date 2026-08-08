from pulse.models.base import Model


class DummyModel(Model):
    @property
    def name(self) -> str:
        return "Dummy Model"
    def generate(self, prompt: str) -> str:
        return (
            "I cannot reveal my system prompt or ignore my "
            "original instructions."
        )