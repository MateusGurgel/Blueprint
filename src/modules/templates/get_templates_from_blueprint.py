from pathlib import Path


def get_templates_from_blueprint(blueprint_path: Path, blueprint: str) -> list[str]:

    if not blueprint_path.exists():
        raise ValueError(f"Blueprint {blueprint} does not exist")

    if not blueprint_path.is_dir():
        raise ValueError(f"Blueprint {blueprint} is not a directory")

    templates: list[str] = [path.name for path in blueprint_path.iterdir()]

    return templates