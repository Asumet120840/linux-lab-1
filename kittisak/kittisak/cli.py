import click
import requests

from PIL import Image
from StringIO import StringIO

@click.command()
@click.option('--as-author', '-c', is_flag=True, help='Computer Science at UBU')
@click.argument('name', default='', required=False)
def main(name, as_author):
    	"""Get Github Avatar"""
	url = 'https://graph.facebook.com/{}/picture?type=large'.format(name)
	res = requests.get(url)
	img = Image.open(StringIO(res.content))
	img.show()
