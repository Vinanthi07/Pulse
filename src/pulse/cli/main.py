import typer

from pulse.attacks.prompt_injection import PromptInjectionAttack
from pulse.config import DEBUG
from pulse.metadata import get_version
from pulse.models.dummy import DummyModel
app = typer.Typer(invoke_without_command=True)
model = DummyModel()

@app.callback()
def main():
    """
    Pulse AI Security Evaluation & Research Platform.
    """
    print("Pulse")
    print("AI Security Evaluation & Research Platform")
    print(f"Version {get_version()}")
    print("Framework Initialized Successfully")

    if DEBUG:
        print("Running in DEBUG mode")

    attack = PromptInjectionAttack()

    print("\nRunning Attack:")
    print(attack.name)

    print("\nPayload:")
    print(attack.PAYLOAD)

    response = attack.execute(model)

    print("\nModel Response:")
    print(response)