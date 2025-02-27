from jinja2 import Template

def format_string(string: str, variables: dict) -> str:
    template = Template(string)
    return template.render(**variables)
