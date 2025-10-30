from pathlib import Path
from typing import Annotated

import typer

from blprint.modules.blueprints.collect_blueprint_values import (
    collect_blueprint_variables,
)
from blprint.modules.blueprints.format_blueprint_variables import (
    format_blueprint_variables,
)
from blprint.modules.blueprints.get_all_blueprint_codes import get_all_blueprint_codes
from blprint.modules.blueprints.instantiate_blueprint import instantiate_blueprint
from blprint.modules.templates.get_templates_from_blueprint import (
    get_templates_from_blueprint,
)

app = typer.Typer()


@app.command()
def create(
    blueprint_name: str,
    destination: Path,
    blueprint_folder_path: Annotated[Path, typer.Argument()] = Path("./blueprints"),
):
    if not destination.exists():
        raise typer.BadParameter(f"Destination {destination} does not exist")

    if not destination.is_dir():
        raise typer.BadParameter(f"Destination {destination} is not a directory")

    if not blueprint_folder_path.exists():
        raise typer.BadParameter(
            f"Blueprint path {blueprint_folder_path} does not exist"
        )

    blueprint_path: Path = Path(str(blueprint_folder_path) + "/" + blueprint_name)

    templates: list[str] = get_templates_from_blueprint(blueprint_path, blueprint_name)

    all_blueprint_codes: list[str] = get_all_blueprint_codes(templates, blueprint_path)

    blueprint_variable_names: list[str] = [
        code.split("__")[0] for code in all_blueprint_codes
    ]

    unique_blueprint_variable_names = list(set(blueprint_variable_names))

    blueprint_variables = collect_blueprint_variables(unique_blueprint_variable_names)

    formatted_blueprint_variables = format_blueprint_variables(
        all_blueprint_codes, blueprint_variables
    )

    instantiate_blueprint(
        templates, blueprint_path, destination, formatted_blueprint_variables
    )
