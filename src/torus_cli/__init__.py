import typer
import subprocess
import sys
from pathlib import Path

app = typer.Typer()

@app.command()
def run(notebook_path: str):
    """Execute a notebook with papermill inside /workspace."""
    nb_path = Path(notebook_path)
    if not nb_path.exists():
        typer.echo(f"Notebook not found: {notebook_path}", err=True)
        raise typer.Exit(1)
    try:
        result = subprocess.run([
            sys.executable, "-m", "papermill", str(nb_path), "/workspace/out.ipynb"
        ], check=True)
    except subprocess.CalledProcessError as e:
        typer.echo(f"Execution failed: {e}", err=True)
        raise typer.Exit(e.returncode)
    typer.echo("Notebook executed successfully.")
