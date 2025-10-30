from pathlib import Path

from blprint.modules.templates.get_template_variables import get_template_variables


def get_all_blueprint_codes(templates: list[str], blueprint_path: Path) -> list[str]:
    variables = set()

    for template in templates:
        template_variables = get_template_variables(template, blueprint_path)
        variables.update(template_variables)

    return list(variables)
