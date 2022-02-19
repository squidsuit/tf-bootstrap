import click
import os, shutil
from pathlib import Path

@click.option('--path', default="/Users/agency/git", help='Path to destroy the project directory in')
@click.argument('name')
@click.command()
def destroy(name, path):
    '''
    Destroy a project

    By default this destroys the project locally, as well as in GitHub and Terraform Cloud.
    '''
    
    click.echo(f'Destroying a project with the name {name}')
    click.confirm(f'Are you sure you want to destroy the project named {name} located at {path}?', abort=True)

    try:
        path = os.path.join(path, name)
        if Path(path).iterdir():
            shutil.rmtree(path)
        else:
            os.rmdir(path)            
    except OSError as e:
        click.echo(f'Womp womp: {e}')
