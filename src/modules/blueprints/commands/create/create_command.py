from pathlib import Path
from typing import Dict, Any, Optional, Annotated

import typer

from modules.blueprints.instantiate_blueprint import instantiate_blueprint
from modules.templates.get_templates_from_blueprint import get_templates_from_blueprint

app = typer.Typer()

@app.command()
def create(
        blueprint_name: str,
        destination: Path,
        blueprint_folder_path: Annotated[Optional[Path], typer.Argument()] = "./blueprints"
):

    if not destination.exists():
        raise typer.BadParameter(f"Destination {destination} does not exist")

    if not destination.is_dir():
        raise typer.BadParameter(f"Destination {destination} is not a directory")

    if not blueprint_folder_path.exists():
        raise typer.BadParameter(f"Blueprint path {blueprint_folder_path} does not exist")

    blueprint_path: Path = Path(str(blueprint_folder_path) + '/' + blueprint_name)

    templates: list[str] = get_templates_from_blueprint(blueprint_path, blueprint_name)

    instantiate_blueprint(templates, blueprint_path, destination, {"name": "Mateus"})