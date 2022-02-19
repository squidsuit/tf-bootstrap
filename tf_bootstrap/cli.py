import click

import create
import destroy

@click.group(chain=True, invoke_without_command=True)
def cli():
    '''
    CLI tool to create and destroy Terraform bootstrapping projects locally, in GitHub, as well as in Terraform Cloud.
    '''
    pass

cli.add_command(create.create)
cli.add_command(destroy.destroy)

if __name__ == '__main__':
    cli()