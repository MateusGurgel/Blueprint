from pathlib import Path
from jinja2 import Environment, FileSystemLoader

def instantiate_template(template: str, blueprint_path: Path, kwargs: dict) -> str:
    env = Environment(loader=FileSystemLoader(blueprint_path))
    template = env.get_template(template)
    rendered_str = template.render(**kwargs)
    return rendered_str