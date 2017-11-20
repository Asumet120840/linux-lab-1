import click
import requests

from PIL import Image
from StringIO import StringIO
from selenium import webdriver

@click.command()
@click.option('--as-cowboy', '-c', is_flag=True, help='Greet as a cowboy.')
@click.argument('name', default='world', required=False)
def main(name, as_cowboy):
    	"""Get image IG"""
    	browser = webdriver.Chrome()
	browser.set_window_size(0, 0)
	browser.get('https://www.instagram.com/{}'.format(name))	
	content = browser.find_element_by_class_name("_9bt3u")
	src = content.get_attribute('src')
	browser.close()
	req=requests.get(src)
	img=Image.open(StringIO(req.content))
	img.show()

	
