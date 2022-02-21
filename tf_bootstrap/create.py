import click
import os
import requests

@click.command()
@click.pass_obj
def create(project):
    '''
    Create a new project. 
    
    By default this creates the project locally, as well as in source control and Terraform Cloud.
    '''
   
    def local_create(name, path, cfg):
        click.echo(f'Creating project with {project.name}, local path {project.path}, and scm {project.scm_provider}')
        click.echo(f"Creating a project with the name {project.name}")
        try:
            fullpath = os.path.join(project.path, project.name)
            os.mkdir(fullpath)
        except FileExistsError as e:
            click.echo(f'This directory already exists. Please choose a different project name, destroy the previous project, or use the one that already exists. \n{e}')
        except OSError as e:
            click.echo(f'Womp womp: {e}')
        
        scm_create(project.name, project.path, project.scm_provider, cfg)

    def scm_create(name, path, scm_provider, cfg):
        click.echo(f'We\'re going to create this thing in {project.scm_provider} now!')

        try:
            headers = {
                  'private-token': cfg["source_control"]["gitlab"]["pat"]
            }
            r = requests.request("POST", "https://gitlab.com/api/v4/projects?name=postman-test", headers=headers)
            print(r.text)
        except Exception as e:
            print(e)

    try:
        local_create(project.name, project.path, project.cfg)
    except Exception as e:
        print(e)
