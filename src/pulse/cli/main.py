import typer

app = typer.Typer(invoke_without_command=True)


@app.callback()
def main():
    """
    Pulse AI Security Evaluation & Research Platform.
    """
    print("Pulse")
    print("AI Security Evaluation & Research Platform")
    print("Version 0.1.0")
    print("Framework Initialized Successfully")