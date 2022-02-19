import click
import os
from pathlib import Path

@click.option('--path', default="/Users/agency/git", help='Path to create the project directory in')
@click.argument('name')
@click.command()
def create(name, path):
    '''
    Create a new project. 
    
    By default this creates the project locally, as well as in GitHub and Terraform Cloud.
    '''
    
    click.echo(f"Creating a project with the name {name}")

    try:
        path = os.path.join(path, name)
        os.mkdir(path)
    except OSError as e:
        click.echo(f'Womp womp: {e}')
   