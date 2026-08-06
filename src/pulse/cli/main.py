import typer
from pulse.metadata import get_version
app = typer.Typer(invoke_without_command=True)
@app.callback()



def main():
    """
    Pulse AI Security Evaluation & Research Platform.
    """
    print("Pulse")
    print("AI Security Evaluation & Research Platform")
    print(f"Version {get_version()}")
    print("Framework Initialized Successfully")
from pulse.config import DEBUG    
print("Framework Initialized Successfully")
if DEBUG:
    print("Running in DEBUG mode")