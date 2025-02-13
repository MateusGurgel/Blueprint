import typer

from blprint.modules.blueprints.commands.create.create_command import app as create_app

app = typer.Typer()

app.add_typer(create_app)

def main():
    app()

if __name__ == "__main__":
    app()