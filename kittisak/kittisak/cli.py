import click
import requests
import time

from PIL import Image
from StringIO import StringIO
from selenium import webdriver

@click.command()
@click.option('--as-cowboy', '-c', is_flag=True, help='Greet as a cowboy.')
@click.argument('name', default='', required=False)
@click.argument('pw', default='', required=False)
def main(name,pw,as_cowboy):
    	"""Get picture in Reg"""
    	#greet = 'Howdy' if as_cowboy else 'Hello'
    	#click.echo('{0}, {1}.'.format(greet, name))
	browser = webdriver.Chrome()
	browser.get('https://reg1.ubu.ac.th/registrar/login.asp')
	id=browser.find_element_by_name('f_uid')
	id.send_keys(name)
	pas=browser.find_element_by_name('f_pwd')
	pas.send_keys(pw)
	pas.submit()
	browser.get('https://reg1.ubu.ac.th/registrar/getstudentimageftp.asp?id={}'.format(name))
	browser.save_screenshot('profile.png')
	browser.close()
	time.sleep(2)
	url=StringIO(open('profile.png','rb').read())
	img=Image.open(url)
	img=img.crop((img.size[0]/2-220,img.size[1]/2-233,img.size[0]/2+220,img.size[1]/2+234))
	img.show()
	img.save("profile.png")
