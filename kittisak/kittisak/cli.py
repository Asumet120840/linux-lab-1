import click
import requests

from PIL import Image
from StringIO import StringIO

@click.command()
@click.option('--as-cowboy', '-c', is_flag=True, help='Computer Science at UBU')
@click.argument('name', default='100009851460255', required=False)
def main(name, as_cowboy):
    """Get Profile Picture FB"""
    #greet = 'Howdy' if as_cowboy else 'Hello'
    #click.echo('{0}, {1}.'.format(greet, name))
    url = 'https://graph.facebook.com/{}/picture?type=large'.format(name)
    res = requests.get(url)
    img = Image.open(StringIO(res.content))
    img.show()
