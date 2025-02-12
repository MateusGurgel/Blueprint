from pathlib import Path
from typing import Dict, Any, Optional, Annotated

import typer

from modules.blueprints.instantiate_blueprint import instantiate_blueprint
from modules.templates.get_templates_from_blueprint import get_templates_from_blueprint

from modules.blueprints.get_blue_print_variables import get_blueprint_variables

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

    variables_list: list[str] = get_blueprint_variables(templates, blueprint_path)
    variables: dict[str, str] = {}

    for variable in variables_list:
        variables[variable] = input(f"Qual é o valor dá variável {variable}: ")

    instantiate_blueprint(templates, blueprint_path, destination, variables)