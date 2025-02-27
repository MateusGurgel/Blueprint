import os
from pathlib import Path

from blprint.modules.templates.format_string import format_string
from blprint.modules.templates.instantiate_template import instantiate_template


def instantiate_blueprint(
        templates: list[str],
        blueprint_path: Path,
        destination_path: Path,
        template_variables: dict[str, str]
):
    for template in templates:
        template_content: str = instantiate_template(template, blueprint_path, template_variables)
        renamed_template = template.replace(".template", '')
        renamed_template = format_string(renamed_template, template_variables)

        template_instance_path: str = os.path.join(destination_path, renamed_template)

        with open(template_instance_path, 'w', encoding='utf-8') as file:
            file.write(template_content)
