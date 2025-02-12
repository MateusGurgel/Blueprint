from pathlib import Path

from jinja2 import Environment, FileSystemLoader, meta


def get_template_variables(template: str, blueprint_path: Path) -> set:
    env = Environment(loader=FileSystemLoader(blueprint_path))
    template_source = env.loader.get_source(env, template)
    parsed_content = env.parse(str(template_source))
    return meta.find_undeclared_variables(parsed_content)