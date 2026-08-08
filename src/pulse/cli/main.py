import typer
from pulse.core.evaluation import EvaluationContext
from pulse.attacks.prompt_injection import PromptInjectionAttack
from pulse.config import DEBUG
from pulse.metadata import get_version
from pulse.models.dummy import DummyModel
from pulse.evaluators.prompt_injection import PromptInjectionEvaluator
app = typer.Typer(invoke_without_command=True)
model = DummyModel()
evaluator = PromptInjectionEvaluator()
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
    context = EvaluationContext(
    attack=attack.name,
    model=model.name,
    payload=attack.PAYLOAD,
    response=response,
)
    result = evaluator.evaluate(context)
    print("\nModel Response:")
    print(response)
    print("\nEvaluation Result")
    print("-----------------")
    print(f"Attack   : {result.attack}")
    print(f"Model    : {result.model}")
    print(f"Payload  : {result.payload}")
    print(f"Response : {result.response}")
    print(f"Verdict  : {result.verdict}")
    print(f"Reason   : {result.reason}")