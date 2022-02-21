import click

import create
import destroy
import utils

class Project(object):
    def __init__(self, name, path, scm_provider, cfg):
        self.name = name
        self.path = path
        self.scm_provider = scm_provider
        self.cfg = cfg        

# @click.group(chain=True, invoke_without_command=True)
@click.group()
@click.option('--name', default="robertocampana", help="Name of the project")
@click.option('--path', default="/users/Agency/git", help="Local location for the project")
@click.option('--scm_provider', default="Gitlab", help="SCM provider (e.g.; GitHub, Gitlab")
@click.pass_context
def cli(ctx, name, path, scm_provider):
    '''
    CLI tool to create and destroy Terraform bootstrapping projects locally, in source control, as well as in Terraform Cloud.
    '''

    cfg = utils.load_config()
    print(cfg)
    ctx.obj = Project(name, path, scm_provider, cfg)

    # print(ctx.obj.name)
    # print(ctx.obj.path)
    # print(ctx.obj.scm_provider)

cli.add_command(create.create)
cli.add_command(destroy.destroy)

if __name__ == '__main__':
    cli()