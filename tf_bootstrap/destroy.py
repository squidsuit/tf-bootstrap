import click
import requests
import os, shutil
from pathlib import Path

@click.command()
@click.pass_obj
def destroy(project):
    '''
    Destroy a project

    By default this destroys the project locally, as well as in source control and Terraform Cloud.
    '''

    def local_destroy(project, cfg):

        click.echo(f'Destroying a project with the name {project.name}')
        click.confirm(f'Are you sure you want to destroy the project named {project.name} located at {project.path}?', abort=True)

        try:
            fullpath = os.path.join(project.path, project.name)
            if Path(fullpath).iterdir():
                shutil.rmtree(fullpath)
            else:
                os.rmdir(fullpath)            
        except OSError as e:
            click.echo(f'Womp womp: {e}')

        scm_destroy(project, cfg)

    def scm_destroy(project, cfg):

        click.echo(f'We\'re going to destroy this thing in {project.scm_provider} now.')

        url = "https://gitlab.com/api/v4/projects/exoskeleton%2F" + project.name 

        try:
            headers = {
                  'private-token': cfg["source_control"]["gitlab"]["pat"]
            }
            r = requests.request("DELETE", url, headers=headers)
            print(r.text)
        except Exception as e:
            print(e)

        tfc_destroy(project, cfg)

    def tfc_destroy(project, cfg):

        click.echo(f'Destroying this project in TFC.')

        url = "https://app.terraform.io/api/v2/organizations/" + cfg["terraform_cloud"]["workspace"] + "/workspaces/" + project.name

        try:
            headers = {
                'Content-Type': 'application/vnd.api+json',
                'Authorization': 'Bearer ' + cfg["terraform_cloud"]["bearer_token"]
            }
            r = requests.request("DELETE", url, headers=headers)
            print(r.text)
            print(f'Destroyed')            
        except Exception as e:
            print(e)

    try:
        local_destroy(project, project.cfg)
    except Exception as e:
        print(e)
