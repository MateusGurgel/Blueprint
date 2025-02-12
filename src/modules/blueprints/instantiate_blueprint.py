from pathlib import Path
from modules.templates.instantiate_template import instantiate_template



def instantiate_blueprint(templates: list[str], blueprint_path: Path, destination_path: Path):
    for template in templates:
        result: str = instantiate_template(template, blueprint_path, {"name": "Mateus"})
        print(result)