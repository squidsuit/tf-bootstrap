from email import header
import click
import json
import os
import requests

@click.command()
@click.pass_obj
def create(project):
    '''
    Create a new project. 
    
    By default this creates the project locally, as well as in source control and Terraform Cloud.
    '''
   
    def local_create(project, cfg):
        click.echo(f'Creating project with {project.name}, local path {project.path}, and scm {project.scm_provider}')
        click.echo(f"Creating a project with the name {project.name}")
        try:
            fullpath = os.path.join(project.path, project.name)
            os.makedirs(fullpath)
        except FileExistsError as e:
            click.echo(f'This directory already exists. Please choose a different project name, destroy the previous project, or use the one that already exists. \n{e}')
        except OSError as e:
            click.echo(f'Womp womp: {e}')
        
        scm_create(project, cfg)

    def scm_create(project, cfg):
        click.echo(f'We\'re going to create this thing in {project.scm_provider} now!')

        url = "https://gitlab.com/api/v4/projects?name=" + project.name

        try:
            headers = {
                  'private-token': cfg["source_control"]["gitlab"]["pat"]
            }
            r = requests.request("POST", url, headers=headers)
            print(r.text)
        except Exception as e:
            print(e)

        tfc_create(project, cfg)

    def tfc_create(project, cfg):
        click.echo(f'Creating workspace in Terraform Cloud now!')

        url = "https://app.terraform.io/api/v2/organizations/" + cfg["terraform_cloud"]["workspace"] + "/workspaces"
        print(url)

        try:
            headers = {
                'Content-Type': 'application/vnd.api+json',
                'Authorization': 'Bearer ' + cfg["terraform_cloud"]["bearer_token"]
            }
            payload = json.dumps({
                "data": {
                    "attributes": {
                    "name": project.name,
                    "resource-count": 0,
                    "updated-at": "2017-11-29T19:18:09.976Z"
                    },
                    "type": "workspaces"
                    }
                })
            r = requests.request("POST", url, headers=headers, data=payload)
            print(r.text)
        except Exception as e:
            print(e)

    try:
        local_create(project, project.cfg)
    except Exception as e:
        print(e)
